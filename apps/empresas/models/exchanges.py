from apps.empresas import constants

from django.db.models import (
    SET_NULL,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    FloatField,
    ForeignKey,
    IntegerField,
    JSONField,
    Model,
    PositiveIntegerField,
    TextField,
)


class ExchangeOrganisation(Model):
    name = CharField(max_length=250, null=True, blank=True)
    image = CharField(max_length=250, null=True, blank=True)
    sub_exchange1 = CharField(max_length=250, null=True, blank=True)
    sub_exchange2 = CharField(max_length=250, null=True, blank=True)
    order = PositiveIntegerField( null=True, blank=True)

    class Meta:
        verbose_name = "Organisation exchange"
        verbose_name_plural = "Organisation exchanges"
        db_table = "assets_exchanges_organisations"

    def __str__(self):
        return str(self.name)


class Exchange(Model):
    exchange_ticker = CharField(max_length=30, null=True, blank=True)
    exchange = CharField(max_length=250, null=True, blank=True)
    country = ForeignKey("general.Country", on_delete=SET_NULL, null=True, blank=True)
    main_org = ForeignKey(ExchangeOrganisation, on_delete=SET_NULL, null=True, blank=True)
    data_source = CharField(
        max_length=100,
        choices=constants.DATA_SOURCES,
        default=constants.DATA_SOURCE_FINPREP
    )

    class Meta:
        ordering = ['-exchange_ticker']
        verbose_name = "Exchange"
        verbose_name_plural = "Exchanges"
        db_table = "assets_exchanges"

    def __str__(self):
        return str(self.exchange_ticker)

    @property
    def num_emps(self):
        return self.companies.all().count()
