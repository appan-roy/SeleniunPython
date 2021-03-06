from selenium import webdriver
from time import sleep
import unittest
import HtmlTestRunner

# Use these below three lines to run tests from command line
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

from pages.LoginPage import Loginpage
from pages.HomePage import Homepage


class Login_Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        
        super(Login_Test, cls).setUpClass()

        cls.driver = webdriver.Chrome("E:\\Softwares\\My PC Apps\\Selenium Python\\Webdrivers\\chromedriver_win32\\chromedriver.exe")

        cls.driver.maximize_window()

        cls.driver.implicitly_wait(10)
        
#     The test case name should start with test always. Naming convention is [test_*].

    def test_login_01_valid_credentials(self):
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        
#         Creating the object of Loginpage class
        login_pg = Loginpage(self.driver)
           
        login_pg.enter_username("Admin")
        login_pg.enter_password("admin123")
        login_pg.click_login_btn()
        
        sleep(2)
        
#         Creating the object of Loginpage class
        home_pg = Homepage(self.driver)
        
        home_pg.click_welcome()        
        home_pg.click_logout()
    
    def test_login_02_invalid_username(self):
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        
#         Creating the object of Loginpage class
        login_pg = Loginpage(self.driver)
           
        login_pg.enter_username("Admin1")
        login_pg.enter_password("admin123")
        login_pg.click_login_btn()
        
        message = self.driver.find_element_by_xpath("//span[@id='spanMessage']").text
        self.assertEqual(message, "Invalid credentials")
        
        
    @classmethod
    def tearDownClass(cls):
        
        super(Login_Test, cls).tearDownClass()
        
        cls.driver.close()
        
        cls.driver.quit()

        print("Test Completed")


# The below block is used to run the python unit test from terminal with HTML reports
if __name__ == '__main__': 
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/Softwares/My PC Apps/Selenium Python/Workspace/SeleniumPythonPOM/Reports'))