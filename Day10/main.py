from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
import time
from typing import List
from PIL import Image, ImageColor
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import sys
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

sys.setrecursionlimit(15000)

@dataclass
class graphVertex:
    """Class for keeping track of graph vertices"""
    symbol: str
    distance: int
    out_edges = []
    parent = None
    coords = None
    used_in_max_depth = False
    visited = False
    potentially_enclosed = False
    child = None
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.distance = None
        self.out_edges = []
    
    def __str__(self):
        return f'{self.symbol}'

    def setPotentially_enclosed(self, bool):
        if not self.visited:
            self.potentially_enclosed = True

def is_in_range(coord, max_w, max_h):
    x, y = coord
    if x >= 0 and x < max_w and y >= 0 and y < max_h:
        # vertex.out_edges.append(coord)
        return True
    else:
        return False

def get_graph(lines: List[str]):
    graph = {}
    graph["nodes"] = {}
    graph["height"] = len(lines)
    graph["width"] = len(lines[0])
    graph["start"] = None
    graph["farthest"] = None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            vertex = graphVertex(char)
            vertex.coords = (x,y)
            if char == "|":
                vertex.out_edges.append((x ,  y-1))
                vertex.out_edges.append((x,   y+1))
            elif char == "-":
                vertex.out_edges.append((x-1, y  ))
                vertex.out_edges.append((x+1, y  ))
            elif char == "L":
                vertex.out_edges.append((x,   y-1))
                vertex.out_edges.append((x+1, y  ))
            elif char == "J":
                vertex.out_edges.append((x,   y-1))
                vertex.out_edges.append((x-1, y  ))
            elif char == "7":
                vertex.out_edges.append((x,   y+1))
                vertex.out_edges.append((x-1, y  ))
            elif char == "F":
                vertex.out_edges.append((x,   y+1))
                vertex.out_edges.append((x+1, y  ))
            elif char == "S":
                graph["start"] = (x,y)
                if is_in_range((x,   y+1), graph["width"], graph["height"]) and lines[y+1][x] in "J|L":
                    vertex.out_edges.append((x,   y+1))
                if is_in_range((x,   y-1), graph["width"], graph["height"]) and lines[y-1][x] in "F|7":
                    vertex.out_edges.append((x,   y-1))
                if is_in_range((x+1, y  ), graph["width"], graph["height"]) and lines[y][x+1] in "J-7":
                    vertex.out_edges.append((x+1, y  ))
                if is_in_range((x-1, y  ), graph["width"], graph["height"]) and lines[y][x-1] in "F-L":
                    vertex.out_edges.append((x-1, y  ))

            graph["nodes"][(x,y)] = vertex
    
    return graph

def print_graph(graph, dist=False):
    print(f"Start at {graph['start']}")
    for y in range(graph["height"]):
        for x in range(graph["width"]):
            char_to_print = ''
            node = graph["nodes"].get((x,y))
            if node == None:
                char_to_print = '.'
            else:
                if dist:
                    char_to_print = node.distance
                    if char_to_print == None:
                        char_to_print = '.'
                else:
                    char_to_print = node.__str__()
            print(char_to_print, end="")
        print()

    # print(graph["nodes"][graph["start"]].out_edges)

def bfs(graph):
    max_depth = 0
    queue = []
    start_node = graph["nodes"][graph["start"]]
    start_node.distance = 0
    queue.append(start_node)
    while len(queue) != 0:
        u = queue.pop(0) # Dequeue
        # print(u)
        for coord in u.out_edges:
            # print(coord)
            v = graph["nodes"][coord]
            # print(v)
            if v.distance == None:
                v.distance = u.distance +1
                if v.distance > max_depth:
                    max_depth = max(max_depth, v.distance)
                    graph["farthest"] = coord
                    # print(f"Max depth: {max_depth:20} at {coord}")
                v.parent = u
                queue.append(graph["nodes"][coord])
        
        # print()

    v = graph["nodes"][graph["farthest"]]
    while v is not None:
        v.used_in_max_depth = True
        v = v.parent
    return max_depth


def create_nipy_spectral_cmap(num_steps=256):
    cmap = plt.get_cmap('nipy_spectral', num_steps)
    return cmap

def generate_color_from_gradient(value, min_value, max_value, cmap):
    normalized_value = (value - min_value) / (max_value - min_value)
    r,g,b,a = cmap(normalized_value)
    return (int(r*255), int(g*255), int(b*255), int(a*255))

