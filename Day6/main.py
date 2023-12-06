import time
from typing import List
from functools import reduce

def get_ints(in_str: str) -> List[int]:
    strs = in_str.split(" ")
    ints = []
    for str in strs:
        if str != "":
            ints.append(int(str))
    return ints

# Return e.g.[(7, 9), (15, 40), (30, 200)]
def make_games(lines: List[str]) -> List[tuple]:
    times = get_ints(lines[0].split(":")[1])
    dists = get_ints(lines[1].split(":")[1])

    games = list(zip(times, dists))

    return games

def ways_to_beat_game(game: tuple) -> int:
    ways_to_beat = 0
    for held_down in range(game[0]):
        dist = held_down*(game[0]-held_down)
        if dist > game[1]:
            ways_to_beat += 1
            # print("T", held_down, "D", dist)
    
    # print(ways_to_beat)
    return ways_to_beat

if __name__ == "__main__":
    start_time = time.time()
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines] # Remove newline char
    
    games = make_games(lines)

    ways_to_beat = [ways_to_beat_game(g) for g in games]


    output = reduce(lambda x, y: x*y, ways_to_beat)

    end_time = time.time()
    print(f"Output: {output}")
    print(f"Took {((end_time-start_time)*1000):.4}ms")