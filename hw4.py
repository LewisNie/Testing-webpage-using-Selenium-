from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import unittest

class Testhw4(unittest.TestCase):
# Create a new instance of the Firefox driver
    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_title_unique(self):
# If you download the chrome driver and put it in your path, then do:
# driver = webdriver.Chrome()

# go to the google home page
        self.driver.get("http://www.oaklandairport.com")

# the page is ajaxy so the title is originally this:
        title_homepage=self.driver.title
        print title_homepage
        self.driver.get("http://www.oaklandairport.com/news.shtml")
        title_news=self.driver.title
        print title_news
        self.driver.get("http://www.oaklandairport.com/airport_development.shtml")
        title_develop=self.driver.title
        print title_develop
        self.driver.get("http://www.oaklandairport.com/noise/index.shtml")
        title_noise=self.driver.title
        print title_noise
        self.driver.get("http://www.oaklandairport.com/air_cargo.shtml")
        title_cargo=self.driver.title
        print title_cargo
        list_title=[title_homepage,title_news,title_develop,title_noise,title_cargo]
        
    def test_404_page(self):
        self.driver.get("http://csueastbay.edu/macs")
        found=self.driver.title
        print found
        self.assertTrue('Sorry, the page cannot be found'==found)
        
    def test_single_word(self):
        self.driver.get("http://www.oaklandairport.com/")
        inputElement = self.driver.find_element_by_name("search1")
        inputElement.send_keys("oakland")
        inputElement.submit()
 
        WebDriverWait(self.driver, 10).until(EC.title_contains("oakland"))
        self.assertTrue(EC.title_is("oakland"))
        print self.driver.title
        
    def test_non_appear_word(self):
        self.driver.get("http://www.oaklandairport.com/")
        inputElement = self.driver.find_element_by_name("search1")
        inputElement.send_keys("ln")
        inputElement.submit()
 
        WebDriverWait(self.driver, 10).until(EC.title_contains("ln"))
        self.assertTrue(EC.title_is("ln"))
        print self.driver.title
        
    def test_multi_word(self):
        self.driver.get("http://www.oaklandairport.com/")
        inputElement = self.driver.find_element_by_name("search1")
        inputElement.send_keys("ln")
        inputElement.submit()
 
        WebDriverWait(self.driver, 10).until(EC.title_contains("ln "))
        self.assertTrue(EC.title_is("ln"))
        print self.driver.title
        
    def tearDown(self):
        self.driver.quit()
# find the element that's name attribute is q (the google search box)
#inputElement = driver.find_element_by_name("q")

# type in the search
#inputElement.send_keys("cheese!")

# submit the form (although google automatically searches now without submitting)
#inputElement.submit()

#try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
   # WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    #print driver.title

#finally:
#    driver.quit()
suite = unittest.TestLoader().loadTestsFromTestCase(Testhw4)
unittest.TextTestRunner(verbosity=2).run(suite)
