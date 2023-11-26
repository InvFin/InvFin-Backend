# Generated by Django 4.2.7 on 2023-11-26 16:44

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import src.general.mixins


class Migration(migrations.Migration):
    dependencies = [
        ("currencies", "0003_remove_currency_accronym_currency_code_and_more"),
        ("periods", "0001_initial"),
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cartera", "0009_ingestransaction_currency_ingestransaction_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="NetWorth",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=3, default=Decimal("0"), max_digits=100
                    ),
                ),
                (
                    "period",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="periods.period",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="net_worth",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "patrimoine_net_worth",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name="Savings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, verbose_name="Nombre")),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=3,
                        default=Decimal("0"),
                        max_digits=100,
                        verbose_name="Monto",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, default="", verbose_name="Descripción"),
                ),
                (
                    "comment",
                    models.TextField(blank=True, default="", verbose_name="Comentario"),
                ),
                ("date", models.DateField(blank=True, verbose_name="Fecha del movimiento")),
                ("transaction_file_id", models.PositiveIntegerField(null=True)),
                ("is_recurrent", models.BooleanField(blank=True, default=False)),
                ("read", models.BooleanField(blank=True, default=False)),
                (
                    "amount_converted",
                    models.DecimalField(
                        blank=True, decimal_places=3, default=Decimal("0"), max_digits=100
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="cartera.cashflowmovementcategory",
                    ),
                ),
                (
                    "currency",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="currencies.currency",
                    ),
                ),
                (
                    "net_worth",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="net_worth_savings",
                        to="cartera.networth",
                    ),
                ),
                (
                    "transaction_file_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="savings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "patrimoine_savings",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name="Spendings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, verbose_name="Nombre")),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=3,
                        default=Decimal("0"),
                        max_digits=100,
                        verbose_name="Monto",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, default="", verbose_name="Descripción"),
                ),
                (
                    "comment",
                    models.TextField(blank=True, default="", verbose_name="Comentario"),
                ),
                ("date", models.DateField(blank=True, verbose_name="Fecha del movimiento")),
                ("transaction_file_id", models.PositiveIntegerField(null=True)),
                ("is_recurrent", models.BooleanField(blank=True, default=False)),
                ("read", models.BooleanField(blank=True, default=False)),
                (
                    "amount_converted",
                    models.DecimalField(
                        blank=True, decimal_places=3, default=Decimal("0"), max_digits=100
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="cartera.cashflowmovementcategory",
                    ),
                ),
                (
                    "currency",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="currencies.currency",
                    ),
                ),
                (
                    "net_worth",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="net_worth_spendings",
                        to="cartera.networth",
                    ),
                ),
                (
                    "transaction_file_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="spendings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "patrimoine_spendings",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
        migrations.RemoveField(
            model_name="spend",
            name="category",
        ),
        migrations.RemoveField(
            model_name="spend",
            name="currency",
        ),
        migrations.RemoveField(
            model_name="spend",
            name="transaction_file_type",
        ),
        migrations.RemoveField(
            model_name="spend",
            name="user",
        ),
        migrations.AddField(
            model_name="income",
            name="amount_converted",
            field=models.DecimalField(
                blank=True, decimal_places=3, default=Decimal("0"), max_digits=100
            ),
        ),
        migrations.AddField(
            model_name="income",
            name="comment",
            field=models.TextField(blank=True, default="", verbose_name="Comentario"),
        ),
        migrations.AddField(
            model_name="income",
            name="content_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="assets_income",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="income",
            name="object_id",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="income",
            name="read",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name="investment",
            name="amount_converted",
            field=models.DecimalField(
                blank=True, decimal_places=3, default=Decimal("0"), max_digits=100
            ),
        ),
        migrations.AddField(
            model_name="investment",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="cartera.cashflowmovementcategory",
            ),
        ),
        migrations.AddField(
            model_name="investment",
            name="comment",
            field=models.TextField(blank=True, default="", verbose_name="Comentario"),
        ),
        migrations.AddField(
            model_name="investment",
            name="is_recurrent",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name="investment",
            name="read",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name="financialobjectif",
            name="amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal("0"), max_digits=100, verbose_name="Monto"
            ),
        ),
        migrations.AlterField(
            model_name="financialobjectif",
            name="percentage",
            field=models.DecimalField(
                decimal_places=3,
                default=Decimal("0"),
                max_digits=100,
                verbose_name="Porcentaje",
            ),
        ),
        migrations.AlterField(
            model_name="firsttradetransaction",
            name="amount",
            field=models.DecimalField(decimal_places=3, default=Decimal("0"), max_digits=100),
        ),
        migrations.AlterField(
            model_name="firsttradetransaction",
            name="commission",
            field=models.DecimalField(decimal_places=3, default=Decimal("0"), max_digits=100),
        ),
        migrations.AlterField(
            model_name="firsttradetransaction",
            name="cusip",
            field=models.CharField(blank=True, default="", max_length=9),
        ),
        migrations.AlterField(
            model_name="firsttradetransaction",
            name="description",
            field=models.CharField(blank=True, default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="firsttradetransaction",
            name="fee",
            field=models.DecimalField(decimal_places=3, default=Decimal("0"), max_digits=100),
        ),
        migrations.AlterField(
            model_name="firsttradetransaction",
            name="interest",
            field=models.DecimalField(decimal_places=3, default=Decimal("0"), max_digits=100),
        ),
        migrations.AlterField(
            model_name="firsttradetransaction",
            name="quantity",
            field=models.DecimalField(decimal_places=3, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name="firsttradetransaction",
            name="symbol",
            field=models.CharField(blank=True, default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="income",
            name="amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal("0"), max_digits=100, verbose_name="Monto"
            ),
        ),
        migrations.AlterField(
            model_name="income",
            name="date",
            field=models.DateField(
                blank=True,
                default=django.utils.timezone.now,
                verbose_name="Fecha del movimiento",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="income",
            name="description",
            field=models.TextField(blank=True, default="", verbose_name="Descripción"),
        ),
        migrations.AlterField(
            model_name="income",
            name="is_recurrent",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name="income",
            name="transaction_file_id",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="ingestransaction",
            name="amount",
            field=models.DecimalField(decimal_places=3, default=Decimal("0"), max_digits=100),
        ),
        migrations.AlterField(
            model_name="ingestransaction",
            name="balance",
            field=models.DecimalField(decimal_places=3, default=Decimal("0"), max_digits=100),
        ),
        migrations.AlterField(
            model_name="ingestransaction",
            name="category",
            field=models.CharField(blank=True, default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="ingestransaction",
            name="comment",
            field=models.CharField(blank=True, default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="ingestransaction",
            name="description",
            field=models.CharField(blank=True, default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="ingestransaction",
            name="image",
            field=models.CharField(blank=True, default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="ingestransaction",
            name="subcaterogy",
            field=models.CharField(blank=True, default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="investment",
            name="amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal("0"), max_digits=100, verbose_name="Monto"
            ),
        ),
        migrations.AlterField(
            model_name="investment",
            name="date",
            field=models.DateField(
                blank=True,
                default=django.utils.timezone.now,
                verbose_name="Fecha del movimiento",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="investment",
            name="description",
            field=models.TextField(blank=True, default="", verbose_name="Descripción"),
        ),
        migrations.AlterField(
            model_name="investment",
            name="price",
            field=models.DecimalField(
                decimal_places=3, default=Decimal("0"), max_digits=100, verbose_name="Precio"
            ),
        ),
        migrations.AlterField(
            model_name="investment",
            name="quantity",
            field=models.DecimalField(
                decimal_places=3, default=Decimal("0"), max_digits=100, verbose_name="Cantidad"
            ),
        ),
        migrations.AlterField(
            model_name="investment",
            name="transaction_file_id",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name="Saving",
        ),
        migrations.DeleteModel(
            name="Spend",
        ),
        migrations.AddField(
            model_name="income",
            name="net_worth",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="net_worth_incomes",
                to="cartera.networth",
            ),
        ),
        migrations.AddField(
            model_name="investment",
            name="net_worth",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="net_worth_investments",
                to="cartera.networth",
            ),
        ),
    ]
