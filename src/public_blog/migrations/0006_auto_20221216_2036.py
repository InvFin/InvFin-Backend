# Generated by Django 3.2.16 on 2022-12-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_blog', '0005_publicblogasnewsletter_call_to_action_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicblogasnewsletter',
            name='call_to_action',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='publicblogasnewsletter',
            name='call_to_action_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]