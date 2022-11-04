# Generated by Django 3.2.15 on 2022-11-04 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classifications', '0001_initial'),
        ('preguntas_respuestas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classifications.category'),
        ),
        migrations.AddField(
            model_name='question',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='user_downvote_question', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, to='classifications.Tag'),
        ),
        migrations.AddField(
            model_name='question',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='user_upvote_question', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quesitoncomment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quesitoncomment',
            name='content_related',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_related', to='preguntas_respuestas.question'),
        ),
        migrations.AddField(
            model_name='answercomment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answercomment',
            name='content_related',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_related', to='preguntas_respuestas.answer'),
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers_apported', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='user_downvote_answer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question_related',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='preguntas_respuestas.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='user_upvote_answer', to=settings.AUTH_USER_MODEL),
        ),
    ]
