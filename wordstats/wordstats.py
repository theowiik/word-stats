import pprint
from model import get_txt_files, analyse_file, combine_all, count_per_year, count

pp = pprint.PrettyPrinter(indent=2)

def main():
    all = []
    for f in get_txt_files('data'):
        w = analyse_file(f)
        all.append(w)

    combined = combine_all(all)

    sortd = combined.get_sorted_word_usage_list()
    pp.pprint(sortd[0:100])

    perfect_amount = count(combined, ['perfect'])
    perfect_amount_per_year = count_per_year(all, ['perfect'])

    print(perfect_amount)
    pp.pprint(perfect_amount_per_year)

if __name__ == '__main__':
    main()
