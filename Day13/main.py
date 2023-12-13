import time

def get_reflection(lines):
    # print("Running", lines)
    for y,_ in enumerate(lines):
        if y == 0 or y == len(lines):
            continue
        line_comp = min(y, len(lines)-y)
        if lines[(y-line_comp):y] == list(reversed(lines[y:y+line_comp])):
            # print(f"Sym {y}")
            return (y)*100
    
    for x,_ in enumerate(lines[0]):
        if x == 0 or x == len(lines[0]):
            continue
        line_comp = min(x, len(lines[0])-x)
        if all([list(line[(x-line_comp):x]) == list(reversed(line[x:x+line_comp])) for line in lines]):
            # print("Found x", x)
            return x

    return -1

if __name__ == "__main__":
    start_time = time.time()
    lines = []
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
    
    to_test = []
    value = 0
    for line in lines:
        if line == '':
            value += get_reflection(to_test)
            # print("New val", value)
            to_test = []
        else:
            to_test.append(line)

    # value = get_reflection(lines)


    end_time = time.time()
    print(f"Solution: {value}")
    print(f"Took {((end_time-start_time)*1000):.4}ms")