import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore
init()

args = sys.argv

if len(args) > 1:
    directory_name = args[1].split('-')[0]

    if directory_name:
        if not os.path.exists(directory_name):
            os.mkdir(directory_name)


def write_file(file_name, content):
    with open(directory_name + '/' + file_name, 'w', encoding='utf-8') as out_file:
        out_file.write(content)


def get_content(url):
    r = requests.get('https://' + url)
    if r:
        limited_content = ['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
        soup = BeautifulSoup(r.content, 'html.parser')
        file = open(directory_name + '/' + url, 'w', encoding='utf-8')
        for tag in soup.find_all(limited_content):
            print(Fore.BLUE + str(tag.string) if tag.find('a') else Fore.WHITE + str(tag.string))
            # if tag.find('a'):
            #     print(Fore.BLUE + str(tag.string), end=' ')
            # else:
            #     print(Fore.WHITE + str(tag.string))
            file.write(str(tag.string) + '\n')
        file.close()


while True:
    url_input = input()

    if url_input == 'exit':
        break
    elif '.' in url_input:
        get_content(url_input)
    else:
        print('Error: Incorrect URL')
