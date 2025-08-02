from selenium import webdriver #Mandatory
from selenium.webdriver.chrome.options import Options #options for running selenium in background
from selenium.webdriver.chrome.service import Service #Mandatory
from webdriver_manager.chrome import ChromeDriverManager #Mandatory
import pandas as pd #labeled table for data analysis

def find_any_element(element, xpaths):
    for xpath in xpaths:
        elements = element.find_elements(by="xpath", value=xpath)
        if elements:
            return elements[0]
    return None

website = "https://www.freemalaysiatoday.com"

#headless mode - running without display
options = Options()
options.add_argument("--headless=new")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

articles = driver.find_elements(by="xpath", value='//article')

dict_articles = []

for article in articles:
    main = find_any_element(article, ['./figure/a','./div/figure/a'])
    if main:
        title = main.get_attribute("aria-label")
        link = main.get_attribute("href")
        dict_articles.append({'title':title, 'link':link})

#print(dict_articles)

df_articles = pd.DataFrame(dict_articles)
df_articles.to_csv('./output/all_articles.csv')
print("complete extraction")

#input("Press Enter Key to close the browser...")
driver.quit()