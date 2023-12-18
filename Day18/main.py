import time
from typing import List


def solve(lines: List[str], useColor=False):
    x, y = 0, 0
    perimeter = 0
    area = 0
    dist_vecs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    color_vecs = {"3": (-1, 0), "1": (1, 0), "2": (0, -1), "0": (0, 1)}
    for l in lines:
        direc, length, color = l.split(" ")
        color = color[2:-1]
        length = int(length)
        dy, dx = dist_vecs[direc]
        if useColor:
            # Pt 2
            length = int(color[:-1],16)
            dy, dx = color_vecs[color[-1]]

        dy, dx = dy*length, dx*length
        y, x = y+dy, x+dx
        perimeter+=length
        area+=x*dy

    return area+perimeter//2+1


if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    start_time = time.time()
    loss_pt1 = solve(lines, useColor=False)
    loss_pt2 = solve(lines, useColor=True)

    end_time = time.time()
    print(f"Solution Pt1: {loss_pt1}")
    print(f"Solution Pt2: {loss_pt2}")
    # print(f"Solution Pt2: {max_energized}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
