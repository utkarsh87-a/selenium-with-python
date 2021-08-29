import time

import Utilities.customlogger as cl
import logging
from base.basepage import BasePage

class CoursesLinkPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _first_login ="//div[contains(text(),'Sign Up or Log In')]"
    _email_ = "email"
    _password_="password"
    _submit_up_="//input[@value='Login']"
    list_menu = "//div[@data-component='list']/ul/li"
    list_iter = "//div[@data-component='list']/ul/li['+str(i)+']"

    def login_page(self,email,password):
        self.elementClick(locator=self._first_login,locatorType='xpath')
        time.sleep(6)
        self.sendKeys(data=email,locator=self._email_,locatorType='id')
        self.sendKeys(data=password,locator=self._password_,locatorType='id')
        self.elementClick(locator=self._submit_up_,locatorType='xpath')
        time.sleep(6)


    def handlelink(self):
        ele = self.getElementList(locator=self.list_menu,locatorType='xpath')
        self.log.info("total number of links is" +str(len(ele)))
        for i in range(0,len(ele)):

            ele1 = self.getElementList(locator=self.list_iter,locatorType='xpath')
        for x in ele1:
            print(self.getText(element=x))



