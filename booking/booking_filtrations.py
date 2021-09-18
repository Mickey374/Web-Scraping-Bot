#This class will actually host all my filtrations after the search button brings out some results for which I #will call the instance of this class in another method in another file

#Applying piping to the driver variable element created to work with the WebDriver imported
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltrations():
    def __init__(self, driver:WebDriver):
        self.driver = driver
        

    def filtrations(self, *star_values):
        star_filtration_box = self.driver.find_element_by_id('filter_class')
        star_filtration_element = star_filtration_box.find_elements_by_css_selector('*')
        
        #print(len(star_filtration_element))

        #A loop to control the iteration of the elements till we find 5 star rating and click on it
        for star_value in star_values:
            for star_element in star_filtration_element:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()
