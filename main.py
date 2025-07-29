from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def find_any_element(element, xpaths):
    for xpath in xpaths:
        elements = element.find_elements(by="xpath", value=xpath)
        if elements:
            return elements[0]
    return None

website = "https://www.freemalaysiatoday.com"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(website)

articles = driver.find_elements(by="xpath", value='//article')

dict_articles = []

for article in articles:
    main = find_any_element(article, ['./figure/a','./div/figure/a'])
    if main:
        title = main.get_attribute("aria-label")
        link = main.get_attribute("href")
        dict_articles.append({'title':title, 'link':link})

print(dict_articles)

#input("Press Enter Key to close the browser...")
driver.quit()