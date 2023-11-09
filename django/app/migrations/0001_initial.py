# Generated by Django 4.2.7 on 2023-11-09 18:30

import app.models.user
import django.utils.timezone
import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "password",
                    models.CharField(max_length=128, verbose_name="password"),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        default=django.utils.timezone.now, null=True
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        default=django.utils.timezone.now, null=True
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="The user's primary email address.",
                        max_length=255,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        help_text="The user's primary phone number.",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True,
                        help_text="The user's first name.",
                        max_length=250,
                        null=True,
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        help_text="The user's last name.",
                        max_length=250,
                        null=True,
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="date joined",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "db_table": "user",
                "abstract": False,
            },
            managers=[
                ("objects", app.models.user.UserManager()),
            ],
        ),
    ]