from aocd import data


def part_a(data):
    """n^2 solution"""
    entries = [int(s) for s in data.split('\n') if s != '']

    for i in range(len(entries)-1):
        for j in range(i, len(entries)):
            if entries[i] + entries[j] == 2020:
                return str(entries[i] * entries[j])

def part_b(data):
    entries = [int(s) for s in data.split('\n') if s != '']

    for i in range(len(entries)-2):
        for j in range(i, len(entries)-1):
            iplusj = entries[i] + entries[j]
            for k in range(j, len(entries)):
                if iplusj + entries[k] == 2020:
                    return str(entries[i] * entries[j] * entries[k])


test_data = """\
1721
979
366
299
675
1456
"""


if __name__ == "__main__":
    assert part_a(test_data) == "514579"
    assert part_b(test_data) == "241861950"
    print(part_a(data))
    print(part_b(data))
