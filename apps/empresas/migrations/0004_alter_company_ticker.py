# Generated by Django 3.2.12 on 2022-05-12 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_auto_20220415_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='ticker',
            field=models.CharField(db_index=True, max_length=30, unique=True),
        ),
    ]