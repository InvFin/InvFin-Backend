# Generated by Django 3.2.12 on 2022-06-20 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20220613_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='for_testing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='for_testing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productcomplementary',
            name='for_testing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productcomplementarypaymentlink',
            name='for_testing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productdiscount',
            name='for_testing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productdiscount',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='stripewebhookresponse',
            name='for_testing',
            field=models.BooleanField(default=False),
        ),
    ]
