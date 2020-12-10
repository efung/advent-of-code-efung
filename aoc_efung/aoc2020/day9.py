from aocd import data
import re


def part_a(data, pre_len=25):
    numbers = [int(s) for s in data.split('\n') if s != '']
    for i in range(pre_len, len(numbers[pre_len:])):
#        print("Checking {}".format(numbers[i]))
        preamble = numbers[i-pre_len:i]
#        print("\t Preamble  : {}".format(preamble))
        valids = [((numbers[i] - x) in [r for r in preamble if r != x]) for x in preamble]
#        print("\t Valids: {}".format(valids))
        if any(valids):
#            index = valids.index(True)
#            print("{} is valid = {} + {}".format(numbers[i], numbers[i] - preamble[index], preamble[index]))
            pass
        else:
#            print("{} is not valid".format(numbers[i]))
            return numbers[i]

def part_b(data, pre_len=25):
    invalid = part_a(data, pre_len)

    numbers = [int(s) for s in data.split('\n') if s != '']

    # Create a window of values to sum
    # Slide end of window forward while sum is too small
    # If sum too big, there is no window with the current start
    # Slide start forward, and grow window again
    start = 0
    end = start+1

    while end <= len(numbers):
        window = numbers[start:end]
        #print(window)
        s = sum(window)
        #print(s)
        if s == invalid:
            #print(window)
            return min(window) + max(window)
        elif s > invalid:
            start += 1
            end = start + 1
        else:
            end += 1

test_data_preamble_5 = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

if __name__ == "__main__":
    assert str(part_a(test_data_preamble_5, pre_len=5)) == "127"
    assert str(part_b(test_data_preamble_5, pre_len=5)) == "62"
    print(part_a(data))
    print(part_b(data))
