# Generated by Django 3.2.15 on 2022-11-04 22:43

import apps.general.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=500, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('spanish_name', models.CharField(blank=True, max_length=500, null=True)),
                ('iso', models.CharField(blank=True, max_length=500, null=True)),
                ('alpha_2_code', models.CharField(blank=True, max_length=2, null=True)),
                ('alpha_3_code', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'assets_countries',
            },
            bases=(models.Model, apps.general.mixins.BaseToAllMixin),
        ),
    ]