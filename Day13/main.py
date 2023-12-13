import time
import copy

def get_error_fixed_reflection(lines):
    val_to_avoid = get_reflection(lines)
    # print(f"Do not return if {val_to_avoid}")
    for y,_ in enumerate(lines):
        for x,_ in enumerate(lines[0]):
            mutable_lines = copy.deepcopy(lines)
            mutable_lines[y][x] = not lines[y][x]
            # print(f"Mutating y={y} x={x}")
            result = get_reflection(mutable_lines, avoid=val_to_avoid)
            if result != -1:
                # print("Result", result)
                return result
    
    print("Could not find match")


def get_reflection(lines, avoid=None):
    # print("Running", lines)
    
    for y,_ in enumerate(lines):
        if y == 0 or y == len(lines):
            continue
        line_comp = min(y, len(lines)-y)
        if lines[(y-line_comp):y] == list(reversed(lines[y:y+line_comp])):
            # print(f"Symmetry at y:{y}")
            if avoid is None or y!= avoid:
                return (y)*100

    for x,_ in enumerate(lines[0]):
        if x == 0 or x == len(lines[0]):
            continue
        line_comp = min(x, len(lines[0])-x)
        if all([list(line[(x-line_comp):x]) == list(reversed(line[x:x+line_comp])) for line in lines]):
            # print(f"Symmetry at x:{x}")
            if avoid is None or y != avoid:
                return x


    return -1

if __name__ == "__main__":
    start_time = time.time()
    lines = []
    with open("input.txt") as file:
        lines = [[char=='#' for char in line.strip()] for line in file.readlines()]
    
    to_test = []
    value = 0
    for line in lines:
        if line == []:
            value += get_error_fixed_reflection(to_test)
            # print("New val", value)
            to_test = []
        else:
            to_test.append(line)

    # value = get_reflection(lines)


    end_time = time.time()
    print(f"Solution: {value}")
    print(f"Took {((end_time-start_time)*1000):.4}ms")