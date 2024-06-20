# Generated by Django 5.0.6 on 2024-06-14 18:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0005_subscription"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="answer",
            options={"verbose_name": "ответ", "verbose_name_plural": "ответы"},
        ),
        migrations.RemoveField(
            model_name="answer",
            name="is_correct",
        ),
        migrations.RemoveField(
            model_name="answer",
            name="question",
        ),
        migrations.AddField(
            model_name="question",
            name="answer",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="correct_answer",
                to="application.answer",
                verbose_name="Правильный ответ",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="choices",
            field=models.ManyToManyField(related_name="choices", to="application.answer"),
        ),
        migrations.AlterField(
            model_name="answer",
            name="answer",
            field=models.CharField(max_length=50, verbose_name="Ответ"),
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "material",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="application.material", verbose_name="Материал"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец",
                    ),
                ),
                ("question", models.ManyToManyField(to="application.question", verbose_name="Вопросы")),
            ],
            options={
                "verbose_name": "тест",
                "verbose_name_plural": "тесты",
            },
        ),
    ]
