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
        #List to handle all data scraped
        collection = []

        #for loop to print out all the Titles/Names of hotels
        for deal_box in self.deal_boxes:

            #Get hotel name
            hotel = deal_box.find_element_by_class_name('sr-hotel__name').get_attribute('innerHTML').strip()
            
            #Get Hotel price
            price = deal_box.find_element_by_class_name('prco-valign-middle-helper').get_attribute('innerHTML').strip()
            
            #Get hotel score
            score = deal_box.get_attribute('data-score').strip()

            collection.append(
                [hotel, price, score]
            )
        
        return collection


        