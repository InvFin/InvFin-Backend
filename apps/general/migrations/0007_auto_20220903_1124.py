# Generated by Django 3.2.15 on 2022-09-03 09:24
import pandas as pd

from django.db import migrations, models

from apps.translate.google_trans_new import google_translator
from apps.general.countries_data import COUNTRIES, ALT_CODES


def populate_countries(apps, schema):
    Country = apps.get_model('general', 'country')
    for country_alpha_2, country_name in COUNTRIES.items():
        obj, created = Country.objects.get_or_create(country=country_alpha_2)
        alt_code = ALT_CODES[country_alpha_2]
        obj.alpha_2_code = country_alpha_2
        obj.alpha_3_code = alt_code[0]
        obj.name = country_name
        obj.spanish_name = google_translator().translate(country_name, lang_src='en', lang_tgt='es')
        obj.iso = alt_code[1]
        obj.save()


def populate_currencies(apps, schema):
    Country = apps.get_model('general', 'country')
    Currency = apps.get_model('general', 'currency')
    df = pd.read_csv('currencies.csv')
    for key, value in df[df.columns[:4]].iterrows():
        country_name = value["Country"]
        currency_name = value["Currency Name"]
        code_alpha = value["Code A"]
        code_num = value["Code N"]
        country, created = Country.objects.get_or_create(name=country_name)
        currency, created = Currency.objects.get_or_create(currency=code_alpha)
        currency.countries.add(country)
        currency.name = currency_name
        currency.accronym = code_alpha
        currency.iso = code_num
        currency.save(update_fields=["name", "iso", "accronym"])
    df = df.loc[:, ['Currency_code',"Symbol"]]
    df = df.dropna()
    for key, value in df.iterrows():
        try:
            currency = Currency.objects.get(accronym=value["Currency_code"])
        except:
            continue
        else:
            currency.symbol = value["Symbol"]
            currency.save()




class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_auto_20220902_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='country',
        ),
        migrations.AddField(
            model_name='currency',
            name='countries',
            field=models.ManyToManyField(blank=True, related_name='currency', to='general.Country'),
        ),
        migrations.AddField(
            model_name='country',
            name='spanish_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='currency',
            name='spanish_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),

        migrations.AddField(
            model_name='currency',
            name='accronym',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.RunPython(populate_countries),
        migrations.RunPython(populate_currencies),
    ]
