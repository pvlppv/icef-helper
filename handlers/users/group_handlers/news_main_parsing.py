import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time



# def get_first_news():
#     headers = {
#         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"
#     }
#
#     url = "https://icef.hse.ru/news/"
#     r = requests.get(url=url, headers=headers)
#
#     soup = BeautifulSoup(r.text, "lxml")
#     articles_cards = soup.find_all("div", class_="post")
#
#     news_dict = {}
#     for article in articles_cards:
#         article_title = article.find("div", class_="post__content").text.strip()
#         article_desc = article.find("div", class_="post__text").text.strip()
#         article_url = article.find("a").get("href")
#         article_date_time = article.find("span", class_="post__date").text.strip()
#
#         # более продвинутое время публикации новости
#         # date_from_iso = datetime.fromisoformat(article_date_time)
#         # date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
#         # article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())
#
#         article_id = article_url.split("/")[-1]
#         article_id = article_id[:-5]
#
#         # print(f"{article_title} | {article_url} | {article_date_time}")
#
#         news_dict[article_id] = {
#             "article_date_time": article_date_time,
#             "article_title": article_title,
#             "article_url": article_url,
#             "article_desc": article_desc
#         }
#
#     with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/icef_news_icefhse.json", "w") as file:
#     # with open("/root/bot/handlers/users/icef_news_icefhse.json", "w") as file:
#         json.dump(news_dict, file, indent=5, ensure_ascii=False)
#

def check_news_update():
    # with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/group_handlers/icef_news_icefhse.json") as file:
    with open("/root/bot/handlers/users/group_handlers/icef_news_icefhse.json") as file:
        news_dict = json.load(file)
        # print(news_dict)

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"
    }

    url = "https://icef.hse.ru/news/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("div", class_="post")

    fresh_news = {}
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

            fresh_news[article_id] = {
                "article_date_time": article_date_time,
                "article_title": article_title,
                "article_url": article_url,
                "article_desc": article_desc
            }

    # with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/group_handlers/icef_news_icefhse.json", "w") as file:
    with open("/root/bot/handlers/users/group_handlers/icef_news_icefhse.json", "w") as file:
        json.dump(news_dict, file, indent=5, ensure_ascii=False)

    return fresh_news
#
#
# def main():
#     # get_first_news()
# check_news_update()
#
#
# if __name__ == '__main__':
#     main()