from typing import List
import time

def get_diffs(seq: List[int]) -> List[int]:
    diffs = []
    for index,num in enumerate(seq):
        if index >= len(seq)-1:
            continue
        difference = seq[index+1]-seq[index]
        diffs.append(difference)
    return diffs

def get_next(seq: List[int]) -> int:
    transforms = [seq]
    derivative_zeroes = False
    while not derivative_zeroes:
        diffs = get_diffs(seq)
        derivative_zeroes = not any(diffs)
        transforms.append(diffs)
        seq = diffs
    
    # print(transforms)

    offset = 0
    for t in reversed(transforms):
        # print(t[-1], end=" ")
        t.append(t[-1]+offset)
        # print(offset, end=" ")
        # print(t[-1])
        offset = t[-1]
    

    return offset

if __name__ == "__main__":
    start_time = time.time()
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [[int(n) for n in line.strip().split(" ")] for line in lines] # Get ints split by spaces
    
    next_vals = [get_next(line) for line in lines]


    end_time = time.time()
    print(f"Sum of next vals: {sum(next_vals)}. Next vals: {next_vals}")
    print(f"Took {((end_time-start_time)*1000):.4}ms")