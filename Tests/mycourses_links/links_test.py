import time

from pages.mycourses_links.mycourses_links import CoursesLinkPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LinksTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.link = CoursesLinkPage(self.driver)

    @pytest.mark.run(order=1)
    def test_links(self):
        self.link.login_page(email='test87@gmail.com',password='abcabc')
        self.link.handlelink()