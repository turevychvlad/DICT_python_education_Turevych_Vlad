import requests
from bs4 import BeautifulSoup
import string
import os

# етап 1: отримання цитати з API
def get_quote():
    url = input("Input the URL:\n> ").strip()  # отримаємо URL від користувача
    try:
        response = requests.get(url)  # надіслати GET-запит
        if response.status_code != 200:
            print("Invalid quote resource!")  # якщо статус не 200 — помилка
            return
        data = response.json()  # розпарсити JSON відповідь
        if 'content' not in data:
            print("Invalid quote resource!")  # якщо немає ключа 'content' — помилка
            return
        print(data['content'])  # вивести цитату
    except:
        print("Invalid quote resource!")  # будь-яка інша помилка — теж виводимо помилку

# етап 2: парсинг imdb сторінки фільму
def get_imdb_info():
    url = input("Input the URL:\n> ").strip()  # отримаємо URL
    if "imdb.com/title/" not in url:
        print("Invalid movie page!")  # перевірка на IMDb movie page
        return
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if response.status_code != 200:
        print("Invalid movie page!")
        return
    soup = BeautifulSoup(response.text, 'html.parser')  # парсимо HTML
    title_tag = soup.find('title')  # шукаємо тег <title>
    desc_tag = soup.find('meta', {'name': 'description'})  # шукаємо опис
    if not title_tag or not desc_tag:
        print("Invalid movie page!")  # якщо нічого не знайдено
        return
    title = title_tag.text.strip().split(" - ")[0]  # обробляємо заголовок
    desc = desc_tag.get('content').strip()  # отримуємо текст опису
    print({"title": title, "description": desc})  # виводимо словник

# етап 3: збереження HTML-коду сторінки
def save_html():
    url = input("Input the URL:\n> ").strip()  # запитати URL
    response = requests.get(url)  # зробити запит
    if response.status_code != 200:
        print(f"The URL returned {response.status_code}!")  # вивести код помилки
        return
    with open("source.html", "wb") as f:  # запис у файл у бінарному режимі
        f.write(response.content)
    print("Content saved.")  # повідомлення про успіх

# етап 4: парсинг статей типу News зі сторінки nature.com
def save_articles():
    url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page=3"
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("article")  # знаходимо всі теги article
    saved = []  # список збережених файлів
    for article in articles:
        type_tag = article.find("span", {"data-test": "article.type"})
        if not type_tag or type_tag.text.strip() != "News":  # фільтрація тільки "News"
            continue
        link_tag = article.find("a", {"data-track-action": "view article"})
        if not link_tag:
            continue
        article_url = "https://www.nature.com" + link_tag.get("href")  # повне посилання
        article_resp = requests.get(article_url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        article_soup = BeautifulSoup(article_resp.content, "html.parser")
        body_tag = article_soup.find("div", class_="c-article-body")  # тіло статті
        if not body_tag:
            continue
        title = link_tag.text.strip()  # заголовок статті
        # форматування назви файла
        filename = title.translate(str.maketrans('', '', string.punctuation)).replace(' ', '_') + ".txt"
        filepath = os.path.join(".", filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(body_tag.text.strip())  # запис тексту статті
        saved.append(filename)
    print("Saved articles:", saved)  # вивід збережених файлів

# етап 5: парсинг кількох сторінок і кількох типів статей
def multi_page_parser():
    page_count = int(input("> "))  # кількість сторінок
    article_type = input("> ").strip()  # тип статей
    base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page="

    for i in range(1, page_count + 1):
        os.makedirs(f"Page_{i}", exist_ok=True)  # створюємо директорію для сторінки
        response = requests.get(base_url + str(i), headers={'Accept-Language': 'en-US,en;q=0.5'})
        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all("article")
        for article in articles:
            type_tag = article.find("span", {"data-test": "article.type"})
            if not type_tag or type_tag.text.strip() != article_type:
                continue  # пропускаємо не ті типи статей
            link_tag = article.find("a", {"data-track-action": "view article"})
            if not link_tag:
                continue
            article_url = "https://www.nature.com" + link_tag.get("href")
            article_resp = requests.get(article_url, headers={'Accept-Language': 'en-US,en;q=0.5'})
            article_soup = BeautifulSoup(article_resp.content, "html.parser")
            body_tag = article_soup.find("div", class_="c-article-body")
            if not body_tag:
                continue
            title = link_tag.text.strip()
            filename = title.translate(str.maketrans('', '', string.punctuation)).replace(' ', '_') + ".txt"
            filepath = os.path.join(f"Page_{i}", filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(body_tag.text.strip())
    print("Saved all articles.")  # повідомлення про завершення

# запуск потрібної функції поетапно для перевірки
# get_quote()
# get_imdb_info()
# save_html()
# save_articles()
# multi_page_parser()
