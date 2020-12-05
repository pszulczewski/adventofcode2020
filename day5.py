import sys
from helpers import load_input


def split_row(rng, fb):
    le = len(rng)
    if fb == 'F':
        return rng[:le // 2]
    elif fb == 'B':
        return rng[le // 2:]
    else:
        print("Nor F or B")


def split_col(rng, rl):
    le = len(rng)
    if rl == 'L':
        return rng[:le // 2]
    elif rl == 'R':
        return rng[le // 2:]
    else:
        print("Nor R or L")


def calc_code(code):
    x = [x for x in range(128)]
    y = [y for y in range(8)]
    for i, char in enumerate(code[0:7]):
        if i == 0:
            row = split_row(x, char)
        else:
            row = split_row(row, char)

    for i, char in enumerate(code[7:10]):
        if i == 0:
            col = split_col(y, char)
        else:
            col = split_col(col, char)
    sid = row[0] * 8 + col[0]
    return row[0], col[0], sid


def highest_seat(codes):
    highest = int()
    for code in codes:
        _, _, sid = calc_code(code)
        if sid > highest:
            highest = sid
    return highest


def free_seat(codes):
    highest_code = 'BBFBBFFLRL'
    rows = range(0, 128)
    cols = range(8)
    for row in rows:
        r = format(row, '#09b')[2:].replace('0', 'F').replace('1', 'B')
        for col in cols:
            c = format(col, '#05b')[2:].replace('0', 'L').replace('1', 'R')
            code = r + c
            if code not in codes:
                print(code, calc_code(code))
            if code == highest_code:
                print(code, calc_code(code), 'Highest stop, previous is answer.')
                sys.exit()


if __name__ == '__main__':
    codes = load_input('input.txt')
    print('Highest seat is:', highest_seat(codes))
    free_seat(codes)
