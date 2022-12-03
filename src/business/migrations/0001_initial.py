# Generated by Django 3.2.15 on 2022-11-04 22:43

import src.business.models
import src.general.mixins
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("currencies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("stripe_id", models.CharField(blank=True, max_length=500, null=True)),
                ("for_testing", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Customer",
                "verbose_name_plural": "Customers",
                "db_table": "business_customers",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("stripe_id", models.CharField(blank=True, max_length=500, null=True)),
                ("for_testing", models.BooleanField(default=False)),
                ("title", models.CharField(max_length=300)),
                ("slug", models.SlugField(blank=True, max_length=300, null=True)),
                ("description", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("image", models.CharField(blank=True, max_length=500, null=True)),
                ("video", models.CharField(blank=True, max_length=500, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                ("visits", models.IntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "db_table": "business_products",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name="ProductComment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("content", models.TextField()),
                ("rating", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products comments",
                "db_table": "business_products_comments",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name="ProductComplementary",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("stripe_id", models.CharField(blank=True, max_length=500, null=True)),
                ("for_testing", models.BooleanField(default=False)),
                ("image", models.CharField(blank=True, max_length=500, null=True)),
                ("video", models.CharField(blank=True, max_length=500, null=True)),
                ("title", models.CharField(blank=True, max_length=300)),
                ("slug", models.SlugField(blank=True, max_length=300, null=True)),
                ("price", models.FloatField(blank=True, null=True)),
                (
                    "payment_type",
                    models.CharField(
                        blank=True, choices=[("subscription", "Subscripción"), ("payment", "Un pago")], max_length=300
                    ),
                ),
                ("description", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "subscription_period",
                    models.CharField(
                        blank=True,
                        choices=[("day", "Daily"), ("week", "Weekly"), ("month", "Montly"), ("year", "Yearly")],
                        max_length=300,
                    ),
                ),
                ("subscription_interval", models.IntegerField(blank=True, default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                ("extras", models.JSONField(default=src.business.models.default_dict)),
                (
                    "purchase_result",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("add_credits", "add_credits"),
                            ("share_excel", "share_excel"),
                            ("ilimited_credits", "ilimited_credits"),
                            ("random_prize", "random_prize"),
                            ("random_credits", "random_credits"),
                        ],
                        max_length=300,
                    ),
                ),
                ("product_result", models.CharField(blank=True, default="", max_length=300)),
            ],
            options={
                "verbose_name": "Product complementary",
                "verbose_name_plural": "Products complementary",
                "db_table": "business_products_complementary",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name="ProductComplementaryPaymentLink",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("stripe_id", models.CharField(blank=True, max_length=500, null=True)),
                ("for_testing", models.BooleanField(default=False)),
                ("title", models.CharField(blank=True, max_length=500, null=True)),
                ("link", models.CharField(blank=True, max_length=500, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                ("for_website", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Product complementary payment link",
                "verbose_name_plural": "Products complementary payment link",
                "db_table": "business_products_complementary_payment_link",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name="ProductDiscount",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("stripe_id", models.CharField(blank=True, max_length=500, null=True)),
                ("for_testing", models.BooleanField(default=False)),
                ("start_date", models.DateTimeField(blank=True, null=True)),
                ("end_date", models.DateTimeField(blank=True, null=True)),
                ("discount", models.FloatField(blank=True, null=True)),
                ("is_percentage", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Product discount",
                "verbose_name_plural": "Products discounts",
                "db_table": "business_products_discounts",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name="TransactionHistorial",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "payment_method",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("credits", "Credits"),
                            ("wire", "Wire"),
                            ("paypal", "Paypal"),
                            ("other", "Others"),
                            ("card", "Card"),
                        ],
                        max_length=300,
                    ),
                ),
                ("final_amount", models.FloatField(blank=True, null=True)),
                ("stripe_response", models.JSONField(blank=True, default=dict, null=True)),
                (
                    "currency",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="currencies.currency"
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="business.customer"),
                ),
                (
                    "discount",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="business.productdiscount",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="business.product"),
                ),
                (
                    "product_comment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="business.productcomment",
                    ),
                ),
                (
                    "product_complementary",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="business.productcomplementary",
                    ),
                ),
            ],
            options={
                "verbose_name": "Transaction",
                "verbose_name_plural": "Transactions",
                "db_table": "business_transactions",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name="StripeWebhookResponse",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("stripe_id", models.CharField(blank=True, max_length=500, null=True)),
                ("for_testing", models.BooleanField(default=False)),
                ("full_response", models.JSONField(default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="business.customer"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="business.product"),
                ),
                (
                    "product_complementary",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="business.productcomplementary",
                    ),
                ),
            ],
            options={
                "verbose_name": "Stripe webhook response",
                "verbose_name_plural": "Stripe webhook responses",
                "db_table": "business_stripe_webhook_responses",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
        migrations.CreateModel(
            name="ProductSubscriber",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscribers",
                        to="business.product",
                    ),
                ),
                (
                    "product_complementary",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="complementary_subs",
                        to="business.productcomplementary",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product subscriber",
                "verbose_name_plural": "Products subscribers",
                "db_table": "business_products_subscribers",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
    ]
