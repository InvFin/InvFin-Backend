from django.contrib import admin

from src.empresas.models import Exchange, ExchangeOrganisation


class ExchangeInline(admin.StackedInline):
    model = Exchange
    fields = [
        "exchange_ticker",
        "exchange",
        "country",
        "data_source",
    ]
    extra = 0
    jazzmin_tab_id = "exchanges"


@admin.register(ExchangeOrganisation)
class ExchangeOrganisationAdmin(admin.ModelAdmin):
    inlines = [ExchangeInline]
    list_display = [
        "id",
        "name",
        "image",
        "sub_exchange1",
        "sub_exchange2",
        "order",
    ]
    list_editable = ["order"]
    search_fields = ["name"]
    jazzmin_form_tabs = [
        ("general", "Main Organisation Exchanges"),
        ("exchanges", "Exchanges"),
    ]
