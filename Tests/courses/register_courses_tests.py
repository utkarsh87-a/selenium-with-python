import time

from pages.courses.register_courses_pages import RegisterCoursesPage
from pages.home.login_page import LoginPage
from Utilities.test_status  import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.lp.login("test@email.com", "abcabc")
        time.sleep(6)
        self.courses.allcourse()
        time.sleep(6)
        self.courses.enterCourseName("JavaScript")
        time.sleep(6)
        self.courses.selectCourseToEnroll()
        time.sleep(6)
        self.courses.clickOnEnrollButton()
        time.sleep(7)
        #self.courses.enrollCourse(num="10", exp="1220", cvv="10")
        self.courses.clickEnrollSubmitButton()
        time.sleep(6)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")