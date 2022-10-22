# Generated by Django 3.2.15 on 2022-10-08 07:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteemail',
            name='users_selected',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='websiteemail',
            name='whom_to_send',
            field=models.CharField(choices=[('all', 'All'), ('type_related', 'Type related'), ('selected', 'Selected')], default='all', max_length=800),
        ),
    ]