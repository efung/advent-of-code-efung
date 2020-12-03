from aocd import data
import re


def part_a(data):
    entries = [s for s in data.split('\n') if s != '']

    valid = 0
    for entry in entries:
        m = re.match(r'(\d+)-(\d+) (\w): (.*)', entry)
        mn = int(m.group(1))
        mx = int(m.group(2))
        (let, pwd) = m.group(3,4)
        t = re.findall(let, pwd)
        if mn <= len(t) <= mx:
            valid += 1

    return str(valid)

def part_b(data):
    entries = [s for s in data.split('\n') if s != '']
    valid = 0
    for entry in entries:
        m = re.match(r'(\d+)-(\d+) (\w): (.*)', entry)
        mn = int(m.group(1))
        mx = int(m.group(2))
        (let, pwd) = m.group(3,4)

        valid += 1 if (pwd[mn-1] == let) ^ (pwd[mx-1] == let) else 0

    return str(valid)

test_data = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


if __name__ == "__main__":
    assert part_a(test_data) == "2"
    assert part_b(test_data) == "1"
    print(part_a(data))
    print(part_b(data))
