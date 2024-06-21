from io import StringIO

from django.core.management import call_command
from django.test import TestCase


class CSUTestCase(TestCase):
    def test_my_csu_command(self) -> None:
        out = StringIO()
        call_command("csu", stdout=out)
        output = out.getvalue().strip()
        self.assertEqual(output, "Superuser created successfully")
