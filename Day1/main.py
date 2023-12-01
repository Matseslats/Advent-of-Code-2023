
def get_calibration_value(line: str) -> int:
    num_string = ""
    # Get all the characters that are digits
    for char in line:
        if char.isdigit():
            num_string += char

    first_int = int(num_string[0])
    last_int = int(num_string[-1])

    return 10*first_int + last_int


if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
    
    sum = sum([get_calibration_value(x) for x in lines])

    print(f"Sum: {sum}")