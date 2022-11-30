# Generated by Django 3.2.15 on 2022-11-28 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('web', '0002_roadmap_roadmapcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteemail',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='websiteemail',
            name='object_id',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]