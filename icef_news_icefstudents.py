import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService

def icefstudents_parsing():
    options1 = webdriver.ChromeOptions()
    options1.add_argument('--headless')
    options1.add_argument('--no-sandbox')
    options1.add_argument('--disable-dev-shm-usage')
    options1.add_experimental_option("prefs", {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # service = ChromeService(executable_path='/Users/pavelpopov/Downloads/chromedriver')
    service = ChromeService(executable_path='/root/bot/chromedriver')
    driver = webdriver.Chrome(service=service, options=options1)
    driver.maximize_window()
    driver.get('http://www.python.org')
    assert "Python" in driver.title

    driver.get('https://icefstudents.hse.ru/')
    driver.implicitly_wait(10)
    cards = driver.find_elements(By.CLASS_NAME, 'js-feed-post')
    dict = {}
    for card in cards:
        title = card.find_element(By.CLASS_NAME, 'js-feed-post-title').text.strip()
        desc = card.find_element(By.CLASS_NAME, 'js-feed-post-descr').text.strip()
        date = card.find_element(By.CLASS_NAME, 'js-feed-post-date').text.strip()
        url = card.find_element(By.CSS_SELECTOR, '.js-feed-post [href]').get_attribute('href')

        dict[title] = {
            'title': title,
            'desc': desc,
            'date': date,
            'url': url
        }
    # with open('/icef_news_icefstudents.json', 'w') as file:
    with open('/root/bot/icef_news_icefstudents.json', 'w') as file:
        json.dump(dict, file, indent=4, ensure_ascii=False)
    driver.quit()

def icefstudents_update():
    while True:
        # with open('/icef_news_icefstudents.json') as file:
        with open('/root/bot/icef_news_icefstudents.json') as file:
            dict = json.load(file)

        options1 = webdriver.ChromeOptions()
        options1.add_argument('--headless')
        options1.add_argument('--no-sandbox')
        options1.add_argument('--disable-dev-shm-usage')
        options1.add_experimental_option("prefs", {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        # service = ChromeService(executable_path='/Users/pavelpopov/Downloads/chromedriver')
        service = ChromeService(executable_path='/root/bot/chromedriver')
        driver = webdriver.Chrome(service=service, options=options1)
        driver.maximize_window()
        driver.get('http://www.python.org')
        assert "Python" in driver.title

        driver.get('https://icefstudents.hse.ru/')
        driver.implicitly_wait(10)
        cards = driver.find_elements(By.CLASS_NAME, 'js-feed-post')
        for card in cards:
            title = card.find_element(By.CLASS_NAME, 'js-feed-post-title').text.strip()
            if title in dict:
                continue
            else:
                title = card.find_element(By.CLASS_NAME, 'js-feed-post-title').text.strip()
                desc = card.find_element(By.CLASS_NAME, 'js-feed-post-descr').text.strip()
                date = card.find_element(By.CLASS_NAME, 'js-feed-post-date').text.strip()
                url = card.find_element(By.CSS_SELECTOR, '.js-feed-post [href]').get_attribute('href')

                dict[title] = {
                    'title': title,
                    'desc': desc,
                    'date': date,
                    'url': url
                }
        # with open('/icef_news_icefstudents.json', 'w') as file:
        with open('/root/bot/icef_news_icefstudents.json', 'w') as file:
            json.dump(dict, file, indent=4, ensure_ascii=False)
        driver.quit()
        print('news from icefstudents.hse.ru done')
        time.sleep(30)

if __name__ == '__main__':
    icefstudents_update()
