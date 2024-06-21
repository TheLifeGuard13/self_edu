import typing

from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    """Проверяет является ли пользователь staff."""

    def has_permission(self, request: typing.Any, view: typing.Any) -> bool:
        if request.user.is_staff:
            return True
        return False
