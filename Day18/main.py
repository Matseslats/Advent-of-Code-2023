import time
from typing import List, Tuple
from shapely.geometry import Polygon


def count_squares_in_path(path):
    total_squares = 0

    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]

        # Calculate Manhattan distance
        distance = abs(x2 - x1) + abs(y2 - y1)

        # Sum up the Manhattan distances
        total_squares += distance

    return total_squares


def solve(lines: List[str]):
    x, y = 0, 0
    max_x, max_y = 0, 0
    nodes = {(x, y): 0}
    coords = []
    perimeter = 0
    area = 0
    dist_vecs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    for l in lines:
        direc, length, color = l.split(" ")
        length = int(length)
        dy, dx = dist_vecs[direc]
        dy, dx = dy*length, dx*length
        y, x = y+dy, x+dx
        perimeter+=length
        area+=x*dy
        print(length)

    print(area, perimeter)
    print(area+perimeter//2+1)

    return area+perimeter//2+1


if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    start_time = time.time()
    loss_pt1 = solve(lines)

    end_time = time.time()
    print(f"Solution Pt1: {loss_pt1}")
    # print(f"Solution Pt2: {max_energized}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
