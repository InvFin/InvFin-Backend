# Generated by Django 3.2.15 on 2022-11-12 19:00

import apps.general.mixins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0002_auto_20221105_2044'),
        ('periods', '0002_auto_20221105_2044'),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAsReportedProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('empresas.company',),
        ),
        migrations.CreateModel(
            name='IncomeStatementAsReported',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('financial_data', models.JSONField()),
                ('from_file', models.CharField(default='', max_length=250, null=True)),
                ('from_folder', models.CharField(default='', max_length=250, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inc_statements_as_reported', to='empresas.company')),
                ('period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='periods.period')),
                ('reported_currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='currencies.currency')),
            ],
            options={
                'db_table': 'assets_income_statement_as_reported',
            },
            bases=(models.Model, apps.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name='CashflowStatementAsReported',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('financial_data', models.JSONField()),
                ('from_file', models.CharField(default='', max_length=250, null=True)),
                ('from_folder', models.CharField(default='', max_length=250, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cf_statements_as_reported', to='empresas.company')),
                ('period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='periods.period')),
                ('reported_currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='currencies.currency')),
            ],
            options={
                'db_table': 'assets_cashflow_statement_as_reported',
            },
            bases=(models.Model, apps.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name='BalanceSheetAsReported',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('financial_data', models.JSONField()),
                ('from_file', models.CharField(default='', max_length=250, null=True)),
                ('from_folder', models.CharField(default='', max_length=250, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='balance_sheets_as_reported', to='empresas.company')),
                ('period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='periods.period')),
                ('reported_currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='currencies.currency')),
            ],
            options={
                'db_table': 'assets_balance_sheet_as_reported',
            },
            bases=(models.Model, apps.general.mixins.BaseToAllMixin),
        ),
    ]