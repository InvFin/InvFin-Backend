# Generated by Django 3.2.14 on 2022-07-27 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_promotion_promotioncampaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteemailstype',
            name='name',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='websitelegalpage',
            name='slug',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='websitelegalpage',
            name='title',
            field=models.CharField(max_length=800),
        ),
    ]