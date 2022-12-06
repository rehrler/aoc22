import pandas as pd


def read_data():
    df = pd.read_csv("data/day02.txt", header=None, index_col=None, sep=" ")
    df.rename({0: "opponent", 1: "answer"}, axis=1, inplace=True)
    return df


def get_res(row):
    poss_res = {
        "AX": 3,
        "AY": 6,
        "AZ": 0,
        "BX": 0,
        "BY": 3,
        "BZ": 6,
        "CX": 6,
        "CY": 0,
        "CZ": 3,
    }
    total_score = poss_res[row["opponent"] + row["answer"]]
    if row["answer"] == "X":
        total_score += 1
    if row["answer"] == "Y":
        total_score += 2
    if row["answer"] == "Z":
        total_score += 3

    return total_score


def part1():
    df = read_data()
    total_score = 0
    for i, row in df.iterrows():
        total_score += get_res(row)
    print(f"Total score expected: {total_score}")
    return 0


def part2():
    df = read_data()
    total_score = 0
    for i, row in df.iterrows():
        if row["answer"] == "X":
            if row["opponent"] == "A":
                row["answer"] = "Z"
            elif row["opponent"] == "B":
                row["answer"] = "X"
            elif row["opponent"] == "C":
                row["answer"] = "Y"
        elif row["answer"] == "Y":
            if row["opponent"] == "A":
                row["answer"] = "X"
            elif row["opponent"] == "B":
                row["answer"] = "Y"
            elif row["opponent"] == "C":
                row["answer"] = "Z"
        elif row["answer"] == "Z":
            if row["opponent"] == "A":
                row["answer"] = "Y"
            elif row["opponent"] == "B":
                row["answer"] = "Z"
            elif row["opponent"] == "C":
                row["answer"] = "X"
        total_score += get_res(row)
    print(f"Total score expected: {total_score}")
    return 0


if __name__ == "__main__":
    part1()
    part2()
