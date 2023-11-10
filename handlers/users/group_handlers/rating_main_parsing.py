import json
import requests
from bs4 import BeautifulSoup



headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

def get_page(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    # with open('/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/0rating_parsing/index.html', 'w') as file:
    with open("/root/bot/handlers/users/index.html", "w") as file:
        file.write(response.text)


def get_json(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    # with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/result_data.json", "w") as file:
    with open("/root/bot/handlers/users/result.json", "w") as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def collect_data():
    s = requests.Session()
    response = s.get(
        url="https://www.hse.ru/n/student-ratings/api?unit=123068296&course=1&from=696219378",
        headers=headers)

    data = response.json()

    result_data = []

    students = data.get('data')
    for student in students:
        name = student.get('title')
        place = student.get('place')
        average = student.get('gradeMid')
        min = student.get('gradeMin')
        percentile = student.get('percentil')
        gpa = student.get('gpa')

        result_data.append(
            {
                'name': name,
                'place': place,
                'average': average,
                'min': min,
                'percentile': percentile,
                'gpa': gpa
            }
        )

        # print(name, place, average, min, percentile, gpa)

    # with open("/Users/pavelpopov/PycharmProjects/ICEF Helper/handlers/users/result_data.json", "w") as file:
    with open("/root/bot/handlers/users/result_data.json", "w") as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)


def main():
    # get_page(url='https://www.hse.ru/ba/icef/ratings')
    # get_json(url='https://www.hse.ru/n/student-ratings/api?unit=123068296&course=1&from=696219378')
    collect_data()

if __name__ == '__main__':
    main()
