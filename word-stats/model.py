import os
import math
import random
import pprint
from dataclasses import dataclass
from typing import List

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
    txt_files = []

    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith('.txt'):
                file_path = os.path.join(root, f)

                txt_files.append(file_path)

    return txt_files


def percentage_swear_words(words: list[str]) -> float:
    swear_words = 0

    for word in words:
        if is_swear_word(word):
            swear_words += 1

    return swear_words / len(words)


def is_swear_word(word: str) -> bool:
    rand = math.floor(random.random() * 100)

    return rand > 50


def main():
    all = []

    for f in get_txt_files('data'):
        all.append(analyse_file(f))
        print(f)

    pp.pprint(all[0].word_usages[:10])

    print(percentage_swear_words(all[0].word_usages))


if __name__ == '__main__':
    main()
