# Generated by Django 3.2.15 on 2022-10-17 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas_respuestas', '0004_rename_extra_data_question_checkings'),
    ]

    operations = [
        migrations.AddField(
            model_name='answercomment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='quesitoncomment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='quesitoncomment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]