import time
from typing import List


def get_weight(lines: List[str]):
    tot_weight = 0
    for x, _ in enumerate(lines[0]):
        wall = len(lines)+1
        for y, _ in enumerate(lines):
            height = len(lines)-y
            match lines[y][x]:
                case 'O':
                    wall -= 1
                    tot_weight += wall
                    print("Added weight", wall)
                    continue
                case '.':
                    continue
                case '#':
                    wall = height
                    print("Wall at", wall)
                    continue

    return tot_weight


if __name__ == "__main__":
    start_time = time.time()
    lines = []
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    weight = get_weight(lines)

    end_time = time.time()
    print(f"Solution: {weight}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
