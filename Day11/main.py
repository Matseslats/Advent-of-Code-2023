import time
from typing import List
from tqdm import tqdm

# Expand empty lines
def expand_galaxies(lines: List[bool]):
    # print("Y pre:", len(lines))
    index = 0
    for y, line in enumerate(lines):
        if not any(line):
            # print(f"No galaxies at y={index}", line)
            lines = lines[:index] + [line] + lines[index:]
            index += 1
        index += 1
    # print("Y post:", len(lines))
    
    # print()

    # print("X pre:", len(lines[0]))
    index = 0
    for x, _ in enumerate(lines[0]):
        line = [line[index] for line in lines]
        if not any(line):
            # print(f"No galaxies at x={index}", line)
            lines = [line[:index] + [line[index]] + line[index:] for line in lines]
            index += 1
        index += 1
    # print("X post:", len(lines[0]))
        
    return lines

# Get coords of where galaxies are
def get_galaxy_coords(lines: List[bool]) -> List[tuple]:
    out = []
    for y, list in enumerate(lines):
        for x, bool in enumerate(list):
            if bool:
                out.append((x,y))
    return out

def get_dist(coord: tuple, coord2: tuple) -> int:
    return abs(abs(coord[0]-coord2[0]) + abs(coord[1] - coord2[1]))

def get_pairs(coords: List[tuple]) -> List[List[tuple]]:
    out = []
    checked = {}
    print("Getting pairs")
    for coord in tqdm(coords):
        for coord2 in coords:
            dist = get_dist(coord, coord2)
            if coord != coord2:
                if not ((coord,coord2) in checked or (coord2,coord) in checked):
                    out.append((dist, coord, coord2))
                    checked[(coord,coord2)] = True
    return out

def print_galaxies(lines: List[List[bool]])->None:
    for y in lines:
        for x in y:
            if x:
                print("#", end="")
            else:
                print(".", end="")
        print()

# Get the results needes
def get_galaxies(lines: List[str]) -> int:
    # print_galaxies(lines)
    lines = expand_galaxies(lines)
    # print_galaxies(lines)
    coords = get_galaxy_coords(lines)
    pairs = get_pairs(coords)
    return coords, pairs

if __name__ == "__main__":
    start_time = time.time()
    lines = []
    with open("smallinput.txt") as file:
        lines = [[char == "#" for char in line.strip()] for line in file.readlines()]
    
    galaxies, pairs = get_galaxies(lines)

    # print(pairs)

    num_galaxies = len(galaxies)

    sum_of_dists = 0
    for d in pairs:
        sum_of_dists += d[0]

    print("1->7",get_dist((4,0),(9,10)))
    print("3->6",get_dist((0,2),(12,7)))
    print("8->9",get_dist((0,11),(5,11)))
    print("1->2",get_dist((4,0),(9,1)))


    end_time = time.time()
    print(f"Number og galaxies: {num_galaxies}")
    print(f"Number of pairs: {len(pairs)}")
    print(f"Sum of distances: {sum_of_dists}")
    print(f"Took {((end_time-start_time)*1000):.4}ms")