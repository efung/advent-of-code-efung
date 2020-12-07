from aocd import data
from collections import defaultdict

def part_a(data):
    groups = data.split('\n\n')
    yeses = list(map(lambda group: len( dict.fromkeys(group.replace('\n','')) ), groups))
    return str( sum(yeses) )

def part_b(data):
    groups = data.split('\n\n')
    everyone = []
    for group in groups:
        g = group.strip()
        size = len(g.split('\n'))
        yeses = defaultdict(lambda: 0)
        for v in g.replace('\n',''):
            yeses[v] += 1
        all_agreed = len(list(filter(lambda x: x == size, yeses.values())))
        everyone.append(all_agreed)

    return str( sum(everyone) )

test_data = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""

if __name__ == "__main__":
    assert part_a(test_data) == "11"
    assert part_b(test_data) == "6"
    print(part_a(data))
    print(part_b(data))
