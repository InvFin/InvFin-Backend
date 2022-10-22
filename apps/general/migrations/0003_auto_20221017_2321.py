# Generated by Django 3.2.15 on 2022-10-17 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailnotification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='emailnotification',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]