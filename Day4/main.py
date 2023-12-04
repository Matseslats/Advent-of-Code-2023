from typing import List

def score_match(win_nums: List[int], my_nums: List[int]) -> int:
    nums_correct = 0
    for num in my_nums:
        nums_correct += num in win_nums
    
    return nums_correct

def get_ints(in_str: str) -> List[int]:
    strs = in_str.split(" ")
    ints = []
    for str in strs:
        if str != "":
            ints.append(int(str))
    return ints

def get_score(line: str) -> int:
    print(line)
    # win_nums = get_ints(line[8:22])
    # my_nums = get_ints(line[25:])
    win_nums = get_ints(line[10:39])
    my_nums = get_ints(line[42:])
    score = score_match(win_nums, my_nums)
    # print(win_nums, my_nums, score)
    return score


def get_scores(lines: List[str]) -> List[int]:
    tot_cards = 0
    card_copies = [1]*len(lines)
    print(card_copies)
    for i, line in enumerate(lines):
        # Get how many cards you won, card_copies[i] is how many were played
        # print(card_copies)
        won_cards = get_score(line)
        # Add the amount of cards you won (the amont of this card you have) to the next n, num of cards won, cards
        for j in range(i+1, i+1+won_cards):
            card_copies[j] += card_copies[i]
        # print(won_cards, card_copies[i])
        tot_cards += card_copies[i]
    return tot_cards

if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines] # Remove newline char
    
    part_nums = get_scores(lines)

    sum = part_nums

    print(f"Sum: {sum}")