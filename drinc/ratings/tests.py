from datetime import date

from django.test import TestCase

from .models import Menu


class MenuModelTests(TestCase):
    def test_is_current_ends_today(self):
        """
        is_current() should returns True for menu that have the closing date set to today.
        """
        current_menu = Menu(name="Test Menu", dateL=date(2024, 5, 1), dateC=date.today())
        self.assertIs(current_menu.is_current(), True)
