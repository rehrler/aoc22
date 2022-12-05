import numpy as np


def read_stacks():
    file1 = open('data/day05_1.txt', 'r')
    lines = file1.readlines()
    spaces = np.arange(1, 34, 4)
    stack = []
    for i in range(len(spaces)):
        stack.append([])
    for line in lines:
        for idx, pos in enumerate(spaces):
            poss_item = line[pos]
            if poss_item != " ":
                stack[idx].append(poss_item)
    for i in range(len(spaces)):
        stack[i].reverse()
    return stack


def read_moves():
    file = open('data/day05_2.txt', 'r')
    lines = file.readlines()
    moves = []
    for line in lines:
        separated = line.split(" ")
        move = [int(separated[1]), int(separated[3]), int(separated[5])]
        moves.append(move)
    return moves


def part1():
    stacks = read_stacks()
    moves = read_moves()
    for move in moves:
        for i in range(move[0]):
            out = stacks[move[1] - 1].pop()
            stacks[move[2] - 1].append(out)
    top_items = ""
    for i in range(len(stacks)):
        top_items += stacks[i].pop()
    print(f"top items in stack: {top_items}")


def part2():
    stacks = read_stacks()
    moves = read_moves()
    for move in moves:
        new_in = []
        for i in range(move[0]):
            out = stacks[move[1] - 1].pop()
            new_in.append(out)
        new_in.reverse()
        for new in new_in:
            stacks[move[2] - 1].append(new)
    top_items = ""
    for i in range(len(stacks)):
        top_items += stacks[i].pop()
    print(f"top items in stack: {top_items}")


if __name__ == "__main__":
    part1()
    part2()
