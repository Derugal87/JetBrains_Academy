from bs4 import BeautifulSoup
import requests
import sys

args = sys.argv

languages = ['Arabic',
             'German',
             'English',
             'Spanish',
             'French',
             'Hebrew',
             'Japanese',
             'Dutch',
             'Polish',
             'Portuguese',
             'Romanian',
             'Russian',
             'Turkish']


if args[1].capitalize() in languages:
    if args[2].capitalize() in languages:
        language = args[1].capitalize()
        to_language = args[2].capitalize()

        _word = args[3]
        url = "https://context.reverso.net/translation/"

        r = requests.get(f'{url}{language.lower()}-{to_language.lower()}/{_word}', headers={'User-Agent': 'Mozilla/5.0'})
        print(str(r.status_code) + ' ' + 'OK')
        soup = BeautifulSoup(r.content, 'html.parser')
        words = [i.text.strip('\n " "') for i in soup.find_all('a', {'class': "translation"})]
        phrases_list = [(i.text.strip('\n " " []')) for i in soup.select("#examples-content .text")]

        print(f'{to_language} Translations:')
        print("\n".join(i for i in words[1:6]))
        print(f'\n{to_language} Examples:')
        for i in range(0, 10, 2):
            print(":\n".join(i for i in phrases_list[i:i + 2]))
            print()
    elif args[2] == 'all':
        language = args[1].capitalize()

        _word = args[3]
        url = "https://context.reverso.net/translation/"

        languages.remove(language)

        with open(f'{_word}.txt', 'a') as file:
            for i in languages:
                r = requests.get(f'{url}{language.lower()}-{i.lower()}/{_word}',
                                     headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(r.content, 'html.parser')
                words = [i.text.strip('\n " "') for i in soup.find_all('a', {'class': "translation"})]
                phrases_list = [(i.text.strip('\n " " []')) for i in soup.select("#examples-content .text")]
                print(f'{i} Translations:')
                file.write('\n')
                file.write(f'{i} Translations:\n')
                print("\n".join(i for i in words[1:2]))
                file.writelines("\n".join(i for i in words[1:2]))
                file.write('\n')
                print(f'\n{i} Examples:')
                file.write(f'\n{i} Examples:\n')
                file.write('')
                for i in range(0, 1):
                    print(":\n".join(i for i in phrases_list[i:i + 2]))
                    file.write(":\n".join(i for i in phrases_list[i:i + 2]))
                    print()
                    file.write('\n')
else:
    print('Unable choose')

