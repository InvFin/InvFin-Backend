# Generated by Django 3.2.15 on 2022-09-29 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=6000000)),
                ('name', models.CharField(max_length=600000)),
                ('exchange', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresas.exchange')),
            ],
            options={
                'verbose_name': 'ETF',
                'verbose_name_plural': 'ETFs',
                'db_table': 'etfs',
            },
        ),
        migrations.CreateModel(
            name='EtfComposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('company_size', models.FloatField(blank=True, null=True)),
                ('number_shares', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('company_related', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresas.company')),
                ('etf_related', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='etfs.etf')),
            ],
            options={
                'verbose_name': 'ETF composition',
                'verbose_name_plural': 'ETFs composition',
                'db_table': 'etfs_composition',
            },
        ),
    ]
