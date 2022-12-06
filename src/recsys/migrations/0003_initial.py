# Generated by Django 3.2.15 on 2022-11-04 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recsys', '0002_initial'),
        ('preguntas_respuestas', '0002_initial'),
        ('business', '0002_initial'),
        ('empresas', '0001_initial'),
        ('public_blog', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promotions', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertermrecommended',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userquestionrecommended',
            name='model_recommended',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='preguntas_respuestas.question'),
        ),
        migrations.AddField(
            model_name='userquestionrecommended',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userpublicblogrecommended',
            name='model_recommended',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='public_blog.publicblog'),
        ),
        migrations.AddField(
            model_name='userpublicblogrecommended',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userpromotionrecommended',
            name='model_recommended',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='promotions.promotion'),
        ),
        migrations.AddField(
            model_name='userpromotionrecommended',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userproductcomplementaryrecommended',
            name='model_recommended',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.productcomplementary'),
        ),
        migrations.AddField(
            model_name='userproductcomplementaryrecommended',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercompanyrecommended',
            name='model_recommended',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresas.company'),
        ),
        migrations.AddField(
            model_name='usercompanyrecommended',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]