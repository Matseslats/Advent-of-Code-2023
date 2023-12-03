from typing import List
import copy

def is_gear_num(lines: List[str], line_no: int, x0: int, x1: int) -> bool:
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
        if char == "*":
            return True
    # for line in lines:
    #     print(line)
    return False

def get_gear_nums(lines: List[str]):
    nums = []
    gear_symbols = []
    for line_no, line in enumerate(lines):
        current_num = {
            "val": -1,
            "x0": -1,
            "x1": -1,
            "line": -1
        }
        for char_no, char in enumerate(line):
            if char == "*":
                gear_symbols.append((line_no, char_no))
            if char.isdigit(): # Digit, add to prev part num
                if current_num["val"] != -1: # Continuation of part num
                    current_num["val"] = current_num["val"]*10 + int(char)
                    current_num["x1"] = char_no
                else: # New part num
                    current_num["val"] = int(char)
                    current_num["x0"] = char_no
                    current_num["x1"] = char_no
                    current_num["line"] = line_no
            else: # Not digit
                if current_num["val"] != -1: # Check if this is first char after part num
                    # Process current_num and surrounding chars
                    # print(current_num["val"], end=";")
                    if is_gear_num(lines, line_no, current_num["x0"], current_num["x1"]):
                        nums.append(copy.deepcopy(current_num))
                        print(current_num["val"], "Added")
                    current_num["val"] = -1
        
        if current_num["val"] != -1: # Check if this is first char after part num
            # Process current_num and surrounding chars
            # print(current_num["val"], end=";")
            if is_gear_num(lines, line_no, current_num["x0"], current_num["x1"]):
                nums.append(copy.deepcopy(current_num))
                print(current_num["val"], "Added")
            current_num["val"] = -1
    return nums, gear_symbols

def get_gear_ratios(part_nums, gear_locations):
    ratios = []
    for loc in gear_locations:
        nums_assosiated = 0
        procuct = 1
        for part_num in part_nums:
            if loc[1] in range(part_num["x0"]-1, part_num["x1"]+2): # Correct x loc 
                if part_num["line"] in range(loc[0]-1, loc[0]+2): # Correct y loc
                    nums_assosiated += 1
                    procuct *= part_num["val"]
        
        if nums_assosiated == 2:
            ratios.append(procuct)
    
    return ratios

if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines] # Remove newline char
    
    part_nums, gear_locations = get_gear_nums(lines)
    # print(part_nums)
    # print(gear_locations)

    ratios = get_gear_ratios(part_nums, gear_locations)

    sum = sum(ratios)

    print(f"Sum: {sum}")