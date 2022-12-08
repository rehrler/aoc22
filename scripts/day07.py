import uuid

import numpy as np


def read_data():
    file = open("data/day07.txt", "r")
    lines = file.readlines()
    identifier = uuid.uuid4()
    curr_node = Node("dir", "root", identifier)
    last_parent = []
    parent = identifier
    for line in lines:
        arr = line.split(" ")
        if arr[0] == "$" and arr[1] == "cd" and arr[2] == "..\n":
            parent = last_parent.pop()
        elif arr[0] == "$" and arr[1] == "cd" and arr[2] != "..\n":
            new_id = uuid.uuid4()
            curr_node.add_child(Node("dir", arr[2], new_id), parent)
            last_parent.append(parent)
            parent = new_id
        elif arr[0] != "dir" and arr[0] != "$":
            new_id = uuid.uuid1()
            curr_node.add_child(Node("file", arr[1], new_id, float(arr[0])), parent)
    return curr_node


class Node:
    def __init__(self, typ: str, name: str, identifier: uuid.UUID, size: float = 0):
        self._type, self._name, self._identifier, self._size = (
            typ,
            name,
            identifier,
            size,
        )
        self._children = []

    def add_child(self, node: "Node", parent: uuid.UUID):
        if self._identifier == parent:
            self._children.append(node)
        else:
            for child in self._children:
                child.add_child(node, parent)

    def calc_size(self) -> float:
        for child in self._children:
            self._size += child.calc_size()
        return self._size

    def sum_dir(self, critical_size: float) -> list:
        sizes = []
        if self._type == "dir":
            if self._size <= critical_size:
                sizes.append(self._size)
            for child in self._children:
                sizes.extend(child.sum_dir(critical_size))
        return sizes

    def get_size(self) -> float:
        return self._size


def part1_2():
    # part 1
    tree = read_data()
    tree.calc_size()
    print(f"size of all directories < 100000: {np.sum(tree.sum_dir(100000))}")

    # part 2
    to_delete = 30000000 - 70000000 + tree.get_size()
    sizes = tree.sum_dir(70000000)
    candidates = []
    for size in sizes:
        if size >= to_delete:
            candidates.append(size)
    print(f"smallest dir to delete is of size: {np.min(candidates)}")


if __name__ == "__main__":
    part1_2()
