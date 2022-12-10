from dataclasses import dataclass
from typing import List, Tuple

import pprint

pp = pprint.PrettyPrinter(indent=2)


@dataclass
class WordSetInfo:
    source_name: str
    word_usages: list[tuple[str, int]]


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def sort_and_clean(dict):
    a = []

    for pair in sorted(dict.items(), key=lambda x: x[1], reverse=True):
        a.append(pair)

    return a


def get_words(filename):
    a = []

    for line in read_file(filename).splitlines():
        if not line:
            continue

        a += line.split(" ")

    return a


def analyse_file(filename) -> WordSetInfo:
    a = get_words(filename)

    common = {}

    for word in a:
        if word in common:
            common[word] += 1
        else:
            common[word] = 1

    # print(common)

    a = sort_and_clean(common)

    return WordSetInfo(source_name=filename, word_usages=a)


def combine(a1: WordSetInfo, a2: WordSetInfo) -> WordSetInfo:
    set1 = {}

    for pair in a1.word_usages:
        set1[pair[0]] = pair[1]

    for pair in a2.word_usages:
        if pair[0] in set1:
            set1[pair[0]] += pair[1]
        else:
            set1[pair[0]] = pair[1]

    combined = sort_and_clean(set1)

    return WordSetInfo(source_name='combined', word_usages=combined)


def main():
    a1 = analyse_file('data/data.txt')
    pp.pprint(a1)

    a2 = analyse_file('data/data2.txt')
    pp.pprint(a2)

    total = combine(a1, a2)

    pp.pprint(total)


if __name__ == '__main__':
    main()
