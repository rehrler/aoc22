import numpy as np


def read_data():
    file = open("data/day10.txt", "r")
    lines = file.readlines()
    commands = []
    for line in lines:
        splitted_str = line.split(" ")
        if len(splitted_str) > 1:
            commands.append([splitted_str[0], int(splitted_str[1])])
        else:
            commands.append([splitted_str[0][:-1], int(0)])

    return commands


def check_ss(nb_cycle, x_value):
    poss_cycles = [20, 60, 100, 140, 180, 220]
    for poss_cycle in poss_cycles:
        if nb_cycle == poss_cycle:
            return poss_cycle * x_value
    return 0


def check_ref_sprite(reference_sprite, x_value):
    if 1 <= x_value <= 38:
        if (
            reference_sprite[x_value - 1] == 1
            and reference_sprite[x_value] == 1
            and reference_sprite[x_value + 1] == 1
        ):
            return reference_sprite
        else:
            new_ref_sprite = np.zeros(40)
            new_ref_sprite[x_value - 1] = 1
            new_ref_sprite[x_value] = 1
            new_ref_sprite[x_value + 1] = 1
            return new_ref_sprite
    elif x_value == 0:
        if reference_sprite[x_value] == 1 and reference_sprite[x_value + 1] == 1:
            return reference_sprite
        else:
            new_ref_sprite = np.zeros(40)
            new_ref_sprite[x_value] = 1
            new_ref_sprite[x_value + 1] = 1
            return new_ref_sprite
    elif x_value == -1:
        if reference_sprite[x_value + 1] == 1:
            return reference_sprite
        else:
            new_ref_sprite = np.zeros(40)
            new_ref_sprite[x_value + 1] = 1
            return new_ref_sprite
    elif x_value == 39:
        if reference_sprite[x_value - 1] == 1 and reference_sprite[x_value] == 1:
            return reference_sprite
        else:
            new_ref_sprite = np.zeros(40)
            new_ref_sprite[x_value] = 1
            new_ref_sprite[x_value - 1] = 1
            return new_ref_sprite
    elif x_value == 40:
        if reference_sprite[x_value - 1] == 1:
            return reference_sprite
        else:
            new_ref_sprite = np.zeros(40)
            new_ref_sprite[x_value - 1] = 1
            return new_ref_sprite


def adapt_screen(reference_sprite, screen, x_value, nb_cycle):
    new_reference_sprite = check_ref_sprite(reference_sprite, x_value)

    if nb_cycle < 41:
        row = 0
    elif 41 <= nb_cycle < 81:
        row = 1
        nb_cycle -= 40
    elif 81 <= nb_cycle < 121:
        row = 2
        nb_cycle -= 80
    elif 121 <= nb_cycle < 161:
        row = 3
        nb_cycle -= 120
    elif 161 <= nb_cycle < 201:
        row = 4
        nb_cycle -= 160
    else:
        row = 5
        nb_cycle -= 200
    if new_reference_sprite[nb_cycle - 1] == 1:
        screen[row, nb_cycle - 1] = 1

    return new_reference_sprite, screen


def part1_2():
    commands = read_data()
    nb_cycle = 0
    x_value = 1
    reference_sprite = np.zeros(40)
    reference_sprite[0], reference_sprite[1], reference_sprite[2] = 1, 1, 1
    screen = np.zeros((6, 40))
    signal_strength = 0
    for command in commands:
        if command[0] == "noop":
            nb_cycle += 1
            signal_strength += check_ss(nb_cycle, x_value)
            reference_sprite, screen = adapt_screen(
                reference_sprite, screen, x_value, nb_cycle
            )
        elif command[0] == "addx":
            nb_cycle += 1
            signal_strength += check_ss(nb_cycle, x_value)
            reference_sprite, screen = adapt_screen(
                reference_sprite, screen, x_value, nb_cycle
            )
            nb_cycle += 1
            signal_strength += check_ss(nb_cycle, x_value)
            reference_sprite, screen = adapt_screen(
                reference_sprite, screen, x_value, nb_cycle
            )
            x_value += command[1]

    print(f"sum of signal strengths {signal_strength}")
    text = "\n"
    for i in range(screen.shape[0]):
        for j in range(screen.shape[1]):
            if screen[i, j] == 1:
                text += "#"
            else:
                text += "."
        text += "\n"
    print(text)


if __name__ == "__main__":
    part1_2()
