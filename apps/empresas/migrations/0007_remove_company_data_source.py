# Generated by Django 3.2.15 on 2022-08-15 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0006_auto_20220815_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='data_source',
        ),
    ]