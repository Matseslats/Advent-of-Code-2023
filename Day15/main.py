import time
from collections import OrderedDict
import re

def get_focal_power(boxes):
    sum = 0
    for key in boxes:
        for index, inner_key in enumerate(boxes[key]):
            sum += (key+1) * (index+1) * boxes[key][inner_key]
    return sum


def update_box(in_arr, boxes):
    # SPlit at either = or -
    parts = re.split(r'[-=]', in_arr)
    value = None
    hashval = get_hash(parts[0])
    if parts[1] != '':
        value = int(parts[1])
        if hashval not in boxes:
            boxes[hashval] = OrderedDict()
        boxes[hashval][parts[0]] = value
    else:
        if hashval in boxes and parts[0] in boxes[hashval]:
            del boxes[hashval][parts[0]]
    
    return boxes

def get_hash(in_arr):
    hash = 0
    for c in in_arr:
        # Add ascii value of each char
        hash += ord(c)
        hash *= 17
        hash %= 256
    #     print(c, ord(c), hash)
    # print(in_arr, hash)
    return hash

if __name__ == "__main__":
    start_time = time.time()
    in_array = []
    with open("input.txt") as file:
        in_array = file.readline().strip().split(",")

    hashes = [get_hash(line) for line in in_array]

    boxes = {}
    for part in in_array:
        boxes = update_box(part, boxes)
    
    focal_power = get_focal_power(boxes)

    end_time = time.time()
    print(f"Solution Pt1: {sum(hashes)}")
    print(f"Solution Pt2: {focal_power}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
