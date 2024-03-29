# Generated by Django 3.2.15 on 2022-12-31 14:33

from django.db import migrations, models
import src.general.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('slug', models.CharField(blank=True, max_length=500, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'db_table': 'categories',
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('slug', models.CharField(blank=True, max_length=500, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'db_table': 'tags',
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
    ]
