import time

import Utilities.customlogger as cl
import logging
from base.basepage import BasePage

class PractiseElementPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _hover_ele = "//li[@id='menu-item-1450']/a/span[@class='menu-text']"
    _ele_practise = "//span[contains(text(),'Elements Practice')]"
    _login_ele="//a[contains(text(),'Sign Up')]"

    def clickpractice(self):
        self.gethover(locator=self._hover_ele,locatorType='xpath')

    def click_elepractice(self):
        self.gethoverandclick(locator=self._ele_practise,locatorType='xpath')


    def verify_title(self):
        return self.verifyPageTitle(titleToVerify="Let's Kode It – Anyone Can Code")
    
    