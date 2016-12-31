from sys import exit
import os
import random

from inflect import engine

inflect = engine()

FILE_NAME = os.path.join(os.path.dirname(__file__), 'words.txt')


def manverbing():
    if not os.path.isfile(FILE_NAME):
        print('i dont have a wordlist to work from, please run the following:')
        print('python ./build_list.py | sort > {}'.format(FILE_NAME))
        exit(1)

    with open(FILE_NAME) as wf:
        words = [w.strip() for w in wf.readlines()]

    return 'Man{}'.format(inflect.present_participle(random.choice(words)))


if __name__ == '__main__':
    print(manverbing())
