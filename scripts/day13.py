import ast

import numpy as np


def read_data():
    lines = open("data/day13.txt", "r").read().split("\n")
    pairs = []
    pair = []
    for line in lines:
        if line == "":
            pairs.append(pair)
            pair = []
        else:
            pair.append(ast.literal_eval(line))
    return pairs


def check_order(value1, value2):
    if type(value1) == int and type(value2) == int:
        if value1 < value2:
            return False, 1
        elif value2 < value1:
            return False, 0
        else:
            return True, -1
    elif type(value1) == list and type(value2) == list:
        for i in range(len(value1)):
            if i < len(value2):
                bol, res = check_order(value1[i], value2[i])
                if not bol:
                    return False, res
            else:
                return False, 0
        if len(value1) < len(value2):
            return False, 1
        else:
            return True, -1

    elif type(value1) == int and type(value2) == list:
        return check_order([value1], value2)
    elif type(value1) == list and type(value2) == int:
        return check_order(value1, [value2])


def bubble_sort(my_list: list):
    n = len(my_list)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            bol, res = check_order(my_list[j], my_list[j + 1])
            if res == 0:
                swapped = True
                my_list = swap(my_list, j, j + 1)
        if not swapped:
            return


def swap(a_list, pos1, pos2):
    a_list[pos1], a_list[pos2] = a_list[pos2], a_list[pos1]
    return a_list


def part1_2():
    pairs = read_data()
    correct_order = 0
    list_of_correct_idx = []
    for idx, pair in enumerate(pairs):
        cont, res = check_order(pair[0], pair[1])
        correct_order += res
        if res == 1:
            list_of_correct_idx.append(idx + 1)
    print(f"sum of correct pair idx: {np.sum(list_of_correct_idx)}")

    pair_list = []
    for i in range(len(pairs)):
        pair_list.append(pairs[i][0])
        pair_list.append(pairs[i][1])
    pair_list.append([[2]])
    pair_list.append([[6]])
    bubble_sort(pair_list)
    idx_2, idx_6 = None, None
    for i in range(len(pair_list)):
        if pair_list[i] == [[2]]:
            idx_2 = i + 1
        if pair_list[i] == [[6]]:
            idx_6 = i + 1
    print(f"decoder key: {idx_2 * idx_6}")
    return 0


if __name__ == "__main__":
    part1_2()
