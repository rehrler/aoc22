import numpy as np


def read_data():
    file = open("data/day09.txt", "r")
    lines = file.readlines()
    commands = []
    for line in lines:
        splitted_str = line.split(" ")
        commands.append([splitted_str[0], int(splitted_str[1])])
    return commands


def move_h(step, direction, h_pos):
    if direction == "U":
        return [h_pos[0] - step, h_pos[1]]
    elif direction == "D":
        return [h_pos[0] + step, h_pos[1]]
    elif direction == "L":
        return [h_pos[0], h_pos[1] - step]
    elif direction == "R":
        return [h_pos[0], h_pos[1] + step]
    else:
        raise ValueError(f"{direction} is not a valid direction")


def move_t(h_pos, t_pos):
    diff_i, diff_j = t_pos[0] - h_pos[0], t_pos[1] - h_pos[1]
    # case touching
    if diff_i == 0 and diff_j == 0:  # case overlaying
        return t_pos
    elif abs(diff_i) + abs(diff_j) == 1:  # case up, down, right, left by 1
        return t_pos
    elif (
        (diff_i == 1 and diff_j == 1)
        or (diff_i == 1 and diff_j == -1)
        or (diff_i == -1 and diff_j == -1)
        or (diff_i == -1 and diff_j == 1)
    ):  # case diagonal
        return t_pos
    # case need to move
    if diff_i == -2 and diff_j == 0:  # case h 2 down
        return [t_pos[0] + 1, t_pos[1]]
    elif diff_i == 0 and diff_j == -2:  # case h 2 right
        return [t_pos[0], t_pos[1] + 1]
    elif diff_i == 2 and diff_j == 0:  # case h 2 up
        return [t_pos[0] - 1, t_pos[1]]
    elif diff_i == 0 and diff_j == 2:  # case h 2 left
        return [t_pos[0], t_pos[1] - 1]
    elif diff_i == -2 and diff_j == -1:  # case h 2 down 1 right
        return [t_pos[0] + 1, t_pos[1] + 1]
    elif diff_i == -1 and diff_j == -2:  # case h 1 down 2 right
        return [t_pos[0] + 1, t_pos[1] + 1]
    elif diff_i == 1 and diff_j == -2:  # case h 1 up 2 right
        return [t_pos[0] - 1, t_pos[1] + 1]
    elif diff_i == 2 and diff_j == -1:  # case h 2 up 1 right
        return [t_pos[0] - 1, t_pos[1] + 1]
    elif diff_i == 2 and diff_j == 1:  # case h 2 up 1 left
        return [t_pos[0] - 1, t_pos[1] - 1]
    elif diff_i == 1 and diff_j == 2:  # case h 1 up 2 left
        return [t_pos[0] - 1, t_pos[1] - 1]
    elif diff_i == -1 and diff_j == 2:  # case h 1 down 2 left
        return [t_pos[0] + 1, t_pos[1] - 1]
    elif diff_i == -2 and diff_j == 1:  # case h 2 down 1 right
        return [t_pos[0] + 1, t_pos[1] - 1]
    # extra case for part 2
    elif diff_i == -2 and diff_j == -2:  # case h 2 down 2 right
        return [t_pos[0] + 1, t_pos[1] + 1]
    elif diff_i == 2 and diff_j == -2:  # case h 2 up 2 right
        return [t_pos[0] - 1, t_pos[1] + 1]
    elif diff_i == 2 and diff_j == 2:  # case h 2 up 2 left
        return [t_pos[0] - 1, t_pos[1] - 1]
    elif diff_i == -2 and diff_j == 2:  # case h 2 down 2 left
        return [t_pos[0] + 1, t_pos[1] - 1]
    else:
        raise ValueError("impossible move")


def part1_2():
    commands = read_data()
    field = np.zeros((400, 400))
    h_pos, t_pos = [200, 200], [200, 200]
    field[t_pos[0], t_pos[1]] = 1
    for command in commands:
        for step in range(command[1]):
            h_pos = move_h(1, command[0], h_pos)
            t_pos = move_t(h_pos, t_pos)
            field[t_pos[0], t_pos[1]] = 1
    unique, counts = np.unique(field, return_counts=True)
    counter = dict(zip(unique, counts))
    print(f"visited fields by knot T: {counter[1]}")

    h_pos = [200, 200]
    knots = []
    for i in range(9):
        knots.append([200, 200])
    field = np.zeros((400, 400))
    field[h_pos[0], h_pos[1]] = 1
    for command in commands:
        for step in range(command[1]):
            h_pos = move_h(1, command[0], h_pos)
            new_knots = []
            for idx, knot in enumerate(knots):
                if idx == 0:
                    new_knot = move_t(h_pos, knot)
                    new_knots.append(new_knot)
                elif idx == len(knots) - 1:
                    new_knot = move_t(new_knots[idx - 1], knot)
                    new_knots.append(new_knot)
                    field[new_knot[0], new_knot[1]] = 1
                else:
                    new_knot = move_t(new_knots[idx - 1], knot)
                    new_knots.append(new_knot)
            knots = new_knots

    unique, counts = np.unique(field, return_counts=True)
    counter = dict(zip(unique, counts))
    print(f"visited fields by knot 9: {counter[1]}")


if __name__ == "__main__":
    part1_2()
