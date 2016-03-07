from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# This example is from http://www.seleniumhq.org/docs/03_webdriver.jsp

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
# If you download the chrome driver and put it in your path, then do:
# driver = webdriver.Chrome()

# go to the google home page
driver.get("http://www.google.com")
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
WebDriverWait(driver, 10)
driver.get("https://www.pytho.org/")

# the page is ajaxy so the title is originally this:
for win in driver.window_handles:
    driver.switch_to.window(win)
    WebDriverWait(driver, 10)
    print driver.title

driver.quit()
