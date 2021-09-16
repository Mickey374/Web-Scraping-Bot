import os
import booking.constants as const
from selenium import webdriver

class Booking(webdriver.Chrome):
    def __init__(self, driver_path= r"C:/Users/hp/Desktop/PERSONAL/Thelma_Work", teardown = False):
        self.driver_path = driver_path

        #Implementing a teardown for a context manager
        self.teardown = teardown
        
        #OS path to handle Chrome Webdriver path.
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__()

        #Adding implicitly wait method
        self.implicitly_wait(15)
        #A cleaner loop for my bot for efficiency
        self.maximize_window()

    def __exit__(self, type, value, traceback):
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.get(const.BASE_URL)
    
    def currency_convert(self, currency=None):
        currency_element = self.find_element_by_css_selector('button[data-tooltip-text="Choose your currency"]')
        currency_element.click()

        selected_currency_element = self.find_element_by_css_selector(f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()
    
    def place_to_go(self, place_to):
        place_going = self.find_element_by_id('ss')
        place_going.clear()
        place_going.send_keys(place_to)

        place_click = self.find_element_by_css_selector('li[data-i="0"]')
        place_click.click()