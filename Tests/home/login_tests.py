import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Utilities.test_status import TestStatus
from pages.home.login_page import LoginPage
import unittest
import pytest
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        print(result1)
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyLoginSuccessful()
        print(result2)
        self.lp.get_title()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        self.lp.get_title()
        result = self.lp.verifyLoginFailed()
        print(result)
        assert result == True


