# Generated by Django 3.2.16 on 2023-08-20 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jwt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_date', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('refresh', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='refreshed_by', to='api.jwt')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jwt', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Jwt',
                'verbose_name_plural': 'Jwt',
                'db_table': 'jwts',
                'ordering': ['-created_at'],
            },
        ),
    ]