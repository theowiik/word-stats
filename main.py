import os
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


def get_txt_files(directory: str) -> List[str]:
    file_list = os.listdir(directory)

    txt_files = [os.path.join(directory, f)
                 for f in file_list if f.endswith('.txt')]

    return txt_files


def main():
    all = []

    for f in get_txt_files('data'):
        all.append(analyse_file(f))

    pp.pprint(all)


if __name__ == '__main__':
    main()
