import os
import string
import requests
from bs4 import BeautifulSoup


def scrape_nature_articles():
    try:
        num_pages = int(input("> "))
        article_type = input("> ")
    except ValueError:
        print("Invalid input")
        return

    base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page="
    domain = "https://www.nature.com"

    for page_num in range(1, num_pages + 1):
        folder_name = f"Page_{page_num}"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        url = base_url + str(page_num)
        response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})

        if response.status_code != 200:
            print(f"The URL returned {response.status_code}!")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')

        for article in articles:
            span_type = article.find('span', {'data-test': 'article.type'})

            if span_type and span_type.text.strip() == article_type:
                a_tag = article.find('a', {'data-track-action': 'view article'})

                if not a_tag:
                    continue

                article_link = domain + a_tag.get('href')
                raw_title = a_tag.text.strip()

                trans_table = str.maketrans('', '', string.punctuation)
                clean_title = raw_title.translate(trans_table).replace(' ', '_')

                file_name = f"{clean_title}.txt"
                file_path = os.path.join(folder_name, file_name)

                article_resp = requests.get(article_link, headers={'Accept-Language': 'en-US,en;q=0.5'})
                if article_resp.status_code == 200:
                    article_soup = BeautifulSoup(article_resp.content, 'html.parser')

                    # Оновлений пошук тіла статті згідно з коментарем
                    body = article_soup.find("p", class_="article__teaser")

                    if body:
                        article_text = str(body.text).strip()

                        with open(file_path, 'wb') as file:
                            file.write(article_text.encode('utf-8'))

    print("Saved all articles.")


if __name__ == "__main__":
    scrape_nature_articles()