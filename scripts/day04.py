import numpy as np
import pandas as pd


def read_data():
    df = pd.read_csv("data/day04.txt", header=None, index_col=None, sep=",|-")
    df.rename({0: "low_1", 1: "up_1", 2: "low_2", 3: "up_2"}, axis=1, inplace=True)
    return df


def check_fully_contained(row):
    fully_contained = (row["low_1"] >= row["low_2"] and row["up_1"] <= row["up_2"]) or (
        row["low_1"] <= row["low_2"] and row["up_1"] >= row["up_2"]
    )
    return 1 if fully_contained else 0


def part1():
    df = read_data()
    nb_fully_contained = 0
    for i, row in df.iterrows():
        nb_fully_contained += check_fully_contained(row)
    print(
        f"assignment pairs which one range fully contain the other: {nb_fully_contained}"
    )
    return 0


def check_overlap(row):
    set_1 = set([a for a in np.arange(row["low_1"], row["up_1"] + 1, 1)])
    set_2 = set([a for a in np.arange(row["low_2"], row["up_2"] + 1, 1)])
    overlap = set_1 & set_2
    if len(overlap) > 0:
        return 1
    else:
        return 0


def part2():
    df = read_data()
    nb_overlap = 0
    for i, row in df.iterrows():
        nb_overlap += check_overlap(row)
    print(f"assignment pairs for which the ranges overlap: {nb_overlap}")
    return 0


if __name__ == "__main__":
    part1()
    part2()
