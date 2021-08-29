import unittest
from Tests.home.login_tests import LoginTests
from Tests.Practice.practice_test import PracticeElementTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PracticeElementTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1,tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)