from helpers import load_input


def incorrect(puzzle):
    for i in range(25, len(puzzle)):
        prev = puzzle[i-25:i]
        ok = False
        for a in range(25):
            for b in range(25):
                if a != b and prev[a] + prev[b] == puzzle[i]:
                    ok = True
        if not ok:
            return puzzle[i]


def sum_of(puzzle, found):
    for i in range(len(puzzle)):
        for j in range(i, len(puzzle)):
            rng = puzzle[i:j]
            if sum(rng) == found:
                return min(rng) + max(rng)


if __name__ == '__main__':
    p = load_input('input.txt')
    puzzle = [int(x) for x in p.splitlines()]
    found = incorrect(puzzle)
    print(found)
    print(sum_of(puzzle, found))
