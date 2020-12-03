from aocd import data
from functools import reduce


def part_a_work(maprows, delta_x, delta_y):
    m = len(maprows)       # rows
    n = len(maprows[0])    # columns
#    print("{} x {}".format(m,n))

    x = y = 0
    trees = 0

    while y < m:
#        print( "({},{})".format(x, y), end='')
        x = (x + delta_x) % n
        y = (y + delta_y)
        if (y < m) and (maprows[y][x] == '#'):
            trees += 1
#            print(" #", end='')
#        print()


    return str(trees)

def part_a(data):
    maprows = [s for s in data.split('\n') if s != '']
    return part_a_work(maprows, delta_x = 3, delta_y = 1)

def part_b(data):
    maprows = [s for s in data.split('\n') if s != '']
    x = []
    x.append(part_a_work(maprows, 1, 1))
    x.append(part_a_work(maprows, 3, 1))
    x.append(part_a_work(maprows, 5, 1))
    x.append(part_a_work(maprows, 7, 1))
    x.append(part_a_work(maprows, 1, 2))
    #print(x)

    return str(reduce(lambda x,y: x*y, map(int, x)))


test_data = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


if __name__ == "__main__":
    assert part_a(test_data) == "7"
    assert part_b(test_data) == "336"
    print(part_a(data))
    print(part_b(data))
