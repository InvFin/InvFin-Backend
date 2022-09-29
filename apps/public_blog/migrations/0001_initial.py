# Generated by Django 3.2.15 on 2022-09-29 15:29

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailPublicBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('opened', models.BooleanField(default=False)),
                ('date_opened', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Email from public blog',
                'db_table': 'emails_public_blog',
            },
        ),
        migrations.CreateModel(
            name='FollowingHistorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_following', models.BooleanField(default=False)),
                ('stop_following', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Users following historial',
                'db_table': 'writter_followers_historial',
            },
        ),
        migrations.CreateModel(
            name='NewsletterFollowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Base de seguidores del blog',
                'db_table': 'writter_followers_newsletters',
            },
        ),
        migrations.CreateModel(
            name='PublicBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_votes', models.IntegerField(default=0)),
                ('total_views', models.PositiveIntegerField(default=0)),
                ('times_shared', models.PositiveIntegerField(default=0)),
                ('resume', models.TextField(default='')),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Publicado'), (2, 'Borrador'), (3, 'Programado'), (4, 'Necesita revisión')], null=True)),
                ('thumbnail', models.ImageField(blank=True, height_field='image_height', null=True, upload_to='', verbose_name='image', width_field='image_width')),
                ('non_thumbnail_url', models.CharField(blank=True, max_length=500, null=True)),
                ('in_text_image', models.BooleanField(default=False)),
                ('send_as_newsletter', models.BooleanField(default=False)),
                ('content', ckeditor.fields.RichTextField()),
                ('published_correctly', models.BooleanField(default=False)),
                ('date_to_publish', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Public blog post',
                'db_table': 'blog_post',
                'ordering': ['total_views'],
            },
        ),
        migrations.CreateModel(
            name='PublicBlogAsNewsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor.fields.RichTextField()),
                ('sent', models.BooleanField(default=False)),
                ('date_to_send', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PublicBlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': "Blog's comment",
                'db_table': 'blog_comments',
            },
        ),
        migrations.CreateModel(
            name='WritterProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host_name', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('long_description', ckeditor.fields.RichTextField(default='')),
                ('facebook', models.CharField(blank=True, max_length=500, null=True)),
                ('twitter', models.CharField(blank=True, max_length=500, null=True)),
                ('insta', models.CharField(blank=True, max_length=500, null=True)),
                ('youtube', models.CharField(blank=True, max_length=500, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=500, null=True)),
                ('tiktok', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'User writter profile',
                'db_table': 'writter_profile',
            },
        ),
    ]
