# Generated by Django 4.2.7 on 2023-12-23 17:46

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cartera", "0010_networth_savings_spendings_remove_spend_category_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="networth",
            old_name="amount",
            new_name="equity",
        ),
        migrations.AddField(
            model_name="networth",
            name="incomes",
            field=models.DecimalField(decimal_places=3, default=Decimal("0"), max_digits=100),
        ),
        migrations.AddField(
            model_name="networth",
            name="investments",
            field=models.DecimalField(decimal_places=3, default=Decimal("0"), max_digits=100),
        ),
        migrations.AddField(
            model_name="networth",
            name="savings",
            field=models.DecimalField(decimal_places=3, default=Decimal("0"), max_digits=100),
        ),
        migrations.AddField(
            model_name="networth",
            name="spendings",
            field=models.DecimalField(decimal_places=3, default=Decimal("0"), max_digits=100),
        ),
    ]