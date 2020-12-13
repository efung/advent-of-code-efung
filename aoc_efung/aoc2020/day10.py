from aocd import data
import re
from functools import reduce


def part_a(data):
    raw = [int(j) for j in data.split('\n') if j != '']
    adapters = [0] +  sorted(raw) + [max(raw) + 3]

    diffs = [adapters[i+1] - adapters[i] for i in range(len(adapters)-1)]
    #print(diffs)

    diff_1jolt = len(list(filter(lambda x : x == 1, diffs)))
    diff_3jolt = len(list(filter(lambda x : x == 3, diffs)))

    return str(diff_1jolt * diff_3jolt)

tribonacci_memo = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
def tribonacci(n):
    if n in tribonacci_memo.keys():
        return tribonacci_memo[n]
    else:
        cnt = tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
        tribonacci_memo[n] = cnt
        return cnt

def part_b(data):
    raw = [int(j) for j in data.split('\n') if j != '']
    adapters = [0] +  sorted(raw) + [max(raw) + 3]

    diffs = [adapters[i+1] - adapters[i] for i in range(len(adapters)-1)]

    # Note that different arrangements arise by omitting
    # one or more adapters in a sequence of two or more adapters 
    # that differ by 1. This is equivalent to counting how many 
    # ways there are to express (1 + 1 + … + 1) as a sum of 
    # integers where each part is in (1,2,3)
    #
    # For example, if there are four adapters that differ by 1:
    #        x  x+1  x+2  x+3
    # diff    1    1    1
    # We can "skip" the adapter by omitting it, which yields
    # differences such as:
    # a)     x       x+2  x+3
    #  diff   2         1
    # b)     x  x+1       x+3
    #  diff   1         2
    # c)     x            x+3
    #  diff             3
    #
    # These look like partitions of (1+1+…+1) where the components
    # can be at most 3.
    #
    # After much searching, I learned that partitions of an 
    # integer where order matters, is called a composition.
    # And by restricting the parts of the composition to
    # be at most a number k, results in the generalized
    # Fibonacci numbers.
    # 
    # https://math.stackexchange.com/questions/3055314/number-of-compositions-of-n-such-that-each-term-is-less-than-equal-to-k
    #
    # So, the number of compositions of n, where the integers
    # are at most 3 is given by the tribonacci numbers
    #
    # T(n) = T(n-1) + T(n-2) + T(n-3)

    # First, we need to count how many runs of 1s there are. 
    # Take the differences, combine into a single string,
    # Use regexes to extract the runs of 1s.

    diff_str = ''.join([str(d) for d in diffs])

    runs_of_1 = re.findall('11+', diff_str)

    trib = list(map(lambda r: tribonacci(len(r)), runs_of_1))

    return str( reduce(lambda x, y: x*y, trib) )

test_data = """\
16
10
15
5
1
11
7
19
6
12
4
"""

test_data_b = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3

"""

if __name__ == "__main__":
    assert part_a(test_data) == "35"
    assert part_a(test_data_b) == "220"
    print(part_a(data))
    assert part_b(test_data) == "8"
    assert part_b(test_data_b) == "19208"
    print(part_b(data))
