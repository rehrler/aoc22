import yaml
from yaml.loader import SafeLoader


def read_data():
    monkeys = []
    with open("data/day11.yml", "r") as f:
        data = yaml.load(f, Loader=SafeLoader)
        for key in data.keys():
            monkey = Monkey(
                number=key,
                starting_items=data[key]["Starting items"],
                operation=data[key]["Operation"],
                test=data[key]["Test"],
                condition_true=data[key]["If true"],
                condition_false=data[key]["If false"],
            )
            monkeys.append(monkey)
        return monkeys


class Monkey:
    def __init__(
        self,
        number: str,
        starting_items: str,
        operation: str,
        test: str,
        condition_true: str,
        condition_false: str,
    ):
        self._number = float(number.split(" ")[-1])
        if type(starting_items) == str:
            self._items = [int(item) for item in starting_items.split(", ")]
        else:
            self._items = [starting_items]
        self._operation = operation.split(" ")
        self._test = [test, condition_true, condition_false]
        self._inspected_items = 0

    def _do_operation(self, old):
        if (
            self._operation[2] == "old"
            and self._operation[3] == "*"
            and self._operation[4].isdigit()
        ):
            return old * float(self._operation[4])
        elif (
            self._operation[2] == "old"
            and self._operation[3] == "+"
            and self._operation[4].isdigit()
        ):
            return old + float(self._operation[4])
        elif (
            self._operation[2] == "old"
            and self._operation[3] == "*"
            and self._operation[4] == "old"
        ):
            return old * old
        elif (
            self._operation[2] == "old"
            and self._operation[3] == "+"
            and self._operation[4] == "old"
        ):
            return old + old
        else:
            raise ArithmeticError(f"{self._operation[3]} is not a valid operation")

    def _do_test(self, value):
        divider = float(self._test[0].split(" ")[-1])
        if value % divider == 0:
            return float(self._test[1].split(" ")[-1])
        else:
            return float(self._test[2].split(" ")[-1])

    def do_inspection(self, human: bool, least_common_multiplier: float = 0):
        if len(self._items) > 0:
            self._inspected_items += 1
            worry_level = self._items.pop(0)
            worry_level = self._do_operation(worry_level)
            if human:
                worry_level = worry_level // 3
            else:
                if worry_level > least_common_multiplier:
                    worry_level = worry_level % least_common_multiplier
            return True, worry_level, self._do_test(worry_level)
        else:
            return False, 0, 0

    def add_item(self, item):
        self._items.append(item)

    def get_nb_inspected_items(self):
        return self._inspected_items

    def get_divider(self):
        return float(self._test[0].split(" ")[-1])


def sim(nb_rounds, human=True):
    monkeys = read_data()
    lcm = 1
    if not human:
        for monkey in monkeys:
            lcm *= monkey.get_divider()
        lcm = int(lcm)
    for rnd in range(nb_rounds):
        for monkey_nb in range(len(monkeys)):
            test, worry_level_item, target = monkeys[monkey_nb].do_inspection(
                human=human, least_common_multiplier=lcm
            )
            while test:
                monkeys[int(target)].add_item(worry_level_item)
                test, worry_level_item, target = monkeys[monkey_nb].do_inspection(
                    human=human, least_common_multiplier=lcm
                )
    inspected_items = []
    for monkey in monkeys:
        inspected_items.append(monkey.get_nb_inspected_items())
    inspected_items.sort()
    print(f"level of monkey business: {inspected_items[-1] * inspected_items[-2]}")


def part1_2():
    sim(20, True)
    sim(10000, False)


if __name__ == "__main__":
    part1_2()
