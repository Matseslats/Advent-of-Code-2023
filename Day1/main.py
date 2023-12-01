substitutions = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9
}

def get_indexes(line: str, subs: dict):
    indexes = []
    for key in subs:
        index_found_at = line.find(str(key))
        if index_found_at != -1:
            indexes.append((key, index_found_at))

    # Sort by index they appear at in string
    indexes = sorted(indexes, key=lambda x: x[1])
    return indexes

def get_calibration_value(line: str) -> int:
    indexes = get_indexes(line, substitutions)
    first_int = int(substitutions[indexes[0][0]])
    last_int = int(substitutions[indexes[-1][0]])

    print(10*first_int + last_int)
    return 10*first_int + last_int


if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
    
    sum = sum([get_calibration_value(x) for x in lines])

    print(f"Sum: {sum}")