# Generated by Django 5.0.6 on 2024-06-13 19:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0004_alter_answer_options_alter_question_options_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscription",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "chapter",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chapter_for_subscription",
                        to="application.chapter",
                        verbose_name="Раздел",
                    ),
                ),
                (
                    "subscriber",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Подписчик",
                    ),
                ),
            ],
            options={
                "verbose_name": "подписка",
                "verbose_name_plural": "подписки",
            },
        ),
    ]
