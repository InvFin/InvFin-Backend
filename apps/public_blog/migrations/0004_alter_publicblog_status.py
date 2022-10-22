# Generated by Django 3.2.15 on 2022-10-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_blog', '0003_publicblog_extra_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicblog',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Publicado'), (2, 'Borrador'), (3, 'Programado'), (4, 'Necesita revisión')], default=2),
        ),
    ]