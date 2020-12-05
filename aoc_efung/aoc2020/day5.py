from aocd import data


def get_row(chars):
    row = 0
    for i in range(len(chars)):
        j = len(chars)- i - 1
        if chars[i] == 'B': 
            jump = 2**j
            row += jump
    return row

def get_col(chars):
    col = 0
    for i in range(len(chars)):
        j = len(chars)- i - 1
        if chars[i] == 'R': 
            jump = 2**j
            col += jump
    return col

def part_a(data):
    entries = [s for s in data.split('\n') if s != '']
    high = -1
    for bpass in entries:
        row = get_row(bpass[0:7])
        col = get_col(bpass[7:10])
        seat_id = row*8 + col
        if seat_id > high:
            high = seat_id

    return str(high)

def part_b(data):
    entries = [s for s in data.split('\n') if s != '']
    seats = []
    for bpass in entries:
        row = get_row(bpass[0:7])
        col = get_col(bpass[7:10])
        seat_id = row*8 + col
        seats.append(seat_id)

    sorted_seats = sorted(seats)
    for i in range(0,len(sorted_seats)-1):
        if sorted_seats[i+1] != sorted_seats[i]+1:
            return sorted_seats[i+1]-1

test_data = """\
FBFBBFFRLR
"""


if __name__ == "__main__":
    assert part_a(test_data) == "357"
#    assert part_b(test_data) == ""
    print(part_a(data))
    print(part_b(data))
