from decimal import Decimal
import random
from typing import Dict, List, Union

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import (
    SET_NULL,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DecimalField,
    ForeignKey,
    IntegerField,
    JSONField,
    ManyToManyField,
    Model,
    OneToOneField,
    PositiveIntegerField,
    TextField,
)

from src.currencies.models import Currency
from src.general.utils import ChartSerializer
from src.empresas.outils.data_management.show.company_data import CompanyData

User = get_user_model()


class Asset(Model):
    user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    content_type = ForeignKey(ContentType, on_delete=SET_NULL, null=True)
    object_id = PositiveIntegerField()
    object = GenericForeignKey("content_type", "object_id")
    is_stock = BooleanField(default=False)
    is_etf = BooleanField(default=False)
    is_crypto = BooleanField(default=False)

    class Meta:
        verbose_name = "Asset"
        verbose_name_plural = "Assets"
        db_table = "cartera_assets"

    def __str__(self):
        return self.object.name if self.object else ""

    @property
    def amount_invested(self):
        # TODO: change it into a queryset
        return sum(move.movement_cost for move in self.movements.filter(asset_related=self))


class PositionMovement(Model):
    MOVE = ((1, "Compra"), (2, "Venta"))

    user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    move_type = IntegerField(choices=MOVE, null=True, blank=True)
    asset_related = ForeignKey(
        Asset,
        null=True,
        blank=True,
        on_delete=SET_NULL,
        related_name="movements",
    )
    price = DecimalField("Precio", max_digits=100, decimal_places=2, default=0)
    date = DateField("Fecha del movimiento", null=True, blank=True)
    quantity = IntegerField("Cantidad", default=0)
    currency = ForeignKey(Currency, on_delete=SET_NULL, null=True, blank=True)
    observacion = TextField("Observaciones", default="")
    fee = DecimalField("Comisión", max_digits=100, decimal_places=2, default=0)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Position movement"
        verbose_name_plural = "Position movements"
        db_table = "cartera_movements"

    def __str__(self):
        return str(self.id)

    @property
    def movement_cost(self):
        # TODO: change it into a queryset
        total = (self.price * self.quantity) + self.fee
        if self.move_type == 2:
            total = total * (-1)
        return total

    @property
    def movement(self):
        return "Compra" if self.move_type == 1 else "Venta"


class CashflowMovementCategory(Model):
    name = CharField("Nombre", max_length=1000)
    date_created = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cashflow category"
        verbose_name_plural = "Cashflow categories"
        db_table = "cartera_cashflow_category"

    def __str__(self):
        return self.name


