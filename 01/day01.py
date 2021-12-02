def part_one(numbers):
    return len([i for i, v in enumerate(numbers) if (i > 0 and v > numbers[i - 1])])

def part_two(numbers):
    added = [sum(numbers[i:i + 3]) for i in range(len(numbers) - 2)]
    return part_one(added)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        numbers = [int(i) for i in f.readlines()] 
    print(f"Part One: {part_one(numbers)}")
    print(f"Part Two: {part_two(numbers)}")
