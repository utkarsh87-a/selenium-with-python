import time

import Utilities.customlogger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _search_box = "//input[@id='search']"
    _course = "//h4[contains(text(),'JavaScript for beginners')]"
    _all_courses = "//a[contains(text(),'ALL COURSES')]"
    _enroll_button = "//body/div[@id='page']/div[@id='header19']/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]"
    _cc_num = "//div[@id='card-number']"
    _cc_exp = "//div[@id='card-expiry']"
    _cc_cvv = "//div[@id='card-cvc']"
    _submit_enroll = "//body/div[@id='page']/div[@id='header19']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/button[1]"
    _enroll_error_message = "//span[contains(text(),'Your card number is incomplete.')]"

    ############################
    ### Element Interactions ###
    ############################
    def allcourse(self):
        self.elementClick(locator=self._all_courses,locatorType='xpath')

    def enterCourseName(self,name):
        self.sendKeys(name,locator=self._search_box,locatorType='xpath')
        print()

    def selectCourseToEnroll(self):
        self.elementClick(locator=self._course,locatorType='xpath')
        print()

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button,locatorType='xpath')

    def enterCardNum(self, num):
        self.sendKeys(num,locator=self._cc_num,locatorType='xpath')

    def enterCardExp(self, exp):
        self.sendKeys(exp,locator=self._cc_exp,locatorType='xpath')


    def enterCardCVV(self, cvv):
        self.sendKeys(cvv,locator=self._cc_cvv,locatorType='xpath')


    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll,locatorType='xpath')


    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        time.sleep(6)
        self.enterCardExp(exp)
        time.sleep(6)
        self.enterCardCVV(cvv)
        time.sleep(6)


    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction='down')
        self.enterCreditCardInformation(num,exp,cvv)
        self.clickEnrollSubmitButton()
        print()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(locator=self._enroll_error_message,locatorType='xpath')
        result = self.isElementDisplayed(element=messageElement)
        return result