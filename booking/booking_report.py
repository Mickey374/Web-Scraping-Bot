#This file will include methods that will pass all the results we need from the boxes

#Import the Webdriver elements to enable boxes_section_elements function as a webdriver using Typing
from selenium.webdriver.remote.webelement import WebElement

class BookingReport():
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_boxes()
    
    def pull_boxes(self):
        return self.boxes_section_element.find_elements_by_class_name('sr_property_block')
    
    def pull_titles(self):
        #for loop to print out all the Titles/Names of hotels
        for deal_box in self.deal_boxes:
            hotel = deal_box.find_element_by_class_name('sr-hotel__name').get_attribute('innerHTML').strip()
            print(hotel)

        