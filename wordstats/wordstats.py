import pprint
from model import get_txt_files, analyse_file, combine_all, count_per_year, count
from view import create_bar_plot, create_line_plot

pp = pprint.PrettyPrinter(indent=2)


def main():
    # Parse data
    a = get_data()

    combined = combine_all(a)

    sortd = combined.get_sorted_word_usage_list()

    perfect_amount = count(combined, ['perfect'])
    perfect_amount_per_year = count_per_year(a, ['perfect'])

    pp.pprint(perfect_amount_per_year)

    # Plot most used words
    labels_most_used = [x[0]
                        for x in combined.get_sorted_word_usage_list()[0:15]]
    values_most_used = [x[1]
                        for x in combined.get_sorted_word_usage_list()[0:15]]

    # create_bar_plot(labels_most_used, values_most_used).show()

    # Plot most used words over time
    labels_over_time = [label for label in perfect_amount_per_year.keys()]
    values_over_time = [value for value in perfect_amount_per_year.values()]

    # create_line_plot(labels_over_time, values_over_time).show()


def get_data():
    a = []

    for f in get_txt_files('wordstats/data'): # TODO: Make this a parameter
        w = analyse_file(f)
        a.append(w)

    return a


if __name__ == '__main__':
    main()
