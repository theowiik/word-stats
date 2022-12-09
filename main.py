def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

a = []
for line in read_file('data/data.txt').splitlines():
    if not line: continue

    a += line.split(" ")

common = {}

for word in a:
    if word in common:
        common[word] += 1
    else:
        common[word] = 1

print(common)
