# Generated by Django 4.2.7 on 2023-12-31 20:41

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import src.general.mixins


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("currencies", "0004_alter_exchangerate_base_alter_exchangerate_target"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("cartera", "0015_alter_investment_movement"),
    ]

    operations = [
        migrations.AddField(
            model_name="income",
            name="to_substract",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="WireTransfer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=500, verbose_name="Nombre")),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=3,
                        default=Decimal("0"),
                        max_digits=100,
                        verbose_name="Monto",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, default="", verbose_name="Descripción"),
                ),
                (
                    "comment",
                    models.TextField(blank=True, default="", verbose_name="Comentario"),
                ),
                ("date", models.DateField(blank=True, verbose_name="Fecha del movimiento")),
                ("transaction_file_id", models.PositiveIntegerField(null=True)),
                ("is_recurrent", models.BooleanField(blank=True, default=False)),
                ("read", models.BooleanField(blank=True, default=False)),
                (
                    "amount_converted",
                    models.DecimalField(
                        blank=True, decimal_places=3, default=Decimal("0"), max_digits=100
                    ),
                ),
                ("sender_id", models.PositiveIntegerField(null=True)),
                ("receiver_id", models.PositiveIntegerField(null=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="cartera.cashflowmovementcategory",
                    ),
                ),
                (
                    "currency",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="currencies.currency",
                    ),
                ),
                (
                    "net_worth",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="net_worth_wire_trasnfers",
                        to="cartera.networth",
                    ),
                ),
                (
                    "receiver_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="receiver",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "sender_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="sender",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "transaction_file_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="wire_trasnfers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "patrimoine_wire_trasnfers",
            },
            bases=(models.Model, src.general.mixins.BaseToAllMixin),
        ),
    ]
