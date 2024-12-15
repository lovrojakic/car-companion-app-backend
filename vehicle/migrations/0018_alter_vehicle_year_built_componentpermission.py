# Generated by Django 5.1.3 on 2024-11-30 17:00

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0017_merge_20241123_1906"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="year_built",
            field=models.IntegerField(
                error_messages={
                    "invalid": "Enter a valid year.",
                    "null": "Year built is required.",
                },
                help_text="Year the vehicle was manufactured",
                validators=[
                    django.core.validators.MinValueValidator(
                        1886, message="Year must be 1886 or later."
                    ),
                    django.core.validators.MaxValueValidator(
                        2025, message="Year cannot be in the future."
                    ),
                ],
                verbose_name="Year Built",
            ),
        ),
        migrations.CreateModel(
            name="ComponentPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "permission_type",
                    models.CharField(
                        choices=[("read", "Read Only"), ("write", "Read & Write")],
                        max_length=5,
                        verbose_name="permission type",
                    ),
                ),
                (
                    "valid_until",
                    models.DateTimeField(
                        blank=True,
                        help_text="If set, the permission will expire at this time",
                        null=True,
                        verbose_name="valid until",
                    ),
                ),
                (
                    "component",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="access_permissions",
                        to="vehicle.vehiclecomponent",
                        verbose_name="component",
                    ),
                ),
                (
                    "granted_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="granted_permissions",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="granted by",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="component_permissions",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "Component Permission",
                "verbose_name_plural": "Component Permissions",
                "ordering": ["-created"],
                "indexes": [
                    models.Index(
                        fields=["component", "user"],
                        name="vehicle_com_compone_ce76eb_idx",
                    ),
                    models.Index(
                        fields=["valid_until"], name="vehicle_com_valid_u_5ce588_idx"
                    ),
                ],
                "unique_together": {("component", "user")},
            },
        ),
    ]