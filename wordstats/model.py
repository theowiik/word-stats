import os
import math
import random
import pprint
import re
from dataclasses import dataclass
from typing import List

pp = pprint.PrettyPrinter(indent=2)


@dataclass
class WordSetInfo:
    source_name: str
    word_usages: dict[str, int]
    year: int | None = None

    def get_sorted_word_usage_list(self) -> list[tuple[str, int]]:
        a = []

        for pair in sorted(self.word_usages.items(), key=lambda x: x[1], reverse=True):
            a.append(pair)

        return a


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def get_cleaned_words(filename):
    a = []

    for line in read_file(filename).splitlines():
        if not line:
            continue

        cleaned_strings = [clean_string(word)
                           for word in line.split(" ") if word]

        a += [word for word in cleaned_strings if word]

    return a


def clean_string(string):
    string = re.sub(r"[.,!?\"\'()–—’‘”“-]", '', string)
    return string.lower().strip()


def analyse_file(filename) -> WordSetInfo:
    a = get_cleaned_words(filename)

    word_usages = {}

    for word in a:
        if word in word_usages:
            word_usages[word] += 1
        else:
            word_usages[word] = 1

    year_string = [x for x in filename.split('\\') if x.startswith('year_')]
    year = None

    if len(year_string) > 0:
        try:
            year = int(year_string[0].split('_')[1])
        except ValueError:
            raise ValueError(
                f"Invalid year in filename: '{filename}', should be 'year_YYYY'")

    return WordSetInfo(
        source_name=filename,
        word_usages=word_usages,
        year=year
    )


def combine(word_set_1: WordSetInfo, word_set_2: WordSetInfo) -> WordSetInfo:
    new_dict = {}

    w_usage_1 = word_set_1.word_usages
    w_usage_2 = word_set_2.word_usages

    for key, value in w_usage_1.items():
        new_dict[key] = value

    for key, value in w_usage_2.items():
        if key in new_dict:
            new_dict[key] += value
        else:
            new_dict[key] = value

    return WordSetInfo(source_name='combined', word_usages=new_dict)


def combine_all(a) -> WordSetInfo:
    if len(a) == 0:
        return WordSetInfo(source_name='empty', word_usages={})
    if len(a) == 1:
        return WordSetInfo(source_name='combined', word_usages=a[0].word_usages)

    combined = combine(a[0], a[1])

    for i in range(2, len(a)):
        combined = combine(combined, a[i])

    return combined


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


def count(word_set, words_to_count):
    words_as_set = set(words_to_count)
    count = 0

    ordered_usage = word_set.get_sorted_word_usage_list()

    only_words = [word[0] for word in ordered_usage]

    for word in words_as_set:
        if word in only_words:
            count += word_set.word_usages[word]

    return count

def count_per_year(word_info_sets, words_to_count):
    output = {}

    for word_info in word_info_sets:
        if word_info.year is None:
            continue

        if word_info.year not in output:
            output[word_info.year] = count(word_info, words_to_count)
        else:
            output[word_info.year] += count(word_info, words_to_count)

    return output

def main():
    all = []

    for f in get_txt_files('data'):
        w = analyse_file(f)
        all.append(w)

    combined = combine_all(all)

    sortd = combined.get_sorted_word_usage_list();
    pp.pprint(sortd[0:100])

    perfect_amount = count(combined, ['perfect'])
    perfect_amount_per_year = count_per_year(all, ['perfect'])


if __name__ == '__main__':
    main()
