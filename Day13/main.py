import time
import copy

time_spent_copying_array = 0


def get_error_fixed_reflection(matrix):
    global time_spent_copying_array
    val_to_avoid = get_reflection(matrix)
    # print(f"Do not return if {val_to_avoid}")
    for y, _ in enumerate(matrix):
        for x, _ in enumerate(matrix[0]):
            s = time.time()
            mutable_lines = copy.deepcopy(matrix)
            time_spent_copying_array += time.time() - s
            mutable_lines[y][x] = not matrix[y][x]
            # print(f"Mutating y={y} x={x}")
            result = get_reflection(mutable_lines, avoid=val_to_avoid)
            if result != -1:
                # print("Result", result)
                return result

    print("Could not find match")


def get_reflection(matrix, avoid=None):
    # print("Running", lines)

    for y, _ in enumerate(matrix):
        if y == 0 or y == len(matrix):
            continue
        line_comp = min(y, len(matrix) - y)
        if matrix[(y - line_comp):y] == list(reversed(matrix[y:y + line_comp])):
            # print(f"Symmetry at y:{y}")
            if not (avoid is not None and y * 100 == avoid):
                # print(avoid, y)
                return y * 100

    for x, _ in enumerate(matrix[0]):
        if x == 0 or x == len(matrix[0]):
            continue
        line_comp = min(x, len(matrix[0]) - x)
        if all([list(line[(x - line_comp):x]) == list(reversed(line[x:x + line_comp])) for line in matrix]):
            # print(f"Symmetry at x:{x}")
            if not (avoid is not None and x == avoid):
                # print(avoid, x)
                return x

    return -1


if __name__ == "__main__":
    start_time = time.time()
    lines = []
    with open("input.txt") as file:
        lines = [[char == '#' for char in line.strip()] for line in file.readlines()]

    to_test = []
    value = 0
    for line in lines:
        if not line:
            value += get_error_fixed_reflection(to_test)
            to_test = []
        else:
            to_test.append(line)

    end_time = time.time()
    print(f"Solution: {value}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
    print(f"Time spent in deepcopy {(time_spent_copying_array * 1000):.4}ms")
