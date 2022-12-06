def read_data():
    file1 = open("data/day06.txt", "r")
    lines = file1.readlines()
    packet = []
    for line in lines:
        packet.append(line)
    return packet[0]


def check_for_packet(packet, length):
    for i in range(len(packet) - length + 1):
        if i > 0:
            new_packet = packet[i:i + length]
            packets = set(new_packet)
            if len(packets) == length:
                print(f"found valid packet at {i + length}")
                break


def part1_2():
    packet = read_data()
    check_for_packet(packet, 4)
    check_for_packet(packet, 14)
    return 0


if __name__ == "__main__":
    part1_2()
