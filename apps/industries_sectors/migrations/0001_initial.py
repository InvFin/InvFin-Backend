# Generated by Django 3.2.15 on 2022-11-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(blank=True, max_length=500, null=True)),
                ('industry_spanish', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Industry',
                'verbose_name_plural': 'Industries',
                'db_table': 'assets_industries',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(blank=True, max_length=500, null=True)),
                ('sector_spanish', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectors',
                'db_table': 'assets_sectors',
            },
        ),
    ]
