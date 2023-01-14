import time
import json

import requests
from bs4 import BeautifulSoup

def icefhse_parsing():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"
    }

    url = "https://icef.hse.ru/news/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("div", class_="post")

    news_dict = {}
    for article in articles_cards:
        article_title = article.find("div", class_="post__content").text.strip()
        article_desc = article.find("div", class_="post__text").text.strip()
        article_url = article.find("a").get("href")
        article_date_time = article.find("span", class_="post__date").text.strip()

        article_id = article_url.split("/")[-1]
        article_id = article_id[:-5]

        news_dict[article_id] = {
            "article_date_time": article_date_time,
            "article_title": article_title,
            "article_url": article_url,
            "article_desc": article_desc
        }
        print(news_dict)
    # with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/icef_news_icefhse.json", "w") as file:
    with open("/root/bot/handlers/icef_news_icefhse.json", "w") as file:
        json.dump(news_dict, file, indent=5, ensure_ascii=False)

def icefhse_update():
    while True:
        # with open("/icef_news_icefhse.json") as file:
        with open("/root/bot/icef_news_icefhse.json") as file:
            news_dict = json.load(file)

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"
        }

        url = "https://icef.hse.ru/news/"
        r = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(r.text, "lxml")
        articles_cards = soup.find_all("div", class_="post")

        for article in articles_cards:
            article_url = article.find("a").get("href")
            article_id = article_url.split("/")[-1]
            article_id = article_id[:-5]

            if article_id in news_dict:
                continue
            else:
                article_title = article.find("div", class_="post__content").text.strip()
                article_desc = article.find("div", class_="post__text").text.strip()
                article_date_time = article.find("span", class_="post__date").text.strip()

                news_dict[article_id] = {
                    "article_date_time": article_date_time,
                    "article_title": article_title,
                    "article_url": article_url,
                    "article_desc": article_desc
                }

        # with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/icef_news_icefhse.json", "w") as file:
        with open("/root/bot/icef_news_icefhse.json", "w") as file:
            json.dump(news_dict, file, indent=5, ensure_ascii=False)
        print('news from icef.hse.ru done')
        time.sleep(30)

if __name__ == '__main__':
    icefhse_parsing()
    # icefhse_update()
