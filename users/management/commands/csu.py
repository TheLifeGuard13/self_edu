import typing

from django.conf import settings
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Create superuser"

    def handle(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        user, created = User.objects.get_or_create(
            email=settings.SUPERUSER_EMAIL,
            first_name=settings.SUPERUSER_FIRST_NAME,
            last_name=settings.SUPERUSER_LAST_NAME,
            is_staff=True,
            is_superuser=True,
        )

        if created:
            user.set_password(settings.SUPERUSER_PASSWORD)
            user.save()
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))
