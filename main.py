import pprint

pp = pprint.PrettyPrinter(indent=2)


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def sort_and_clean(dict):
    a = []

    for pair in sorted(dict.items(), key=lambda x: x[1], reverse=True):
        a.append(pair)

    return a


def analyse_file(filename):
    a = []

    for line in read_file('data/data.txt').splitlines():
        if not line:
            continue

        a += line.split(" ")

    common = {}

    for word in a:
        if word in common:
            common[word] += 1
        else:
            common[word] = 1

    # print(common)

    a = sort_and_clean(common)
    return a


def main():
    a1 = analyse_file('data/data.txt')
    pp.pprint(a1)

    a2 = analyse_file('data/data2.txt')
    pp.pprint(a2)


if __name__ == '__main__':
    main()
