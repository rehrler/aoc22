import pandas as pd


def read_data():
    df = pd.read_csv("data/day03.txt", header=None, index_col=None)
    return df


def get_score(letter: str):
    score = ord(letter.lower()) - 96
    if letter.isupper():
        score += 26
    return score


def solve_part1(param: str):
    arr = [char for char in param]
    bucket1, bucket2 = arr[:int(len(arr) / 2)], arr[int(len(arr) / 2):]
    equal_item = (set(bucket1) & set(bucket2)).pop()
    return get_score(equal_item)


def part1():
    df = read_data()
    score = 0
    for i, row in df.iterrows():
        score += solve_part1(row[0])
    print(f"sum of the priorities: {score}")
    return 0


def solve_part2(elf_bucket):
    equal_item = (set([char for char in elf_bucket[0]]) & \
                  set([char for char in elf_bucket[1]]) & \
                  set([char for char in elf_bucket[2]])).pop()
    return get_score(equal_item)


def part2():
    score = 0
    df = read_data()
    elf_bucket = []
    for i, row in df.iterrows():
        if (i % 3 == 0 and i != 0) or i == len(df) - 1:
            if i == len(df) - 1:
                elf_bucket.append(row[0])
            score += solve_part2(elf_bucket)
            elf_bucket = [row[0]]
        else:
            elf_bucket.append(row[0])
    print(f"sum of the priorities: {score}")


if __name__ == "__main__":
    part1()
    part2()
