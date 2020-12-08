import sys
from helpers import load_input


def run(codes):
    index = 0
    acc_value = 0
    indexes = []
    while index <= len(codes):
        try:
            inst, step = codes[index].split()
        except IndexError:
            print('END\n')
            return acc_value
        if index not in indexes:
            indexes.append(index)
        else:
            print(f"Loop!, last acc: {acc_value}\n")
            return False
        if inst == 'nop': index = index + 1
        elif inst == 'acc':
            acc_value += int(step)
            index = index + 1
        elif inst == 'jmp': index = index + int(step)


def replace_try(codes):
    tested = []
    x = False
    while not x:
        for i, code in enumerate(codes):
            if 'jmp' in code and i not in tested:
                new = codes.copy()
                new[i] = code.replace('jmp', 'nop')
                tested.append(i)
                x = run(new)
                if x:
                    print('ACC:', x)
                    break
        break


if __name__ == '__main__':
    codes = load_input('input.txt').splitlines()
    print(run(codes))
    print('-'*120)
    replace_try(codes)
