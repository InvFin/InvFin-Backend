# Generated by Django 3.2.16 on 2022-10-23 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public_blog', '0007_delete_emailpublicblog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailPublicBlog',
        ),
    ]