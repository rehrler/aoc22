import numpy as np
import pandas as pd


def read_data():
    df = pd.read_csv("data/day01.txt", header=None, index_col=None, skip_blank_lines=False)
    return df


def part1_2():
    df = read_data()
    value, top_values = 0, []
    for i, row in df.iterrows():
        curr_val = row[0]
        if np.isnan(curr_val):
            top_values.append(value)
            value = 0
        else:
            value += curr_val
    top_values = sorted(top_values)[-3:]
    print(f"Elf carrying the most Calories: {top_values[-1]}")
    print(f"Top 3 Elfs carrying the most Calories: {np.sum(top_values)}")
    return 0


if __name__ == "__main__":
    part1_2()
