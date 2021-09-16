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

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(f'td[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def choose_adults(self, count=1):
        select_element = self.find_element_by_id('xp__guests__toggle')
        select_element.click()


        #While loop to decrease the adults value until is 1 before we can start increasing.
        while True:
            decrease_adult_element = self.find_element_by_css_selector('button[aria-label="Decrease number of Adults"]')
            decrease_adult_element.click()

            #Check and see the input value field accepting the value of Adults number
            adult_value_element = self.find_element_by_id('group_adults')
            adult_value = adult_value_element.get_attribute('value')

            #If condition to check if value is 1
            if int(adult_value) == 1:
                break

        #check and increment the value of the Adults count
        increase_adult_element = self.find_element_by_css_selector('button[aria-label="Increase number of Adults"]')

        for i in range(count -1):
            increase_adult_element.click()

