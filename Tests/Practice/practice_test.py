import time

from pages.Practice.practise_element import PractiseElementPage
from pages.home.login_page import LoginPage

import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PracticeElementTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):

        self.pe = PractiseElementPage(self.driver)

    @pytest.mark.run(order=1)
    def test_practiseElement(self):
        self.pe.clickpractice()
        time.sleep(6)
        self.pe.click_elepractice()
        time.sleep(8)
        result = self.pe.verify_title()
        assert result == True
