from django.conf import settings
from django.db import models

from config.settings import NULLABLE


class Chapter(models.Model):
    """
    Модель Раздела
    """

    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    preview = models.ImageField(upload_to="chapter/", **NULLABLE, verbose_name="Превью")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "раздел"
        verbose_name_plural = "разделы"
        ordering = ['id']


class Material(models.Model):
    """
    Модель Материала
    """

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    preview = models.ImageField(upload_to="material/", **NULLABLE, verbose_name="Превью")
    url = models.CharField(max_length=150, **NULLABLE, verbose_name="Ссылка")
    course = models.ForeignKey(Chapter, on_delete=models.CASCADE, **NULLABLE, verbose_name="Раздел")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "материал"
        verbose_name_plural = "материалы"
        ordering = ['id']


class Subscription(models.Model):
    """
    Модель Подписки
    """

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, **NULLABLE, verbose_name="Раздел",
                                related_name="chapter_for_subscription")
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Подписчик")

    def __str__(self) -> str:
        return f"{self.chapter}, {self.subscriber}"

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"
