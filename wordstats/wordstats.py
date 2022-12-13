import pprint
from wordstats.model import analyse_file, combine_all, count_per_year, get_txt_files

pp = pprint.PrettyPrinter(indent=2)

all = []

for f in get_txt_files('data'):
    w = analyse_file(f)
    all.append(w)

combined = combine_all(all)

crazy_amount = count_per_year(combined, ['crazy'])
crazy_amount_per_year = count_per_year(all, ['crazy'])

pp.pprint(crazy_amount_per_year)
