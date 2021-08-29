import time

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import Utilities.customlogger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_link = "Sign Up or Log In"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
            self.clickLoginLink()
            self.clearFields()
            self.enterEmail(email)
            self.enterPassword(password)
            time.sleep(3)
            self.clickLoginButton()


    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//body/div[@id='page']/div[@id='header5']/div[1]/nav[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/img[1]",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid. Please try a')]",
                                       locatorType="xpath")
        return result
    # failure scenario

    def verifyLoginTitle(self):
        return self.verifyPageTitle('My Courses')

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def get_title(self):
        a = self.getTitle()
        print("title is ",a)