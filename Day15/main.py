import time

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

    end_time = time.time()
    print(f"Solution Pt1: {sum(hashes)}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
