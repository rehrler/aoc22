import numpy as np


def read_data():
    with open("data/day12.txt", "r").read().split("\n") as lines:
        field = []
        for line in lines:
            new_row = [ord(char) - 96 for char in line]
            field.append(new_row)
        new_field = np.zeros((len(field), len(field[0])))
        for i in range(len(field)):
            for j in range(len(field[0])):
                new_field[i, j] = field[i][j]
        return new_field


def get_node(field, node: int):
    for i in range(np.shape(field)[0]):
        for j in range(np.shape(field)[1]):
            if field[i, j] == node:
                return i, j


def lca(field, start_row, start_col, end_row, end_col):
    # step 0
    open_bin = [(start_row, start_col)]
    distance = np.full(np.shape(field), fill_value=1000000000)
    distance[start_row, start_col] = 0
    while len(open_bin) != 0:
        current_node = open_bin.pop()
        for neighbour_node in [
            (current_node[0] + 1, current_node[1]),
            (current_node[0] - 1, current_node[1]),
            (current_node[0], current_node[1] + 1),
            (current_node[0], current_node[1] - 1),
        ]:
            if (
                0 <= neighbour_node[0] < np.shape(field)[0]
                and 0 <= neighbour_node[1] < np.shape(field)[1]
            ):
                if (
                    field[neighbour_node[0], neighbour_node[1]]
                    - field[current_node[0], current_node[1]]
                    < 2
                ):
                    if (
                        distance[current_node[0], current_node[1]] + 1
                        < distance[neighbour_node[0], neighbour_node[1]]
                    ) and (
                        distance[current_node[0], current_node[1]] + 1
                        < distance[end_row, end_col]
                    ):
                        distance[neighbour_node[0], neighbour_node[1]] = (
                            distance[current_node[0], current_node[1]] + 1
                        )
                        if (
                            neighbour_node[0] == end_row
                            and neighbour_node[1] == end_col
                        ):
                            continue
                        else:
                            open_bin.append((neighbour_node[0], neighbour_node[1]))
    return distance[end_row, end_col]


def get_all_starts(field):
    starts = []
    for i in range(np.shape(field)[0]):
        for j in range(np.shape(field)[1]):
            if field[i, j] == 1:
                starts.append((i, j))
    return starts


def part1_2():
    field = read_data()
    (start_row, start_col) = get_node(field, -13)
    (end_row, end_col) = get_node(field, -27)
    field[start_row, start_col] = 1
    field[end_row, end_col] = 27
    short_dist = lca(field, start_row, start_col, end_row, end_col)
    print(f"shortest distance: {short_dist}")

    poss_shortest_dist = []
    poss_starts = get_all_starts(field)
    for poss_start in poss_starts:
        short_dist = lca(field, poss_start[0], poss_start[1], end_row, end_col)
        poss_shortest_dist.append(short_dist)
    poss_shortest_dist.sort()
    print(f"shortest distance: {poss_shortest_dist[0]}")

    return 0


if __name__ == "__main__":
    part1_2()
