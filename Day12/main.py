import time

PRINT_DEBUG = False

prev_vals = {}

def get_solution(line, to_match, depth=0):
    start_str = f"[{depth:3}]{'  '*depth}"
    if PRINT_DEBUG:
        print(start_str, line, to_match)
    if (len(line) == 0 or '#' not in line) and len(to_match) == 0:
        if PRINT_DEBUG:
            print(start_str, "TRUE")
        return 1
    if len(line) < sum(to_match) or (len(line)>0 and to_match==[]):
        if PRINT_DEBUG:
            print(start_str, "FALSE")
        return 0
    
    val = 0

    to_match_tuple = tuple(to_match)
    if (line, to_match_tuple) in prev_vals:
        if PRINT_DEBUG:
            print(start_str, f"Saved as {prev_vals[(line, to_match_tuple)]}")
        return prev_vals[(line, to_match_tuple)]

    if line[0] == '?':
        """Sum of split"""
        if PRINT_DEBUG:
            print(start_str, "SPLIT")
        val = (get_solution('#'+line[1:], to_match, depth=depth+1) + get_solution('.'+line[1:], to_match, depth=depth+1))
    elif line[0] == '#' and '.' in line[:to_match[0]]:
        if PRINT_DEBUG:
            print(start_str, "INVALID PATH.")
        return 0
    elif '.' not in line[:to_match[0]]: # Valid
        if len(line)>to_match[0] and line[to_match[0]] == '#': # '#' would follow immediately after, invalid
            return 0 # Invalid path
        if PRINT_DEBUG:
            print(start_str, "OK, CHECK REST")
        val = get_solution(line[to_match[0]+1:], to_match[1:], depth=depth+1)

    else: # Starts with '.'
        if PRINT_DEBUG:
            print(start_str, "NOPE, CHECK REST")
        val = get_solution(line[1:], to_match, depth=depth+1)

    if PRINT_DEBUG:
        print(start_str, val)
    prev_vals[(line, to_match_tuple)] = val
    return val


def get_input(line):
    string, ints = line.split(" ")
    ints = [int(i) for i in ints.split(",")]
    string = string*1
    ints = ints*1
    print("INPUT:",string, ints)
    return string, ints


def check(lines):
    sols = []
    for line in lines:
        string, ints = get_input(line)
        sol = get_solution(string, ints)
        sols.append(sol)

    return sols
    # return [get_solution(get_input(line)) for line in lines]

if __name__ == "__main__":
    start_time = time.time()
    lines = []
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
    
    solutions = check(lines)
    print(solutions)


    end_time = time.time()
    print(f"Number of solutions: {sum(solutions)}")
    print(f"Took {((end_time-start_time)*1000):.4}ms")