# Generated by Django 3.2.15 on 2022-10-17 21:28

import apps.general.mixins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("public_blog", "0006_auto_20221017_2321"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailPublicBlog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("date_sent", models.DateTimeField(auto_now_add=True)),
                ("opened", models.BooleanField(default=False)),
                ("date_opened", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "email_related",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="email_related",
                        to="public_blog.publicblogasnewsletter",
                    ),
                ),
                (
                    "sent_to",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "verbose_name": "Email from public blog",
                "db_table": "public_blog_newsletters_emails",
            },
            bases=(models.Model, apps.general.mixins.BaseToAllMixin),
        ),
    ]
