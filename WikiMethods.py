from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E

class WikiMethods(object):

    wait_time = 30
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = W(driver, self.wait_time)
    

    def navigate_to_url(self, url):
        try:
            print("Enter Method: get_url")
            print("     Navigating to - " + url)
            self.driver.get(url)
            print("     Maximizing window")
            self.driver.maximize_window()
            print("Exit Method: get_url")
        except Exception as e: 
            print("     Failed to get random link. See details below")
            print("     " + format(e)) 
            print("     Closing window")
            self.driver.close() 
            print("Exit Method: get_url")
            quit() 

    def get_last_edit(self):
        try:
            print("Enter Method: get_last_edit")
            last_edit = self.wait.until(E.presence_of_element_located((By.ID, "footer-info-lastmod")))
            print("     Last Edit: " + last_edit.text)
            print("Exit Method: get_last_edit")
            return last_edit
        except Exception as e: 
            print("     Failed to get random link. See details below")
            print("     " + format(e)) 
            print("     Closing window")
            self.driver.close() 
            print("Exit Method: get_last_edit")
            quit() 

    def get_random_link(self):
        try:
            print("Enter Method: get_random_link")
            print("     Getting random link")
            link = self.wait.until(E.presence_of_element_located((By.ID, "n-randompage")))
            #link = self.driver.find_element_by_id("n-randompage")
            print("     Found random link element")
            print("     Clicking...")
            print("Exit Method: get_random_link")
            link.click()
            
        except Exception as e:
            print("     Failed to get random link. See details below")
            print("     " + format(e)) 
            print("     Closing window")
            self.driver.close() 
            print("Exit Method: get_random_link")
            quit() 

    def get_link(self, link_text):
        try:
            print("Enter Method: get_link")
            print("     Searching for link")
            link = self.wait.until(E.presence_of_element_located((By.LINK_TEXT, link_text)))
            return link
        except Exception as e:
            print("     Failed to find link element. See details below")
            print("     " + format(e)) 
            print("     Closing window")
            self.driver.close() 
            print("Exit Method: get_link")
            quit() 

    def get_all_links_from_body(self):
        try:
            print("Enter Method: get_all_links_from_body")
            link_list = []
            print("     Getting body content")
            body_elements = self.wait.until(E.presence_of_all_elements_located((By.ID, "bodyContent")))
            for element in body_elements:
                print("     Filtering for anchor tags")
                anchor_tags = element.find_elements_by_tag_name("a")
                for tag in anchor_tags:
                    link_list.append(tag)
            print("     Got " + format(len(link_list)) +" links from body content")
            print("Exit Method: get_all_links_from_body")
            return link_list

        except Exception as e:
            print("     Failed to get all links. See details below")
            print("     " + format(e)) 
            print("     Closing window")
            self.driver.close() 
            print("Exit Method: get_all_links_from_body")
            quit() 

    def filter_links(self, link_list):
        try:
            print("Enter Method: filter_links")
            filtered_links = []
            print("     Filtering links")
            for link in link_list:
                # Filters links with no text, links to edit the page, and links without alphanumeric characters
                if len(link.text) > 1 and link.text != "edit" and (link.text.isalnum() or " " in link.text) and link.text != "ISBN" and "\"" not in link.text:
                    #print(link.text)
                    filtered_links.append(link) 
            print("     Filtered down to " + format(len(filtered_links)) +" links from body content")
            print("Exit Method: filter_links")
            return filtered_links

        except Exception as e:
            print("     Failed to filter links. See details below")
            print("     " + format(e)) 
            print("     Closing window")
            self.driver.close() 
            print("Exit Method: filter_links")
            quit() 

    def print_and_format_link_list_text(self, link_list):
        try:
            print("Enter Method: print_and_format_link_list_text")        
            print("     Formatting and printing links")
            for link in link_list:
                print(link.text + ",")
        except Exception as e:
            print("     Failed to format and print link text. See details below")
            print("     " + format(e)) 
            print("     Closing window")
            self.driver.close() 
            print("Exit Method: print_and_format_link_list_text")
            quit()  

    def is_wikipedia_article(self):
        try:
            print("Enter Method: is_wikipedia_article") 
            if "https://en.wikipedia.org/wiki/" not in self.driver.current_url or "https://en.wikipedia.org/wiki/Wikipedia" in self.driver.current_url or "https://en.wikipedia.org/wiki/Help" in self.driver.current_url:
                print("Navigated out of the bounds of the game. Going back")
                self.driver.back()
            print("Exit Method: is_wikipedia_article")
        except Exception as e:
            print("     Failed to determine if page was a wikipedia page")
            print("     " + format(e)) 
            print("     Closing window")
            self.driver.close() 
            print("Exit Method: is_wikipedia_article")
            quit()            

    def find_link_to_click(self, list_of_words, list_of_links, i):
        try:
            print("Enter Method: find_link_to_click")
            link_count = len(list_of_links)-1 
            for link in list_of_links:
                for count, word in enumerate(list_of_words):
                    #print(len(word)*".")
                    print(word)
                    if word in link.text.upper():
                        print("     LINK FOUND!!!!!!!!!!!!!!!!!!!:" + link.text.upper())
                        print("Exit Method: find_link_to_click")
                        link.click()
                        print("CLICK NUMBER: " + format(i))
                        return
                    elif count == link_count:
                        self.get_random_link()
                        print("CLICK NUMBER: " + format(i))
                        print("Exit Method: find_link_to_click")
                        return
                    else:
                        continue  

        except Exception as e:
            print("     Failed to find find a link to click. See details below")
            print("     " + format(e)) 
            print("     Closing window")
            self.driver.close() 
            print("Exit Method: find_link_to_click")
            quit()  
            
    def get_all_text(self):
        try:
            print("Enter Method: find_keywords")
            keywords = self.driver.find_element_by_xpath("/html/body").text
            
            print("Exit Method: find_keywords")
        except Exception as e:    
            print("     Failed to find duplicates. See details below")
            print("     " + format(e)) 
            print("     Closing window")
            self.driver.close() 
            print("Exit Method: find_keywords")
            quit()  
            
    def find_duplicates(self, list):
        try:
            print("Enter Method: find_duplicates")
            duplicates=[]
            unique=[]
            print("     Iterating over list to find duplicates")
            for item in list:
                if item.text not in duplicates:
                    unique.append(format(item.text))
                else:
                    duplicates.append(format(item.text))
                    print(format(item.text))
            print("     Found " + format(len(duplicates)) + " duplicates")
            print("Exit Method: find_duplicates")
        except Exception as e:                
            print("     Failed to find duplicates. See details below")
            print("     " + format(e)) 
            print("     Closing window")
            self.driver.close() 
            print("Exit Method: find_duplicates")
            quit()  

