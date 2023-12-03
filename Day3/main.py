from typing import List

def is_part_num(lines: List[str], line_no: int, x0: int, x1: int) -> bool:
    chars_to_analyze = ""
    if line_no > 0:
        """Check line above"""
        chars_to_analyze += (lines[line_no-1][max(x0-1,0):min(x1+2, len(lines[line_no]))])

    if line_no < len(lines)-1:
        """Check line below"""
        chars_to_analyze += (lines[line_no+1][max(x0-1,0):min(x1+2, len(lines[line_no]))])

    # Check left and right of digit
    chars_to_analyze += (lines[line_no][max(x0-1,0)])
    chars_to_analyze += (lines[line_no][min(x1+1, len(lines[line_no])-1)])
    # print(chars_to_analyze, " === ")
    for char in chars_to_analyze:
        if not char.isdigit() and char != ".":
            return True
    # for line in lines:
    #     print(line)
    return False

def get_part_nums(lines: List[str]) -> int:
    total = 0
    for line_no, line in enumerate(lines):
        current_num = {
            "val": -1,
            "x0": -1,
            "x1": -1
        }
        for char_no, char in enumerate(line):
            if char.isdigit(): # Digit, add to prev part num
                if current_num["val"] != -1: # Continuation of part num
                    current_num["val"] = current_num["val"]*10 + int(char)
                    current_num["x1"] = char_no
                else: # New part num
                    current_num["val"] = int(char)
                    current_num["x0"] = char_no
                    current_num["x1"] = char_no
            else: # Not digit
                if current_num["val"] != -1: # Check if this is first char after part num
                    # Process current_num and surrounding chars
                    # print(current_num["val"], end=";")
                    if is_part_num(lines, line_no, current_num["x0"], current_num["x1"]):
                        # print(current_num["val"], "Added")
                        total += current_num["val"]
                    current_num["val"] = -1
        
        if current_num["val"] != -1: # Check if this is first char after part num
            # Process current_num and surrounding chars
            # print(current_num["val"], end=";")
            if is_part_num(lines, line_no, current_num["x0"], current_num["x1"]):
                # print(current_num["val"], "Added")
                total += current_num["val"]
            current_num["val"] = -1
            # print(char, end="")
        # print()
    return total

if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines] # Remove newline char
    
    part_nums = get_part_nums(lines)

    sum = part_nums

    print(f"Sum: {sum}")