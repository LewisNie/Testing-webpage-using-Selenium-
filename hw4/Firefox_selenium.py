from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
import unittest

class Testhw4(unittest.TestCase):
# Create a new instance of the Firefox driver
    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_title_unique(self):
# go to the Oaklandairport home page
        self.driver.get("http://www.oaklandairport.com")
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
        a=0
        for i in range(0,len(list_title)):
                for j in range(i+1, len(list_title)):
                    if(list_title[i]==list_title[j]):
                        a=1
        self.assertTrue(a==0)

   
    def test_404_page(self):
        self.driver.get("http://csueastbay.edu/macs")
        found=self.driver.title
        self.assertIn('404',self.driver.page_source)
        
    def test_single_word(self):
        self.driver.get("http://www.oaklandairport.com/")
        inputElement = self.driver.find_element_by_name("search1")
        inputElement.clear()
        inputElement.send_keys("oakland")
        
 #       inputElement.submit()
        inputGo=self.driver.find_element_by_name("Submit")
        inputGo.click()
        Link1=self.driver.find_element_by_link_text("Untitled Document")
        Link1.click()
        self.assertIn('Oakland',self.driver.page_source)
        self.driver.back()
        Link2=self.driver.find_element_by_link_text("Oakland International Airport: Air Show 2002")
        Link2.click()
        self.assertIn('Oakland',self.driver.page_source)
        self.driver.back()
        Link3=self.driver.find_element_by_link_text("Oakland International Airport: Airport Development")
        Link3.click()
        self.assertIn('Oakland',self.driver.page_source)
        """try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("oakland"))
            self.assertTrue(EC.title_is("oakland"))
            print self.driver.title
        except NoSuchElementException:
            fail("can't find element with id=location")"""
    def test_non_appear_word(self):
        self.driver.get("http://www.oaklandairport.com/")
        inputElement = self.driver.find_element_by_name("search1")
        inputElement.clear()
        inputElement.send_keys("ln")
 #       inputElement.submit()
        inputGo=self.driver.find_element_by_name("Submit")
        inputGo.click()
 
        """try: 
            WebDriverWait(self.driver, 10).until(EC.title_contains("ln"))
            self.assertTrue(EC.title_is("ln"))
            print self.driver.title
        except NoSuchElementException:
             fail("can't find element with id=location")"""
             
    def test_multi_word(self):
        self.driver.get("http://www.oaklandairport.com/")
        inputElement = self.driver.find_element_by_name("search1")
        inputElement.clear()
        inputElement.send_keys("San Jose")
        
 #       inputElement.submit()
        inputGo=self.driver.find_element_by_name("Submit")
        inputGo.click()

        Link1=self.driver.find_element_by_link_text("Oakland International Airport: Amtrak")
        Link1.click()
        self.assertIn('San Jose',self.driver.page_source)
        self.driver.back()
        Link2=self.driver.find_element_by_link_text("Oakland International Airport: Education")
        Link2.click()
        self.assertIn('San',self.driver.page_source)
        self.driver.back()
        Link3=self.driver.find_element_by_link_text("Oakland International Airport: Water and Wetlands")
        Link3.click()
        self.assertIn('San',self.driver.page_source)
        """try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("ln "))
            self.assertTrue(EC.title_is("hello world"))
            print self.driver.title
        except NoSuchElementException:
            fail("can't find element with id=location")"""
    def tearDown(self):
        self.driver.quit()

suite = unittest.TestLoader().loadTestsFromTestCase(Testhw4)
unittest.TextTestRunner(verbosity=2).run(suite)
