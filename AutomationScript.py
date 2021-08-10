from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from WikiMethods import WikiMethods as WM
import time

URL = "https://en.wikipedia.org/wiki/Main_Page"
RANDOM = "https://en.wikipedia.org/wiki/Special:Random"
USA_URL = "https://en.wikipedia.org/wiki/United_States"

test_link = "https://en.wikipedia.org/wiki/Albanian_Greek_Catholic_Church"
driver = webdriver.Chrome("/Users/danielstorm/Downloads/chromedriver")
jesus_words = ["JESUS", "CATHOLIC", "POPE", "BISHOP", "PREIST", "RELIGION", "FAITH", "GOD", "BAPTIST",
                "METHODIST", "LUTHERAN", "PASTOR", "BIBLE", "THEOLOGY", "MEXICO", "ITALY", "ROME", "VATICAN", "GUATEMALA", "SPAIN", "SPANISH", "LATIN",
                "CANADA", "UNITED KINGDOM", "IRELAND", "FRANCE", "GERMANY", "ALBANIA", "BELARUS", "GREECE", "RUSSIA", "MACEDONIA", "ROMANIA", "UKRAINE",
                "AUSTRALIA", "BRAZIL", "ARGENTINA", "COLUMBIA", "CHILE", "PARAGUAY", "ANDORRA", "CROATIA", "POLAND", "MALTA", "MONACO", "PHILIPPEANS", "VENEZUELA",
                "HAITI", "COSTA RICA", "AFRICA", "SOUTH AMERICA", "NORTH AMERICA", "EUROPE", "ASIA", "AMERICA", "FRENCH", "ITALIAN", "INDIA", "CHINA", "CHRIST", "CHURCH"
                ]

wm = WM(driver)

# Navigate to Wikipedia

success = 0
fail = 0

wm.navigate_to_url(URL)
# Click the Random article link
wm.get_random_link() 
navigation_history = []   
i = 1
while i < 6:
    for url in navigation_history:
        if driver.current_url == url:
            print("Stuck between atricles, getting random link")
            wm.get_random_link()
    navigation_history.append(driver.current_url)
    body_links = wm.get_all_links_from_body() 
    filtered_links = wm.filter_links(body_links)
    wm.find_link_to_click(jesus_words, filtered_links, i)
    wm.is_wikipedia_article()
    if driver.current_url == "https://en.wikipedia.org/wiki/Jesus":
        print("YAYYYY IT WORKED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        success += 1
        break
    if i == 5:
        print("NOPE IT DIDN'T WORK")
        fail += 1
    i += 1
print("SUCCESSES: " + format(success))
print("FAILURES: " + format(fail))
driver.close()
