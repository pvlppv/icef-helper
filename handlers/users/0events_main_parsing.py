# def get_first_events():
#     headers = {
#         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
#     }
#
#     url = "https://icef.hse.ru/announcements"
#     r = requests.get(url=url, headers=headers)
#
#     soup = BeautifulSoup(r.text, "lxml")
#     articles_cards = soup.find_all("div", class_="b-events")
#
#     events_dict = {}
#     for article in articles_cards:
#         article_title = article.find("a", class_="link").text.strip()
#         article_date = article.find("div", class_="title").text.strip()
#         article_time = article.find("div", class_="b-events__extra date").text.strip()
#         article_address = article.find("p", class_="b-text-grey small").text.strip()
#         article_url = article.find("a").get("href")
#
#         article_id = article_url.split("/")[-1]
#         article_id = article_id[:-5]
#
#         # print(f"{article_title} | {article_date} | {article_time} | {article_address} | {article_url}")
#
#         events_dict[article_id] = {
#             "article_title": article_title,
#             "article_date": article_date,
#             "article_time": article_time,
#             "article_address": article_address,
#             "article_url": article_url,
#         }
#
#     with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/0events_dict.json", "w") as file:
#     # with open("/root/bot/handlers/users/0events_dict.json", "w") as file:
#         json.dump(events_dict, file, indent=5, ensure_ascii=False)



# def check_events_update():
#     # with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/0events_dict.json") as file:
#     with open("/root/bot/handlers/users/0events_dict.json") as file:
#         events_dict = json.load(file)
#
#     headers = {
#         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
#     }
#
#     url = "https://icef.hse.ru/announcements"
#     r = requests.get(url=url, headers=headers)
#
#     soup = BeautifulSoup(r.text, "lxml")
#     articles_cards = soup.find_all("div", class_="b-events")
#
#     new_events = {}
#     for article in articles_cards:
#         article_url = article.find("a").get("href")
#         article_id = article_url.split("/")[-1]
#         article_id = article_id[:-5]
#
#         if article_id in events_dict:
#             continue
#         else:
#             article_title = article.find("a", class_="link").text.strip()
#             article_date = article.find("div", class_="title").text.strip()
#             article_time = article.find("div", class_="b-events__extra date").text.strip()
#             article_address = article.find("p", class_="b-text-grey small").text.strip()
#
#             events_dict[article_id] = {
#                 "article_title": article_title,
#                 "article_date": article_date,
#                 "article_time": article_time,
#                 "article_address": article_address,
#                 "article_url": article_url,
#             }
#
#             new_events[article_id] = {
#                 "article_title": article_title,
#                 "article_date": article_date,
#                 "article_time": article_time,
#                 "article_address": article_address,
#                 "article_url": article_url,
#             }
#
#     # with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/0events_dict.json", "w") as file:
#     with open("/root/bot/handlers/users/0events_dict.json", "w") as file:
#         json.dump(events_dict, file, indent=5, ensure_ascii=False)
#
#     return new_events

# def main():
#     # get_first_events()
# check_events_update()
#
#
# if __name__ == '__main__':
#     main()



