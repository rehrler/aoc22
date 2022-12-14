import numpy as np


def read_data():
    lines = open("data/day14.txt", "r").read().split("\n")
    field = np.zeros((1000, 1000))
    for line in lines:
        lins = line.split(" -> ")
        for k in np.arange(0, len(lins) - 1, 1):
            start_point, end_point = lins[k].split(","), lins[k + 1].split(",")
            start_point = [int(number) for number in start_point]
            start_point = [int(number) for number in start_point]
            end_point = [int(number) for number in end_point]
            if start_point[0] == end_point[0]:  # horizontal line
                if start_point[1] < end_point[1]:
                    for i in np.arange(start_point[1], end_point[1] + 1, 1):
                        field[i, start_point[0]] = 1
                elif start_point[1] > end_point[1]:
                    for i in np.arange(end_point[1], start_point[1] + 1, 1):
                        field[i, start_point[0]] = 1
                else:
                    raise ValueError("invalid line")
            elif start_point[1] == end_point[1]:  # vertical line
                if start_point[0] < end_point[0]:
                    for j in np.arange(start_point[0], end_point[0] + 1, 1):
                        field[start_point[1], j] = 1
                elif start_point[0] > end_point[0]:
                    for j in np.arange(end_point[0], start_point[0] + 1, 1):
                        field[start_point[1], j] = 1
                else:
                    raise ValueError("invalid line")
            else:
                raise ValueError("invalid line")
    return field


def find_lowest_row(field):
    lowest_row = 0
    for i in range(np.shape(field)[0]):
        if np.any(field[i]) == 1:
            lowest_row = i
    return lowest_row


def add_sand_unit(field, lowest_row):
    curr_pos = [0, 500]
    new_pos = [0, 500]
    standstill = False
    while not standstill:
        if (
            field[curr_pos[0] + 1, curr_pos[1]] != -1
            and field[curr_pos[0] + 1, curr_pos[1]] != 1
        ):  # down
            new_pos = [curr_pos[0] + 1, curr_pos[1]]
        else:
            if (
                field[curr_pos[0] + 1, curr_pos[1] - 1] != -1
                and field[curr_pos[0] + 1, curr_pos[1] - 1] != 1
            ):  # left
                new_pos = [curr_pos[0] + 1, curr_pos[1] - 1]
            else:
                if (
                    field[curr_pos[0] + 1, curr_pos[1] + 1] != -1
                    and field[curr_pos[0] + 1, curr_pos[1] + 1] != 1
                ):  # right
                    new_pos = [curr_pos[0] + 1, curr_pos[1] + 1]
        if new_pos[0] == curr_pos[0] and new_pos[1] == curr_pos[1]:
            field[new_pos[0], new_pos[1]] = -1
            standstill = True
        else:
            curr_pos = new_pos
        if curr_pos[0] > lowest_row:
            return field, False
    if curr_pos[0] == 0 and curr_pos[1] == 500:
        return field, False
    else:
        return field, True


def sim_sand(field):
    lowest_row = find_lowest_row(field)
    sand_units = 0
    next_sand = True
    while next_sand:
        field, next_sand = add_sand_unit(field, lowest_row)
        if next_sand:
            sand_units += 1
    return sand_units


def add_inf_line(field):
    lowest_row = find_lowest_row(field)
    for j in range(np.shape(field)[1]):
        field[lowest_row + 2, j] = 1
    return field


def part1_2():
    # part 1
    field = read_data()
    sand_units = sim_sand(field)
    print(f"sand units: {sand_units}")
    # part 2
    field = read_data()
    field = add_inf_line(field)
    sand_units = sim_sand(field) + 1
    print(f"sand units: {sand_units}")
    return 0


if __name__ == "__main__":
    part1_2()