def png_graph(graph, width, height, max):
    cmap = create_nipy_spectral_cmap()
    im = Image.new('RGBA', (width,height)) # create the Image of size 1 pixel 
    im.putpixel((0,0), ImageColor.getcolor('black', 'RGBA')) # or whatever color you wish
    for y in range(graph["height"]):
        for x in range(graph["width"]):
            color = (0, 0, 0)
            node = graph["nodes"].get((x, y))
            if node is not None:
                if node.distance is not None:
                    color = generate_color_from_gradient(node.distance, 0, max, cmap)
                    if not node.used_in_max_depth:
                        color = (color[0], color[1], color[2], 50)
            # if len(node.out_edges) == 0:
            #     color = (100,100,100,255)
            im.putpixel((x, y), color)  # directly use the RGB tuple

    im.putpixel(graph["start"], (255,0,0,255))
    im.putpixel(graph["farthest"], (0,0,255,255))

    # v = graph["nodes"][graph["farthest"]]
    # while v is not None:
    #     im.putpixel(v.coords, (255,255,255,255))
    #     v = v.parent

    im.save('simplePixel.png') # or any image format

# Go through the graph clockwise, set all nodes on starboard (if not visited) as potentially enclosed
def png_dfs_graph(graph, width, height, max_depth, out="part2.png"):
    cmap = create_nipy_spectral_cmap()
    im = Image.new('RGBA', (width,height)) # create the Image of size 1 pixel 
    for y in range(graph["height"]):
        for x in range(graph["width"]):
            color = (0, 0, 0,0)
            node = graph["nodes"].get((x, y))
            if node is not None:
                if node.visited:
                    color = generate_color_from_gradient(node.distance, -1, max_depth, cmap)
                    # color = (150,150,150,255)
                    # color = (255,255,255,255)
                    # if not node.used_in_max_depth:
                    #     color = (color[0], color[1], color[2], 50)
            if len(node.out_edges) == 0:
                color = (0,0,0,255)
            # if node.potentially_enclosed:
            #     color = (200, max(color[1]-100,0), max(color[2]-100,0), color[3])
            im.putpixel((x, y), color)  # directly use the RGB tuple

    # im.putpixel(graph["start"], (0,255,0,255))
    # im.putpixel(graph["farthest"], (0,0,255,255))

    # v = graph["nodes"][graph["farthest"]]
    # while v is not None:
    #     im.putpixel(v.coords, (255,255,255,255))
    #     v = v.parent

    im.save(out) # or any image format


def dfs(graph, u, depth=0, nodes=[]):
    for coord in u.out_edges:
        v = graph["nodes"][coord]
        if v.visited == False:
            nodes.append(v.coords)
            v.potentially_enclosed = False
            v.parent = u
            u.child = v
            v.visited = True
            v.distance = depth
                
            graph, depth, nodes = dfs(graph, v, depth+1, nodes)

    return graph, depth, nodes

def polygonArea(vertices):
    #A function to apply the Shoelace algorithm
    numberOfVertices = len(vertices)
    sum1 = 0
    sum2 = 0

    for i in range(0,numberOfVertices-1):
        sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
        sum2 = sum2 + vertices[i][1] *  vertices[i+1][0]

    #Add xn.y1
    sum1 = sum1 + vertices[numberOfVertices-1][0]*vertices[0][1]   
    #Add x1.yn
    sum2 = sum2 + vertices[0][0]*vertices[numberOfVertices-1][1]   

    area = abs(sum1 - sum2) / 2
    return area

if __name__ == "__main__":
    start_time = time.time()
    lines = []
    with open("maininput.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    
    graph = get_graph(lines)

    original_graph = deepcopy(graph)

    bfs_graph = deepcopy(graph)
    max_depth = bfs(bfs_graph)
    png_graph(bfs_graph, graph["width"], graph["height"], max_depth)


    dfs_graph, max_length, nodes = dfs(deepcopy(graph), graph["nodes"][graph["start"]])
    png_dfs_graph(dfs_graph, graph["width"], graph["height"], max_length)

    polygon = Polygon(nodes)



    end_time = time.time()
    print(f"Max depth: {max_depth}. Max length: {max_length}. Contains {polygon.area - max_length/2 + 1} points")
    print(f"Took {((end_time-start_time)*1000):.4}ms")