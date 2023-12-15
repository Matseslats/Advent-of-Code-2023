import time
from collections import OrderedDict
import re


# Calculate the focal power of the boxes
def get_focal_power(boxes):
    sum = 0
    for key in boxes:
        for index, inner_key in enumerate(boxes[key]):
            # Calculate and accumulate the focal power using the formula
            # (key + 1) * (index + 1) * value_of_inner_key
            sum += (key+1) * (index+1) * boxes[key][inner_key]
    return sum


# Update the boxes dict with the new box
def update_box(in_arr, boxes):
    # If there is a value, add it to the dict
    if '=' in in_arr:
        parts = in_arr.split('=')
        hashval = get_hash(parts[0])
        value = int(parts[1])
        if hashval not in boxes: # If the key doesnt exst, create it
            boxes[hashval] = OrderedDict()
        boxes[hashval][parts[0]] = value
    # If there is no value, remove it from the dict
    else:
        hashval = get_hash(in_arr[:-1])
        if hashval in boxes and in_arr[:-1] in boxes[hashval]: # Check if the key exists
            del boxes[hashval][in_arr[:-1]]
    
    return boxes



# Get the hash of the input
def get_hash(in_arr):
    hash = 0
    for c in in_arr:
        # Add the ascii value of the character to the hash, multiply by 17 and mod 256
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash

if __name__ == "__main__":
    in_array = []
    with open("input.txt") as file:
        in_array = file.readline().strip().split(",")

    start_time = time.time()
    hashes = [get_hash(line) for line in in_array]

    boxes = {}
    for part in in_array:
        boxes = update_box(part, boxes)
    
    focal_power = get_focal_power(boxes)

    end_time = time.time()
    print(f"Solution Pt1: {sum(hashes)}")
    print(f"Solution Pt2: {focal_power}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
