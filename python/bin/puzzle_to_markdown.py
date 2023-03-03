#!/usr/bin/env python3

import sys,requests
from bs4 import BeautifulSoup


def main(year, day):
    #URL='https://adventofcode.com/2022/day/1'
    #page = requests.get(URL)

    #soup = BeautifulSoup(page.content, 'html.parser')
    soup = BeautifulSoup(open('puzzle.html'), 'html.parser')

    for elem in soup.find('article', class_='day-desc'):
        #TODO: implement 'ul'
        if elem.name == 'h2':
            print(f'## {elem.contents[0]}', end="")
        elif elem.name == 'p':
            for x in elem.contents:
                try:
                    print(x.contents[0], end="")
                except AttributeError:
                    print(x, end="")
        elif elem.name == 'pre':
            print('```')
            print(elem.find('code').contents[0], end="")
            print('```', end="")
        else:
            continue

        print()
        print()

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print(f'Usage: {sys.argv[0]} YEAR DAY')
