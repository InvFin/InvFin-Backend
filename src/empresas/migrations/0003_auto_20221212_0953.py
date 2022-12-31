# Generated by Django 3.2.15 on 2022-12-12 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_rename_account_payables_balancesheet_accounts_payable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eficiencyratio',
            old_name='payables_turnover',
            new_name='accounts_payable_turnover',
        ),
        migrations.RenameField(
            model_name='eficiencyratio',
            old_name='fcf_to_operating_cf',
            new_name='free_cashflow_to_operating_cashflow',
        ),
        migrations.RenameField(
            model_name='nongaap',
            old_name='average_payables',
            new_name='average_accounts_payable',
        ),
    ]
