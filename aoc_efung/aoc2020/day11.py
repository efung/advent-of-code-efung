from aocd import data
from asciimatics.screen import ManagedScreen
from time import sleep
import re
import copy


def occupied(r, c, layout):
    """Return number of occupied seats immediately adjacent to seat (r,c)."""
    occupy = 0

    NW = (-1, -1)
    NE = (-1,  1)
    N  = (-1,  0)
    W  = (0,  -1)
    E  = (0,   1)
    SW = (1,  -1)
    SE = (1,   1)
    S  = (1,   0)

    for dirs in [NW, NE, N, W, E, SW, SE, S]:
        dr, dc = r+dirs[0], c + dirs[1]
        if (dr >= 0) and (dc >= 0) and (dr < len(layout)) and (dc < len(layout[0])):
            if layout[dr][dc] == '#':
                occupy += 1

    return occupy


VISUALIZE = False
def display(layout):
    with ManagedScreen() as screen:
        for r in range(0, len(layout)):
            for c in range(0, len(layout[0])):
                screen.print_at(layout[r][c], r, c)

        screen.refresh()
        sleep(0.8)

def part_a(data):
    initial = [list(r) for r in data.split('\n') if r != '']
    layout_new = copy.deepcopy(initial)

    if VISUALIZE:
        display(layout_new)

    changed = True
    while changed:
        changed = False
        layout = copy.deepcopy(layout_new)
        for r in range(0, len(layout)):
            for c in range(0, len(layout[0])):
                if layout[r][c] == 'L' and occupied(r, c, layout) == 0:
                    layout_new[r][c] = '#'
                    changed = True
                elif layout[r][c] == '#' and occupied(r, c, layout) >= 4:
                    layout_new[r][c] = 'L'
                    changed = True

        if VISUALIZE:
            display(layout_new)

    return len(re.findall('#', ''.join([str(s) for s in layout_new])))

def occupied_first(r, c, layout):
    """Return number of occupied seats seen from seat (r,c)."""
    occupy = 0

    NW = (-1, -1)
    NE = (-1,  1)
    N  = (-1,  0)
    W  = (0,  -1)
    E  = (0,   1)
    SW = (1,  -1)
    SE = (1,   1)
    S  = (1,   0)

    for dirs in [NW, NE, N, W, E, SW, SE, S]:
        dr, dc = r+dirs[0], c + dirs[1]
        while (dr >= 0) and (dc >= 0) and (dr < len(layout)) and (dc < len(layout[0])):
            if layout[dr][dc] == '#':
                occupy += 1
                break
            elif layout[dr][dc] == 'L':
                break
            dr, dc = dr+dirs[0], dc + dirs[1]

    return occupy

def part_b(data):
    initial = [list(r) for r in data.split('\n') if r != '']
    layout_new = copy.deepcopy(initial)

    if VISUALIZE:
        display(layout_new)

    changed = True
    while changed:
        changed = False
        layout = copy.deepcopy(layout_new)
        for r in range(0, len(layout)):
            for c in range(0, len(layout[0])):
                if layout[r][c] == 'L' and occupied_first(r, c, layout) == 0:
                    layout_new[r][c] = '#'
                    changed = True
                elif layout[r][c] == '#' and occupied_first(r, c, layout) >= 5:
                    layout_new[r][c] = 'L'
                    changed = True

        if VISUALIZE:
            display(layout_new)

    return len(re.findall('#', ''.join([str(s) for s in layout_new])))

test_data = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

if __name__ == "__main__":
    assert part_a(test_data) == 37
    print(part_a(data))

    assert part_b(test_data) == 26
    print(part_b(data))