class CashflowMovement(Model):
    user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    name = CharField("Nombre", max_length=1000)
    amount = DecimalField("Monto", max_digits=100, decimal_places=2, default=0)
    description = TextField("Descripción", default="")
    date = DateField("Fecha del movimiento", null=True, blank=True)
    currency = ForeignKey(Currency, on_delete=SET_NULL, null=True, blank=True)
    is_recurrent = BooleanField(default=False)
    category = ForeignKey(CashflowMovementCategory, on_delete=SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ["-date"]

    def __str__(self):
        return self.name


class Income(CashflowMovement):
    class Meta:
        verbose_name = "Income"
        verbose_name_plural = "Incomes"
        db_table = "cartera_income"


class Spend(CashflowMovement):
    class Meta:
        verbose_name = "Spend"
        verbose_name_plural = "Spends"
        db_table = "cartera_spend"


class FinancialObjectif(Model):
    user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    name = CharField("Nombre", max_length=1000)
    date_created = DateTimeField(auto_now_add=True)
    date_to_achieve = DateTimeField(null=True, blank=True)
    date_achived = DateTimeField(null=True, blank=True)
    observation = TextField("Observaciones", default="")
    accomplished = BooleanField(default=False)
    abandoned = BooleanField(default=False)
    percentage = DecimalField("Porcentaje", max_digits=100, decimal_places=2, default=0)
    amount = DecimalField("Monto", max_digits=100, decimal_places=2, default=0)
    is_rule = BooleanField(default=False)
    rule_ends = BooleanField(default=False)
    requirement = JSONField(default=dict)
    start_date = DateTimeField(null=True, blank=True)
    end_date = DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["date_created"]
        verbose_name = "Objetivo financiero"
        verbose_name_plural = "Objetivo financieros"
        db_table = "cartera_objectives"


class Patrimonio(Model, ChartSerializer):
    user = OneToOneField(
        User,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name="user_patrimoine",
    )
    assets = ManyToManyField(Asset, blank=True)
    objectives = ManyToManyField(FinancialObjectif, blank=True)
    default_currency = ForeignKey(
        Currency,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        default="1",
    )

    class Meta:
        verbose_name = "Patrimonio"
        verbose_name_plural = "Patrimonios"
        db_table = "cartera_patrimoine"

    def __str__(self):
        return self.user.username if self.user else ""

    def gastos_totales(self, ingresos_totales):
        # TODO: change it into a queryset
        spends = Spend.objects.filter(user=self.user)
        gastos_totales = sum(Decimal(item.amount) for item in spends)
        if gastos_totales is None:
            gastos_totales = 0
        return {
            "total": gastos_totales,
            "spends": spends,
            "percentage": (
                ((gastos_totales / ingresos_totales) * 100) if ingresos_totales != 0 else 0
            ),
        }

    @property
    def ingresos_totales(self):
        # TODO: change it into a queryset
        incomes = Income.objects.filter(user=self.user)
        total = sum(Decimal(item.amount) for item in incomes)
        if total is None:
            total = 0
        return {"total": total, "incomes": incomes}

    def cantidad_total_invertida(self, ingresos_totales):
        # TODO: change it into a queryset
        cantidad_total_invertida = sum(item.amount_invested for item in self.assets.all())
        if cantidad_total_invertida is None:
            cantidad_total_invertida = 0
        return {
            "total": cantidad_total_invertida,
            "percentage": (
                ((cantidad_total_invertida / ingresos_totales) * 100)
                if ingresos_totales != 0
                else 0
            ),
        }

    def ahorros_totales(self, ingresos_totales, gastos_totales, cantidad_total_invertida):
        ahorros_totales = ingresos_totales - gastos_totales - cantidad_total_invertida
        return {
            "total": ahorros_totales,
            "percentage": (
                (((ahorros_totales) / ingresos_totales) * 100) if ingresos_totales != 0 else 0
            ),
        }

    @property
    def patrimoine(self):
        total_income_earned = self.ingresos_totales
        total_income_spend = self.gastos_totales(total_income_earned["total"])
        income_invested = self.cantidad_total_invertida(total_income_earned["total"])
        income_saved = self.ahorros_totales(
            total_income_earned["total"], total_income_spend["total"], income_invested["total"]
        )

        percentage_spend = total_income_spend["percentage"]
        percentage_saved = income_saved["percentage"]
        percentage_invested = income_invested["percentage"]
        percentage_earned = 100 - percentage_spend - percentage_saved - percentage_invested

        incomes_and_spends = list(total_income_earned["incomes"]) + list(
            total_income_spend["spends"]
        )
        income_earned = total_income_earned["total"]
        income_spend = total_income_spend["total"]
        income_saved = income_saved["total"]
        income_invested = income_invested["total"]

        return {
            "income_earned": f"{income_earned}",
            "income_spend": f"{income_spend}",
            "income_saved": f"{income_saved}",
            "income_invested": f"{income_invested}",
            "incomes_and_spends": incomes_and_spends,
            "percentage_earned": percentage_earned,
            "percentage_spend": percentage_spend,
            "percentage_saved": percentage_saved,
            "percentage_invested": percentage_invested,
        }

    def prepare_chart_data(self, main_key, main_dict):
        data = {"labels": [], "datasets": []}
        dataset = {"label": main_key, "data": [], "backgroundColor": [], "hoverOffset": 4}

        for key, value in main_dict.items():
            data["labels"].append(key)
            dataset["data"].append(value)
            dataset["backgroundColor"].append(
                "#" + "".join([random.choice("ABCDEF0123456789") for _ in range(6)])
            )

        data["datasets"].append(dataset)

        return {
            "type": "doughnut",
            "data": data,
            "options": {
                "responsive": "true",
                "maintainAspectRatio": "false",
                "plugins": {
                    "legend": {
                        "position": "top",
                    },
                    "title": {"display": "true", "text": main_key},
                },
            },
        }

    @property
    def overall_portfolio_information(self):
        income_invested = self.cantidad_total_invertida(self.ingresos_totales["total"])
        total_invertido = float(income_invested["total"])
        overall_portfolio_information: Dict[str, Union[float, int, List]] = {
            "positions": [],
            # 'average_cash_conversion_ratio': 0,
            "average_roce": 0,
            "average_gross_margin": 0,
            "average_net_income_margin": 0,
            "average_interest_coverage": 0,
            "average_roic": 0,
            "average_price_earnings": 0,
            "average_current_ratio": 0,
            "average_quick_ratio": 0,
        }

        for asset in self.assets.filter(is_stock=True):
            amount_invested = float(asset.amount_invested)
            empresa = asset.object
            ratios = CompanyData(empresa).get_ratios_information()
            percentage_invested = (
                ((amount_invested / total_invertido) * 100) if total_invertido != 0 else 0
            )

            # overall_portfolio_information['average_cash_conversion_ratio'] += ratios.average * percentage_invested
            overall_portfolio_information["average_roce"] += (
                ratios["average_roce"] * percentage_invested
            ) / 100
            overall_portfolio_information["average_gross_margin"] += (
                ratios["average_gross_margin"] * percentage_invested
            ) / 100
            overall_portfolio_information["average_net_income_margin"] += (
                ratios["average_net_income_margin"] * percentage_invested
            ) / 100
            overall_portfolio_information["average_interest_coverage"] += (
                ratios["average_interest_coverage"] * percentage_invested
            ) / 100
            overall_portfolio_information["average_roic"] += (
                ratios["average_roic"] * percentage_invested
            ) / 100
            overall_portfolio_information["average_price_earnings"] += (
                ratios["average_price_earnings"] * percentage_invested
            ) / 100
            overall_portfolio_information["average_current_ratio"] += (
                ratios["average_current_ratio"] * percentage_invested
            ) / 100
            overall_portfolio_information["average_quick_ratio"] += (
                ratios["average_quick_ratio"] * percentage_invested
            ) / 100

            overall_portfolio_information["positions"].append(
                {
                    "empresa": empresa,
                    "amount_invested": amount_invested,
                    "percentage_invested": percentage_invested,
                    "company_valuation": ratios,
                }
            )
        return overall_portfolio_information

    def positions_segmentation_information(self, total_invertido):
        positions_information = {
            "empresas": [],
            "segmentation": [],
            "positons_moves": PositionMovement.objects.filter(user=self.user),
        }

        segmentation = {"Sectores": {}, "Indústrias": {}, "Países": {}, "Mercados": {}}

        for empresa in self.assets.filter(is_stock=True):
            amount_invested = float(empresa.amount_invested)
            empresa = empresa.object
            empresa_sector = empresa.sector.sector
            empresa_industry = empresa.industry.industry
            empresa_country = empresa.country.country
            empresa_exchange = empresa.exchange.exchange

            if empresa_sector not in segmentation["Sectores"]:
                segmentation["Sectores"][empresa_sector] = 1
            else:
                segmentation["Sectores"][empresa_sector] += 1

            if empresa_industry not in segmentation["Indústrias"]:
                segmentation["Indústrias"][empresa_industry] = 1
            else:
                segmentation["Indústrias"][empresa_industry] += 1

            if empresa_country not in segmentation["Países"]:
                segmentation["Países"][empresa_country] = 1
            else:
                segmentation["Países"][empresa_country] += 1

            if empresa_exchange not in segmentation["Mercados"]:
                segmentation["Mercados"][empresa_exchange] = 1
            else:
                segmentation["Mercados"][empresa_exchange] += 1

            empresa_info = {
                "name": empresa.name,
                "ticker": empresa.ticker,
                "amount_invested": amount_invested,
                "percentage_invested": (
                    ((amount_invested / total_invertido) * 100) if total_invertido != 0 else 0
                ),
            }
            positions_information["empresas"].append(empresa_info)

        for key, value in segmentation.items():
            chart_data = self.prepare_chart_data(key, value)
            positions_information["segmentation"].append(chart_data)

        return positions_information

    @property
    def balance_sheet(self):
        income_invested = self.cantidad_total_invertida(self.ingresos_totales["total"])
        total_invertido = float(income_invested["total"])
        return self.positions_segmentation_information(total_invertido)
