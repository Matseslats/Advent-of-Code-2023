import time
import tqdm

def init_graph(lines):
    graph = {}
    for y,_ in enumerate(lines):
        for x,char in enumerate(lines[y]):
            graph[(x,y)] = []
            if x > 0 and lines[y][x-1] in ".S": # Left
                graph[(x,y)].append((x-1,y))
            if x < len(lines[y])-1 and lines[y][x+1] in ".S": # Right
                graph[(x,y)].append((x+1,y))
            if y > 0 and lines[y-1][x] in ".S": # Up
                graph[(x,y)].append((x,y-1))
            if y < len(lines)-1 and lines[y+1][x] in ".S": # Down
                graph[(x,y)].append((x,y+1))
            
            if char == "S":
                graph["S"] = (x,y)
    return graph


if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    start_time = time.time()

    graph = init_graph(lines)
    current_spaces = set()
    current_spaces.add(graph["S"])
    for i in tqdm.tqdm(range(64)):
        new_spaces = set()
        for space in current_spaces:
            for neighbor in graph[space]:
                new_spaces.add(neighbor)
        
        current_spaces = new_spaces
    # print(current_spaces)

    pt1 = pt2 = 0
    pt1 = len(current_spaces)

    end_time = time.time()
    print(f"Solution Pt1: {pt1}")
    print(f"Solution Pt2: {pt2}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
