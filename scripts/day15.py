import shapely.ops as operations
from shapely import LineString
from shapely import Polygon


def read_data():
    lines = open("data/day15.txt", "r").read().split("\n")
    entries = []
    for line in lines:
        split1 = line.split(": ")
        split2 = split1[0].split(", ")
        split3 = split1[1].split(", ")
        sensor_x, sensor_y = int(split2[0].split("=")[-1]), int(
            split2[1].split("=")[-1]
        )
        beacon_x, beacon_y = int(split3[0].split("=")[-1]), int(
            split3[1].split("=")[-1]
        )
        new_entry = {
            "sensor": {"x": sensor_x, "y": sensor_y},
            "beacon": {"x": beacon_x, "y": beacon_y},
        }
        entries.append(new_entry)
    return entries


def get_x_min_max(data):
    x_min, x_max = 0, 0
    for point in data:
        if point["sensor"]["x"] > x_max:
            x_max = point["sensor"]["x"]
        if point["beacon"]["x"] > x_max:
            x_max = point["beacon"]["x"]
        if point["sensor"]["x"] < x_min:
            x_min = point["sensor"]["x"]
        if point["beacon"]["x"] < x_min:
            x_min = point["beacon"]["x"]
    return x_min, x_max


def build_polygon_area(data, y_coord):
    poss_x_max, poss_x_min = [], []
    diamonds = []
    subtract_part1 = 0
    for pair in data:
        man_dis = abs(pair["sensor"]["x"] - pair["beacon"]["x"]) + abs(
            pair["sensor"]["y"] - pair["beacon"]["y"]
        )
        poss_x_max.append(pair["sensor"]["x"] + man_dis)
        poss_x_min.append(pair["sensor"]["x"] - man_dis)
        distances = ((man_dis, 0), (0, man_dis), (-man_dis, 0), (0, -man_dis))
        if pair["sensor"]["y"] == y_coord:
            subtract_part1 += 1
        diamonds.append(
            Polygon(
                [
                    (pair["sensor"]["x"] + x, pair["sensor"]["y"] + y)
                    for x, y in distances
                ]
            )
        )
    union = operations.unary_union(diamonds)
    return (
        union,
        min(poss_x_min),
        max(poss_x_max),
        subtract_part1,
    )


def part1_2():
    # part 1
    data = read_data()
    y_coord = 2000000
    diamonds, x_min, x_max, sub_part1 = build_polygon_area(data, y_coord)
    (coords_x, coords_y) = diamonds.intersection(
        LineString([(x_min, y_coord), (x_max, y_coord)])
    ).xy
    print(
        f"occupied positions at line y={y_coord}: {int(abs(coords_x[0] - coords_x[1] + sub_part1))}"
    )

    # part 2
    max_coord = 4000000
    total_field = Polygon(
        [(0, 0), (0, max_coord), (max_coord, max_coord), (max_coord, 0)]
    )
    diamond_field_intersection = total_field.intersection(diamonds)
    hole = total_field.difference(diamond_field_intersection)
    hole_x, hole_y = hole.exterior.coords.xy
    # check with debugging coordinates of hole
    print(f"tuning frequency: {int(max_coord * hole_x[0] + hole_y[1])}")
    return 0


if __name__ == "__main__":
    part1_2()
