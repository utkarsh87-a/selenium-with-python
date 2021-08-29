import time

import Utilities.customlogger as cl
import logging
from base.basepage import BasePage

class EnrollmentPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    _first_login ="//div[contains(text(),'Sign Up or Log In')]"
    _signup_ = "//a[contains(text(),'Sign Up')]"
    _firstname_="name"
    _lastname_="last_name"
    _email_="email"
    _password_="password"
    _confirm_password_="password_confirmation"
    _submit_up_="//input[@type='submit']"
    _my_courses = "//h1[contains(text(),'My Courses')]"
    _dropdown = "//a/span[@class='caret']"
    _logout = "//a[contains(text(),'Logout')]"

    def login_sign(self):
        self.elementClick(locator=self._first_login,locatorType='xpath')
        time.sleep(7)
        self.elementClick(locator=self._signup_,locatorType='xpath')

    def registar_details(self,fname,lname,email,password,confirmpass):
        self.sendKeys(data=fname,locator=self._firstname_)
        self.sendKeys(data=lname,locator=self._lastname_)
        self.sendKeys(data=email,locator=self._email_)
        self.sendKeys(data=password,locator=self._password_)
        self.sendKeys(data=confirmpass,locator=self._confirm_password_)
        time.sleep(7)
        self.elementClick(locator=self._submit_up_,locatorType='xpath')
        time.sleep(7)

    def verifytext(self):
        return self.isElementPresent(locator=self._my_courses,locatorType='xpath')

    def logout(self):
        self.elementClick(locator=self._dropdown,locatorType='xpath')
        time.sleep(4)
        self.elementClick(locator=self._logout,locatorType='xpath')
        time.sleep(6)

    def verifyhometitel(self):
        return self.verifyPageTitle(titleToVerify="Home Page")





