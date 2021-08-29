import time

import Utilities.customlogger as cl
import logging
from base.basepage import BasePage

class SwitchToPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _newpage_locator = "//body/div[@id='page']/div[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]/img[1]"

    def switchtonew(self):
        element = self.windowhandle()
        time.sleep(6)
        self.openwindowinsametab(locator=self._newpage_locator,locatorType='xpath')
        time.sleep(7)
        ele = self.windowhandles()
        self.switchtonew(id=ele[1])
        time.sleep(6)
        self.switchtonew(id=element)

