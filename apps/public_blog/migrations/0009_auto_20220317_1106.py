# Generated by Django 3.2.12 on 2022-03-17 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public_blog', '0008_emailpublicblog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicblogasnewsletter',
            name='default_despedida',
        ),
        migrations.RemoveField(
            model_name='publicblogasnewsletter',
            name='default_introduction',
        ),
        migrations.RemoveField(
            model_name='publicblogasnewsletter',
            name='default_title',
        ),
        migrations.RemoveField(
            model_name='publicblogasnewsletter',
            name='despedida',
        ),
        migrations.RemoveField(
            model_name='publicblogasnewsletter',
            name='introduction',
        ),
        migrations.RemoveField(
            model_name='publicblogasnewsletter',
            name='use_default_despedida',
        ),
        migrations.RemoveField(
            model_name='publicblogasnewsletter',
            name='use_default_introduction',
        ),
        migrations.RemoveField(
            model_name='publicblogasnewsletter',
            name='use_default_title',
        ),
    ]
