def part_one(lines: list):
    m = {"forward": 0, "down": 0, "up": 0}
    for l in lines:
        direction, amount = l.strip().split(" ")
        m[direction] += int(amount)
    return m["forward"] * (m["down"] - m["up"])


def part_two(lines: list):
    m = {"forward": 0, "down": 0, "up": 0}
    depth = 0
    for l in lines:
        direction, amount = l.strip().split(" ")
        m[direction] += int(amount)
        if direction == "forward" and (aim := m["down"] - m["up"]) != 0:
            depth += aim * int(amount)
    return m["forward"] * depth


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
