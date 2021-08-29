from Utilities.test_status import TestStatus
from pages.Switchto_page.switchto import SwitchToPage
import unittest
import pytest
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SwitchtoTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sp = SwitchToPage(self.driver)

    @pytest.mark.run(order=1)
    def test_switchpage(self):
        self.sp.switchtonew()