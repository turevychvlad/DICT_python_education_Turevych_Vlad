import os
import re
import string
import requests
from bs4 import BeautifulSoup

# вимикаємо SSL-перевірку, бо деякі сайти можуть мати самопідписані сертифікати
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

HEADERS = {
    'Accept-Language': 'en-US,en;q=0.5',  # примусово ставимо англійську мову
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36'
}

# Етап 1: запит до API, парсимо JSON, витягуємо цитату

def get_quote():
    url = input("Input the URL:\n> ").strip()
    try:
        res = requests.get(url, verify=False, headers=HEADERS)
        if res.status_code != 200:
            print("Invalid quote resource!")
            return
        data = res.json()
        quote = data.get('content')
        if not quote:
            print("Invalid quote resource!")
        else:
            print(quote)
    except Exception:
        print("Invalid quote resource!")

# Етап 2: дістаємо title та description з IMDb

def get_movie_info():
    url = input("Input the URL:\n> ").strip()
    if 'imdb.com/title/' not in url:
        print("Invalid movie page!")
        return
    try:
        res = requests.get(url, headers=HEADERS, verify=False)
        if res.status_code != 200:
            print("Invalid movie page!")
            return
        soup = BeautifulSoup(res.content, 'html.parser')
        title_tag = soup.find('title')
        desc_tag = soup.find('meta', {'name': 'description'})
        if not title_tag or not desc_tag:
            print("Invalid movie page!")
            return
        title = title_tag.text.strip()
        description = desc_tag['content'].strip()
        print({"title": title, "description": description})
    except Exception:
        print("Invalid movie page!")

# Етап 3: зберігаємо HTML сторінку у файл

def save_html():
    url = input("Input the URL:\n> ").strip()
    try:
        res = requests.get(url, verify=False, headers=HEADERS)
        if res.status_code != 200:
            print(f"The URL returned {res.status_code}!")
            return
        with open("source.html", "wb") as f:
            f.write(res.content)
        print("Content saved.")
    except Exception:
        print("Error occurred while fetching the page.")

# допоміжна функція для створення коректного імені файлу

def sanitize_filename(name):
    name = name.translate(str.maketrans('', '', string.punctuation)).replace(' ', '_')
    return name.strip()

# Етап 4-5: завантажуємо статті за типом і зберігаємо у відповідну директорію

def save_articles():
    page_count = int(input())  # кількість сторінок
    article_type = input().strip().lower()  # тип статей
    base_url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2022&page='
    
    for page in range(1, page_count + 1):
        dir_name = f"Page_{page}"
        os.makedirs(dir_name, exist_ok=True)
        
        url = base_url + str(page)
        res = requests.get(url, headers=HEADERS, verify=False)
        if res.status_code != 200:
            continue

        soup = BeautifulSoup(res.content, 'html.parser')
        articles = soup.find_all('article')

        for article in articles:
            art_type_tag = article.find('span', {'data-test': 'article.type'})
            found_type = art_type_tag.text.strip().lower() if art_type_tag else ""
            if article_type not in found_type:
                continue

            link_tag = article.find('a', href=True)
            if not link_tag or not link_tag['href'].startswith('/articles/'):
                continue

            article_url = 'https://www.nature.com' + link_tag['href']
            article_res = requests.get(article_url, headers=HEADERS, verify=False)
            if article_res.status_code != 200:
                continue

            article_soup = BeautifulSoup(article_res.content, 'html.parser')
            body = article_soup.find('div', class_=lambda x: x and 'body' in x)
            if not body:
                body = article_soup.find('div', {'role': 'main'})
            if not body:
                continue

            content = body.get_text(strip=True)
            title = link_tag.text.strip()
            filename = sanitize_filename(title) + ".txt"
            filepath = os.path.join(dir_name, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    print("Saved all articles.")

# меню вибору етапів

def main():
    print("Вибери етап: 1, 2, 3 або 4")
    stage = input("> ").strip()
    if stage == '1':
        get_quote()
    elif stage == '2':
        get_movie_info()
    elif stage == '3':
        save_html()
    elif stage == '4':
        save_articles()
    else:
        print("Invalid stage")

if __name__ == "__main__":
    main()
