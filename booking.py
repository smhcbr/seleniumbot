import os
from lib2to3.pgen2 import driver
from selenium.webdriver.common.keys import Keys
from unicodedata import numeric
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import booking.constants as const
from selenium.webdriver.common.by import By

class Booking(webdriver.Chrome):
     def __init__(self, driver_path=r"/Users/smhcbr/Desktop/seleniumdrivers", teardown=False):
         self.driver_path = driver_path
         self.teardown = teardown
         os.environ['PATH'] += self.driver_path
         super(Booking, self).__init__()
         self.maximize_window()

     def __exit__(self, exc_type, exc_val, exc_tb):
         if self.teardown:
            self.quit()
    
     def land_first_page(self):
            self.get(const.BASE_URL)
            

     def search_review(self, article_name):
         print(article_name)
         try:
             print('tryic', article_name)
             wait = WebDriverWait(self, 5)
             wait.until(EC.text_to_be_present_in_element((By.ID, 'searchbar-input'), article_name)) 
             girdi = self.find_element_by_id('searchbar-input') 
             girdi.send_keys(article_name) 
         except TimeoutException:
             self.refresh()


     def search_click(self):
         search_bttn = self.find_element_by_css_selector(
             'button[class="outline-button outline_button_active autocomplete-button"]'
         )
         search_bttn.click()