# Generated by Django 4.1.7 on 2023-02-27 13:56

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
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
                    "uuid",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("secret_code", models.CharField(max_length=4)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("in_progress", "in_progress"),
                            ("won", "won"),
                            ("lost", "lost"),
                        ],
                        default="in_progress",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="game",
            constraint=models.CheckConstraint(
                check=models.Q(("secret_code__regex", "^[RBGYWO]{4}$")),
                name="secret_code_regex",
            ),
        ),
    ]
