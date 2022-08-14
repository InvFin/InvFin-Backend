from email.policy import default
from django.db.models import JSONField, Model, ForeignKey, SET_NULL

from apps.empresas.models import Company


class StatementsFinnhub(Model):
    company = ForeignKey(Company, on_delete=SET_NULL, null=True, blank=True)
    financials = JSONField(default={})

    class Meta:
        verbose_name = "Finnhub All Statements"
        verbose_name_plural = "Finnhub All Statements"
        db_table = "assets_companies_all_statements_finnhub"

    def __str__(self):
        return self.company.ticker
