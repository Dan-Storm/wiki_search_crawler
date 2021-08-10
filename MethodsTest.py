import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from WikiMethods import WikiMethods as WM



class MethodsTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/danielstorm/Downloads/chromedriver")
        
    def test_wiki_methods(self):
        URL = "https://en.wikipedia.org/wiki/Lexington,_Edwards_County,_Illinois"
        wm = WM(self.driver)
        with self.subTest("Testing navigate_to_url"):
            wm.navigate_to_url(URL)
            self.assertTrue(self.driver.title in "Lexington, Edwards County, Illinois - Wikipedia")
            print("Page title matches storred title, testing will continue") 
 
        with self.subTest("Testing get last edit"):
            last_edit = wm.get_last_edit()
            self.assertTrue("This page was last edited on 15 January 2018, at 01:26" in last_edit.text)
            print("Last edit date matches storred date, testing will continue")  

        with self.subTest("Testing get_all_links_from_body"):
            all_links = wm.get_all_links_from_body()
            self.assertTrue(len(all_links) == 87)
            print("Got all links from body, testing will continue")

        with self.subTest("Testing filter_links"):
            filtered_links = wm.filter_links(all_links)
            self.assertTrue(len(filtered_links) == 65)
            print("Filtered links from body text, testing will continue")

        with self.subTest("Testing get_link"):
            link_to_get_text = filtered_links[23].text
            starting_page_title = format(self.driver.title)
            link_to_click = wm.get_link(link_to_get_text)
            link_to_click.click()
            self.assertTrue(self.driver.title in "Bone Gap, Illinois - Wikipedia")
            print("Got link, navigating back to " + starting_page_title + " page") 
            self.driver.back()
            self.assertTrue(self.driver.title in "Lexington, Edwards County, Illinois - Wikipedia")
            print("Navigated back to the correct page. Testing will continue")      

        with self.subTest("Testing get_random_link"):
            wm.get_random_link()
            self.assertTrue(self.driver.title not in "Lexington, Edwards County, Illinois - Wikipedia")
            print("Got random link, navigating back to " + starting_page_title + " page") 
            self.driver.back()
            self.assertTrue(self.driver.title in "Lexington, Edwards County, Illinois - Wikipedia")
            print("Navigated back to the correct page. Testing will continue")

    def tearDown(self):
        self.driver.close()               

if __name__ == "__main__":
    unittest.main()

