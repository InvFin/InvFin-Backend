# Generated by Django 3.2.14 on 2022-07-25 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recsys', '0002_auto_20220725_2252'),
        ('business', '0004_auto_20220725_2252'),
        ('seo', '0011_auto_20220725_2252'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Promotion',
        ),
        migrations.DeleteModel(
            name='PromotionCampaign',
        ),
    ]
