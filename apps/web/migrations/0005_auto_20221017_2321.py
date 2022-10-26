# Generated by Django 3.2.15 on 2022-10-17 21:21

from django.db import migrations, models


# def populate_categories_users(apps, schema):
#     for key, value in CONTENT_PURPOSES:
#         WebsiteEmailsType = apps.get_model("web", "WebsiteEmailsType")
#         UsersCategory = apps.get_model("web", "UsersCategory")
#         web_email_type = WebsiteEmailsType.objects.create(name=value, slug=key)
#         cat = UsersCategory.objects.create(name=value, slug=key)
#         cat.email_type_related.add(web_email_type)

class Migration(migrations.Migration):
    dependencies = [
        ("web", "0004_auto_20221016_0939"),
    ]

    operations = [
        migrations.AddField(
            model_name="websiteemail",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="websiteemail",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="websiteemailtrack",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="websiteemailtrack",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
