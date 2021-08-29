import time

from pages.Practice.practise_element import PractiseElementPage
from pages.Enrollment.new_enrollmentpage import EnrollmentPage


import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class EnrollmentTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):

        self.ep = EnrollmentPage(self.driver)

    @pytest.mark.run(order=1)
    def test_enrollment(self):
        self.ep.login_sign()
        self.ep.registar_details(fname="utkarsh1",lname="dubey1",email="test88@email.com",password="abcabc",confirmpass="abcabc")
        result1 = self.ep.verifytext()
        assert result1==True
        time.sleep(7)
        self.ep.logout()
        result2 = self.ep.verifyhometitel()
        assert result2==True
