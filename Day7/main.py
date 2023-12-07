import time
from typing import List

def get_cards(in_str):
    cards = []
    for char in in_str:
        card_int = None
        if char == 'T':
            card_int = 10
        elif char == 'J':
            card_int = 1
        elif char == 'Q':
            card_int = 12
        elif char == 'K':
            card_int = 13
        elif char == 'A':
            card_int = 14
        else:
            card_int = int(char)
        cards.append(card_int)
    
    return cards

def get_type(cards):
    card_set = list(set(cards))
    set_len = len(card_set)
    jokers = cards.count(1)
    if jokers>0:
        set_len -= 1

    if set_len == 5: # High card
        return 0
    elif set_len == 4: # One pair
        return 1
    elif set_len == 3: # Two pair / Three of a kind
        if cards.count(card_set[0]) == 3-jokers or cards.count(card_set[1]) == 3-jokers or cards.count(card_set[2]) == 3-jokers or jokers>0 and cards.count(card_set[3]) == 3-jokers:
            return 3  # Three of a kind
        return 2 # Two pair
    elif set_len == 2: # Four of a kind / Full house
        if cards.count(card_set[0]) == 4-jokers or cards.count(card_set[1]) == 4-jokers or jokers>0 and cards.count(card_set[2]) == 4-jokers:
            return 5  # Four of a kind
        return 4 # Full house
    elif set_len == 1 or jokers==5: # Five of a kind
        return 6



def get_cards_and_bids(lines: List[str]) -> List[tuple]:
    # data format => ([hand_type, c1, c2, c3, c4, c5], bid)
    data = []
    for line in lines:
        cards_str, bid = line.split(" ")
        bid = int(bid)
        cards = get_cards(cards_str)
        type = get_type(cards)

        data_point = ([type] + cards, bid)
        data.append(data_point)
    return sorted(data)


if __name__ == "__main__":
    start_time = time.time()
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines] # Remove newline char
    
    games = get_cards_and_bids(lines)

    sum = 0
    for rank, (card, bid) in enumerate(games, start=1):
        print(rank, card, bid)
        sum += rank*bid


    end_time = time.time()
    print(f"Output: {sum}")
    print(f"Took {((end_time-start_time)*1000):.4}ms")