import numpy as np


def read_data():
    return np.genfromtxt("data/day08.txt", delimiter=1, dtype=int)


def check_vis(row, col, i, j):
    # check row from left
    row_left_visible, row_right_visible = True, True
    for jj in range(len(row)):
        if jj != j:
            if row[jj] >= row[j]:
                if jj < j:
                    row_left_visible = False
                else:
                    row_right_visible = False
    # check col
    col_top_visible, col_low_visible = True, True
    for ii in range(len(col)):
        if ii != i:
            if col[ii] >= col[i]:
                if ii < i:
                    col_top_visible = False
                else:
                    col_low_visible = False
    if row_left_visible or row_right_visible or col_top_visible or col_low_visible:
        return 1
    else:
        return 0


def calc_vis_trees(sub_row_col):
    score = 0
    for i in range(len(sub_row_col) - 1):
        if sub_row_col[0] > sub_row_col[i + 1]:
            score += 1
        elif sub_row_col[0] <= sub_row_col[i + 1]:
            score += 1
            break
    if score == 0:
        score = 1
    return score


def calc_score(candidate, field):
    row, col = field[candidate[0], :], field[:, candidate[1]]
    # going left
    sub_row_left = np.flip(row[: candidate[1] + 1])
    score_left = calc_vis_trees(sub_row_left)
    # going right
    sub_row_right = row[candidate[1] :]
    score_right = calc_vis_trees(sub_row_right)
    # going up
    sub_col_up = np.flip(col[: candidate[0] + 1])
    score_up = calc_vis_trees(sub_col_up)
    # going down
    sub_col_down = col[candidate[0] :]
    score_down = calc_vis_trees(sub_col_down)
    return score_left * score_right * score_up * score_down


def part1_2():
    field = read_data()
    visible = 2 * field.shape[0] + 2 * (field.shape[1] - 2)
    candidates = []
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if (
                i != 0
                and i != field.shape[0] - 1
                and j != 0
                and j != field.shape[1] - 1
            ):
                visibility = check_vis(field[i, :], field[:, j], i, j)
                visible += visibility
                if visibility == 1:
                    candidates.append([i, j])
    print(f"visible trees: {visible}")

    scores = np.zeros(field.shape)
    for candidate in candidates:
        scores[candidate[0], candidate[1]] = calc_score(candidate, field)
    print(f"max score {np.max(scores)}")


if __name__ == "__main__":
    part1_2()
