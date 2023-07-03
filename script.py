#!/usr/bin/python3

import requests
import sys
from bs4 import BeautifulSoup
import os

# длина строки
LINE_LENGTH = 80
# имя файла результата
FILE_NAME = 'output.txt'

# класс для простого текста
class Text:
    def __init__(self, html):
        self.html = html
        self.text = html.text

    def add_line_breaks(self): # функция разбивания текста на строки
        result = ''
        index = LINE_LENGTH
        while (len(self.text) / index > 0):
            while (index < len(self.text) and self.text[index] != ' ' and index > 0):
                index -= 1
            result += self.text[0 : index]
            result += '\n'
            self.text = self.text[index + 1 : len(self.text)]
            index = LINE_LENGTH
        result += self.text
        self.text = result

# класс для контента со ссылками
class Content(Text):
    def add_links(self): # функция добавлени адресов ссылок в текст
        for a in self.html.findAll('a'):
            if a.string == None:
                a.string = ''
            a.string = a.string + "[{}]".format(a['href'])
        self.text = self.html.text

def get_tags_from_file(file_name, default_values): # функция получения тэгов из файла
    tags = []
    try:
        file = open(file_name, "r")
        while file and True:
            line = file.readline()
            if not line:
                break
            tags.append(line.strip())
    except FileNotFoundError:
        tags = default_values
    return tags

def create_path(url):
    url = url[url.find('://') + 3 : len(url)]
    dirs = url.split('/')
    path = ''
    for dir in dirs:
        path = dir + '/'
        if not(os.path.exists(path)):
            os.mkdir(dir)
        os.chdir(os.getcwd() + '/' + dir)

# извлечение html-страницы по url
url = sys.argv[1]
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# получение тэгов для поиска информации
header_tags = get_tags_from_file('header_tags.txt', ['h1', 'h2'])
content_tags = get_tags_from_file('content_tags.txt', ['p'])

# получение заголовков и контента
if (soup.article):
    headers = soup.article.find_all(header_tags)
    contents = soup.article.find_all(content_tags)
else:
    headers = soup.find_all(header_tags)
    contents = soup.find_all(content_tags)

# обработка заголовков и контента, формирование результата
result = ''
for title in headers:
    header = Text(title)
    header.add_line_breaks()
    result += f'{header.text}\n'
for p in contents:
    content = Content(p)
    content.add_links()
    content.add_line_breaks()
    result += f'{content.text}\n'

# формирование пути для выходного файла по url
create_path(url)
print(f'Результат: {os.getcwd()}/{FILE_NAME}')

# запись результата в файл
file = open(FILE_NAME, "w")
file.write(result)
file.close()
