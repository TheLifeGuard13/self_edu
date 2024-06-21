import typing

from rest_framework.exceptions import ValidationError


class UrlValidator:
    """Валидирует поле url модели материалов"""

    def __init__(self, field: typing.Any) -> None:
        self.field = field

    def __call__(self, value: typing.Any) -> None:
        temp_value = dict(value).get(self.field)
        allowed_server = "@youtube.com"
        if temp_value is not None and allowed_server not in temp_value:
            raise ValidationError("Ссылка должна быть только с сервиса Youtube или отсутствовать")
