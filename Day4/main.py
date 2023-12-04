from typing import List

def score_match(win_nums: List[int], my_nums: List[int]) -> int:
    nums_correct = 0
    for num in my_nums:
        nums_correct += num in win_nums
    
    # Get the score, 1 match = 1 pt, double for every next match
    if nums_correct <= 0:
        return 0
    return pow(2, nums_correct-1)

def get_ints(in_str: str) -> List[int]:
    strs = in_str.split(" ")
    ints = []
    for str in strs:
        if str != "":
            ints.append(int(str))
    return ints

def get_score(line: str) -> int:
    print(line)
    win_nums = get_ints(line[10:39])
    my_nums = get_ints(line[42:])
    score = score_match(win_nums, my_nums)
    print(win_nums, my_nums, score)
    return score


def get_scores(lines: List[str]) -> List[int]:
    return [get_score(line) for line in lines]

if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines] # Remove newline char
    
    part_nums = get_scores(lines)

    sum = sum(part_nums)

    print(f"Sum: {sum}")