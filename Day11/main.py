import time
from typing import List
from tqdm import tqdm

# Expand empty lines
def expand_galaxies(lines: List[bool], scale=1):
    # print("Y pre:", len(lines))
    expand_x = {}
    expand_y = {}
    index = 0
    print("Expanding y")
    for y, line in enumerate(lines):
        if not any(line):
            expand_y[y] = scale
        #     # print(f"No galaxies at y={index}", line)
        #     lines = lines[:index] + [line] + lines[index:]
        #     index += 1
        # index += 1
    # print("Y post:", len(lines))
    
    # print()

    # print("X pre:", len(lines[0]))
    index = 0
    print("Expanding x")
    for x, _ in enumerate(lines[0]):
        line = [line[x] for line in lines]
        if not any(line):
            expand_x[x] = scale
            # for i in range(scale):
            #     # print(f"No galaxies at x={index}", line)
            #     lines = [line[:index] + [line[index]] + line[index:] for line in lines]
            #     index += 1
        # index += 1
    # print("X post:", len(lines[0]))
        
    print(expand_x, expand_y)
    return lines, expand_x, expand_y

# Get coords of where galaxies are
def get_galaxy_coords(lines: List[bool]) -> List[tuple]:
    out = []
    for y, list in enumerate(lines):
        for x, bool in enumerate(list):
            if bool:
                out.append((x,y))
    return out


# print("8->9",get_dist((0,11),(5,11), {2: 1, 5: 1, 8: 1}, {3: 1, 7: 1})) = 5
def get_dist(coord: tuple, coord2: tuple, expand_x: dict, expand_y: dict) -> int:
    dist = abs(abs(coord[0]-coord2[0]) + abs(coord[1] - coord2[1]))
    # print(dist)
    for check_x in range(coord[0], coord2[0]):
        if expand_x.get(check_x) is not None:
            # print("Adding")
            dist += expand_x[check_x]
    
    for check_y in range(coord[1], coord2[1]):
        if expand_y.get(check_y) is not None:
            # print("Adding")
            dist += expand_y[check_y]

    return dist

def get_pairs(coords: List[tuple], expand_x: dict, expand_y: dict) -> List[List[tuple]]:
    out = []
    checked = {}
    print("Getting pairs")
    for coord in tqdm(coords):
        for coord2 in coords:
            dist = get_dist(coord, coord2, expand_x, expand_y)
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
    print_galaxies(lines)
    lines, expand_x, expand_y = expand_galaxies(lines, 1)
    # print_galaxies(lines)
    coords = get_galaxy_coords(lines)
    pairs = get_pairs(coords, expand_x, expand_y)
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

    # print("1->7",get_dist((3,0),(7,8), {2: 1, 5: 1, 8: 1}, {3: 1, 7: 1}))
    # print("3->6",get_dist((0,2),(9,6), {2: 1, 5: 1, 8: 1}, {3: 1, 7: 1}))
    # print("8->9",get_dist((0,10),(4,10), {2: 1, 5: 1, 8: 1}, {3: 1, 7: 1}))
    # print("1->2",get_dist((3,0),(7,1), {2: 1, 5: 1, 8: 1}, {3: 1, 7: 1}))


    end_time = time.time()
    print(f"Number og galaxies: {num_galaxies}")
    print(f"Number of pairs: {len(pairs)}")
    print(f"Sum of distances: {sum_of_dists}")
    print(f"Took {((end_time-start_time)*1000):.4}ms")