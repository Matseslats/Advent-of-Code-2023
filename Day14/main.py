import time
import numpy as np
from tqdm import tqdm


def rotate_matrix(matrix):
    # Rotate the array 90 degrees clockwise
    rotated_array = np.rot90(matrix, k=-1)

    return rotated_array


def get_weight(in_arr, move=True):
    new_arr = np.array([['.' for y in range(len(in_arr[0]))] for x in range(len(in_arr))])
    # print(f"Input: \n{in_arr}")
    tot_weight = 0
    for x, _ in enumerate(new_arr[0]):
        wall = len(new_arr)+1
        for y, _ in enumerate(new_arr):
            height = len(new_arr)-y
            if move:
                if in_arr[y][x] == "O":
                    wall -= 1
                    tot_weight += wall
                    new_arr[len(new_arr)-(wall)][x] = 'O'
                    # print("Added weight", wall)
                elif in_arr[y][x] == "#":
                    wall = height
                    new_arr[y][x] = '#'
                    # print("Wall at", wall, x, y)
            else:
                if in_arr[y][x] == "O":
                    tot_weight += height

    # print(f"Output: \n{new_arr}")

    return tot_weight, new_arr


def print_arr(arr):
    for line in arr:
        print("".join(line))


def find_loop(start_matrix):
    rot_matrix = start_matrix
    seen = {}
    iter = 0
    target_iter = 1000000000
    for _ in tqdm(range(target_iter)):
        tuples = tuple(map(tuple, rot_matrix))
        if tuples in seen:
            loop_len = iter-seen[tuples]
            needed_loops = ((target_iter-seen[tuples]) % loop_len)  # How many more cycles are needed
            print(loop_len, iter, needed_loops)
            return rot_matrix, needed_loops, get_weight(rot_matrix)[0]

        for i in range(4):
            global rolled_north
            rot_matrix = rotate_matrix(rolled_north)
            weight, rolled_north = get_weight(rot_matrix)

        seen[tuples] = iter
        iter += 1
    return rot_matrix, 0, get_weight(rot_matrix)[0]


if __name__ == "__main__":
    start_time = time.time()
    in_array = []
    with open("input.txt") as file:
        in_array = np.array([np.array(line.strip()) for line in file.readlines()])

    north_weight, rolled_north = get_weight(in_array)

    rot_matrix = rolled_north
    pt2_weight = 0

    rot_matrix, rest_loops, pt2_weight = find_loop(rot_matrix)


    for _ in tqdm(range(rest_loops)):
        for i in range(4):
            pt2_weight, rolled_north = get_weight(rot_matrix)
            rot_matrix = rotate_matrix(rolled_north)

    # print_arr(rot_matrix)

    end_time = time.time()
    print(f"Solution Pt1: {north_weight}")
    print(f"Solution Pt2: {get_weight(rot_matrix, move=False)[0]}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
