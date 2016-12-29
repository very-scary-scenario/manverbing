import re

from nltk.corpus import wordnet


def get_words():
    words = set()

    for synset in wordnet.all_synsets(wordnet.VERB):
        for name in (l.name() for l in synset.lemmas() if all((
            l.count() > 0,
            re.search(r'^[a-z]+$', l.name()),
        ))):
            words.add(name)

    return words


if __name__ == '__main__':
    for word in get_words():
        print(word)
