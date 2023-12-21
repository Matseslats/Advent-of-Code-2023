import time
import tqdm
import numpy as np

def init_graph(lines):
    graph = {}
    y = 0
    for _ in tqdm.tqdm(lines):
        for x,char in enumerate(lines[y]):
            graph[(x,y)] = []
            if x > 0 and lines[y][x-1] in ".S": # Left
                graph[(x,y)].append((x-1,y))
            elif x == 0 and lines[y][-1] in ".S":
                graph[(x,y)].append((len(lines[y])-1,y))
            if x < len(lines[y])-1 and lines[y][x+1] in ".S": # Right
                graph[(x,y)].append((x+1,y))
            elif x == len(lines[y])-1 and lines[y][0] in ".S":
                graph[(x,y)].append((0,y))
            if y > 0 and lines[y-1][x] in ".S": # Up
                graph[(x,y)].append((x,y-1))
            elif y == 0 and lines[-1][x] in ".S":
                graph[(x,y)].append((x,len(lines)-1))
            if y < len(lines)-1 and lines[y+1][x] in ".S": # Down
                graph[(x,y)].append((x,y+1))
            elif y == len(lines)-1 and lines[0][x] in ".S":
                graph[(x,y)].append((x,0))
            
            if char == "S":
                graph["S"] = (x,y)
        y += 1
    return graph


def print_dists(distances, lines, filename):
    with open(filename, "w") as file:
        for y,_ in enumerate(lines):
            for x,char in enumerate(lines[y]):
                if char == "#":
                    file.write("    .")
                elif char == "S":
                    file.write("    S")
                elif (x,y) in distances:
                    file.write(f"{distances[(x,y)]:5}")
                else:
                    file.write("    -")
            file.write("\n")
    # for y,_ in enumerate(lines):
    #     for x,char in enumerate(lines[y]):
    #         if char == "#":
    #             print("    .", end="")
    #         elif char == "S":
    #             print("    S", end="")
    #         elif (x,y) in distances:
    #             print(f"{distances[(x,y)]:5}", end="")
    #         else:
    #             print("    -", end="")
    #     print()


def get_dist(distances, dist):
    count = 0
    for space in distances:
        # space_dist = distances[space]
        # while space_dist > 0:
            if distances[space] <= dist and (dist % 2 == distances[space] % 2):
                count += 1
            # space_dist -= 2
    return count


if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = [line.strip().replace("S", ".") for line in file.readlines()]

    start_time = time.time()

    original_rows = len(lines)
    original_cols = len(lines[0])

    tile_width = 39

    tiled_lines = [
        [lines[y % original_rows][x % original_cols] for x in range(tile_width * original_cols)]
        for y in range(tile_width * original_rows)
    ]

    # Example: Print the result
    # for row in tiled_lines:
    #     print(row)

    print("Init graph")
    graph = init_graph(tiled_lines)
    graph["S"] = (len(tiled_lines)//2, len(tiled_lines[0])//2)
    print("Done init graph")
    distances = {graph["S"]: 0}
    current_spaces = set()
    current_spaces.add(graph["S"])
    for i in tqdm.tqdm(range(140)):
        new_spaces = set()
        for space in current_spaces:
            for neighbor in graph[space]:
                if neighbor not in distances:
                    distances[neighbor] = distances[space] + 1
                new_spaces.add(neighbor)
        
        current_spaces = new_spaces

    # print_dists(distances, lines, "dists.txt")

    pt1 = pt2 = 0
    pt1 = get_dist(distances, 64)

    i = 0
    with open("pt2", "w") as file:
        for _ in range(150):
            file.write(f"{i}, {get_dist(distances, i)}\n")
            i += 1

    end_time = time.time()
    print(f"Solution Pt1: {pt1}")
    print(f"Solution Pt2: {pt2}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
