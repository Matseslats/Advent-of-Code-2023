import time
import numpy as np
from tqdm import tqdm


def rotate_matrix(matrix):
    # Rotate the array 90 degrees clockwise
    rotated_array = np.rot90(matrix, k=-1)

    return rotated_array


def get_weight(in_arr):
    new_arr = np.array([['.' for y in range(len(in_arr[0]))] for x in range(len(in_arr))])
    # print(f"Input: \n{in_arr}")
    tot_weight = 0
    for x, _ in enumerate(new_arr[0]):
        wall = len(new_arr)+1
        for y, _ in enumerate(new_arr):
            height = len(new_arr)-y
            if in_arr[y][x] == "O":
                wall -= 1
                tot_weight += wall
                new_arr[len(new_arr)-(wall)][x] = 'O'
                # print("Added weight", wall)
            elif in_arr[y][x] == "#":
                wall = height
                new_arr[y][x] = '#'
                # print("Wall at", wall, x, y)

    # print(f"Output: \n{new_arr}")

    return tot_weight, new_arr


def print_arr(arr):
    for line in arr:
        print("".join(line))



if __name__ == "__main__":
    start_time = time.time()
    in_array = []
    with open("input.txt") as file:
        in_array = np.array([np.array(line.strip()) for line in file.readlines()])

    north_weight, rolled_north = get_weight(in_array)

    rot_matrix = rolled_north
    pt2_weight = 0

    for _ in tqdm(range(1000000000)):
        for i in range(4):
            pt2_weight, rolled_north = get_weight(rot_matrix)
            # print("Rolled:")
            # print_arr(rolled_north)
            # print()
            # print()

            # print_arr(rolled_north)
            rot_matrix = rotate_matrix(rolled_north)
            # print("Rotated:")
            # print_arr(rot_matrix)
        # print_arr(rot_matrix)
        # print()


    # for line in rolled_north:
    #     print("".join(line))
    # print()

    end_time = time.time()
    print(f"Solution Pt1: {north_weight}")
    print(f"Solution Pt2: {pt2_weight}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
