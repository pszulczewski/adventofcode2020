import re
from collections import defaultdict
from helpers import load_input


def map_colors(puzzle):
    color_map = defaultdict(dict)
    all_collors = set()
    for rule in puzzle.splitlines():
        color = re.match(r'\w+ \w+', rule).group(0)
        if color != 'shiny gold':
            all_collors.add(color)
        contains = re.findall(r'(\d+) (\w+ \w+)', rule)
        for count, col in contains:
            if col != 'shiny gold':
                all_collors.add(col)
            color_map[color][col] = count
    return color_map, all_collors


def colors_with_gold_bag(all_colors, color_map):
    found_gold = set()
    for color in all_colors:
        def contains_gold(n_color):
            next_colors = color_map.get(n_color)
            if next_colors:
                if next_colors.get('shiny gold'):
                    return True
                else:
                    for nex_col in next_colors:
                        ok = contains_gold(nex_col)
                        if ok:
                            return ok

        success = contains_gold(color)
        if success:
            found_gold.add(color)

    return len(found_gold)


def map_colors2(puzzle):
    color_map = defaultdict(dict)
    for rule in puzzle.splitlines():
        color = re.match(r'\w+ \w+', rule).group(0)
        contains = re.findall(r'(\d+) (\w+ \w+)', rule)
        for count, col in contains:
            color_map[color][col] = count
    return color_map


def count_with_gold_bag(color_map):
    count_gold = 0
    for color, count in color_map.get('shiny gold').items():
        def get_next(n_color):
            count_ = 1
            next_colors = color_map.get(n_color)
            if next_colors:
                for nex_col, nex_count in next_colors.items():
                    count_ += int(nex_count) * get_next(nex_col)
            return count_
        count_gold += int(count) * get_next(color)
    return count_gold


if __name__ == '__main__':
    puzzle = load_input('input.txt')
    map1, all_ = map_colors(puzzle)
    print(colors_with_gold_bag(all_, map1))
    map2 = map_colors2(puzzle)
    print(count_with_gold_bag(map2))
