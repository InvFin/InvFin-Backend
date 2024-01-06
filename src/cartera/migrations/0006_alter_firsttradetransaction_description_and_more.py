# Generated by Django 4.2.7 on 2023-11-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cartera", "0005_firsttradetransaction_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="firsttradetransaction",
            name="description",
            field=models.CharField(default="", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="firsttradetransaction",
            name="price",
            field=models.DecimalField(decimal_places=4, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name="firsttradetransaction",
            name="quantity",
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name="firsttradetransaction",
            name="symbol",
            field=models.CharField(default="", max_length=20, null=True),
        ),
    ]