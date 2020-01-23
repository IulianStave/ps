import unittest

from selenium import webdriver
from src.locators import Locators
from src.pages import HomePage, SearchResultsPage
from .testData import testData

# from src.pages import HomePage, SearchResultsPage

# Base Class for the tests
class Test_Search_Base(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        # Setting up how we want Chrome to run
        inst.driver = webdriver.Chrome()
        # browser should be loaded in maximized window
        inst.driver.maximize_window()

    @classmethod
    def tearDown(inst):
        # To do the cleanup after test has executed.
        # inst.driver.close()
        inst.driver.quit()

# Test class containing methods corresponding to testcases.
class Test_Home(Test_Search_Base):
    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()

    def test_home_page_loaded_successfully(self):
        # instantiate an object of HomePage class. 
        # When the constructor of HomePage class is called
        # it opens up the browser and navigates to Home Page 
        # of the site under test
        self.homePage = HomePage(self.driver)
        # assert if the title of Home Page contains the appropriate title
        self.assertIn(testData.HOME_PAGE_TITLE, self.homePage.driver.title)
    
    def test_user_should_be_able_to_search(self):
        self.homePage = HomePage(self.driver)
        # search for the search term on Home Page. The search term would be picked from
        # test data file
        self.homePage.search()
        # instantiate an object of SearchResultsPage class passing in the driver as parameter.
        # this will allow the newly created object to have access to the browser and perform
        # operations further.
        self.searchResultsPage = SearchResultsPage(self.homePage.driver)
        # assert if the search term is present in the title of the Amazon's Search Results Page
        self.assertIn(testData.SEARCH_TERM, self.searchResultsPage.driver.title)
        # assert that the search term indeed return some results.
        self.assertNotIn(testData.NO_RESULTS_TEXT, self.searchResultsPage.driver.page_source)
    


class Test_Search(Test_Search_Base):
    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()

    def test_search_results(self):
        # instantiate an object of HomePage class. Remember when the constructor of HomePage class is called
        # it opens up the browser and navigates to Home Page of the site under test.
        self.homePage = HomePage(self.driver)
        # assert if the title of Home Page contains Amazon.in
        self.assertIn(testData.HOME_PAGE_TITLE, self.homePage.driver.title)