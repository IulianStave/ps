import unittest
# from SearchTextTestCases import SearchText
# from HomeTextTestCases import HomePageTest
from src.testBase import Test_Search, Test_Home

# get all tests from SearchText and HomePageTest class
home_page_test = unittest.TestLoader().loadTestsFromTestCase(Test_Home)
search_results_test = unittest.TestLoader().loadTestsFromTestCase(Test_Search)

# print("\n\n", ho_page_test)
# home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

#  @classmethod
#     def my_tests(cls):
#         return unittest.defaultTestLoader.getTestCaseNames(cls)
test_suite = unittest.TestSuite()
# print("\n\n", HomePageTest.my_tests())
# for name in HomePageTest.my_tests():
#     print(name)
#     # testcase = HomePageTest()
#     # print(testcase)
#     # test_suite.addTest(testcase)
test_suite.addTest(home_page_test)
test_suite.addTest(search_results_test)

# test_suite.addTest(ho_page_test)
# create a test suite combining search_text and home_page_test
# test_suite = unittest.TestSuite([home_page_test, search_text])

# run the suite
# unittest.TextTestRunner(verbosity=2).run(test_suite)
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(test_suite)
