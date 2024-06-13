from django.conf import settings
from django.db import models

from config.settings import NULLABLE


class Chapter(models.Model):
    """
    Модель Раздела
    """

    name = models.CharField(max_length=150, verbose_name="Название")
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


class Material(models.Model):
    """
    Модель Материалов
    """

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    preview = models.ImageField(upload_to="material/", **NULLABLE, verbose_name="Превью")
    url = models.CharField(max_length=150, **NULLABLE, verbose_name="Ссылка")
    course = models.ForeignKey(Chapter, on_delete=models.SET, **NULLABLE, verbose_name="Курс")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "материал"
        verbose_name_plural = "материалы"


# class Test(models.Model):
#     """
#     Модель Теста
#     """
#

#     material = models.ForeignKey(Material, on_delete=models.SET, **NULLABLE, verbose_name="Курс",
#                                related_name="material_for_test")
#     subscriber = models.ForeignKey(
#         settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Подписчик")
#
#     def __str__(self) -> str:
#         return f"{self.course}, {self.subscriber}"
#
#     class Meta:
#         verbose_name = "подписка"
#         verbose_name_plural = "подписки"