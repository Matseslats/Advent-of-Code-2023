import time
import tqdm

def init_graph(lines):
    graph = {}
    for y,_ in enumerate(lines):
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
    return graph


def print_dists(distances, lines):
    for y,_ in enumerate(lines):
        for x,char in enumerate(lines[y]):
            if char == "#":
                print("    .", end="")
            elif char == "S":
                print("    S", end="")
            elif (x,y) in distances:
                print(f"{distances[(x,y)]:5}", end="")
            else:
                print("    -", end="")
        print()


def get_dist(distances, dist):
    count = 0
    for space in distances:
        if distances[space] <= dist and (dist % 2 == distances[space] % 2):
            count += 1
    return count


if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    start_time = time.time()

    graph = init_graph(lines)
    distances = {graph["S"]: 0}
    current_spaces = set()
    current_spaces.add(graph["S"])
    for i in tqdm.tqdm(range(240)):
        new_spaces = set()
        for space in current_spaces:
            for neighbor in graph[space]:
                if neighbor not in distances:
                    distances[neighbor] = distances[space] + 1
                new_spaces.add(neighbor)
        
        current_spaces = new_spaces

    print_dists(distances, lines)

    pt1 = pt2 = 0
    pt1 = get_dist(distances, 64)

    end_time = time.time()
    print(f"Solution Pt1: {pt1}")
    print(f"Solution Pt2: {pt2}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
