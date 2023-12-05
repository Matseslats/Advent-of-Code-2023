from typing import List
import time
start_time = time.time()

def empty_map() -> dict:
    map = {
        "conversions": []
    }

    return map

def get_maps(lines: List[str]) -> dict:
    maps = {
        "to_convert": []
    }
    nums = [int(x) for x in lines[0].split(": ")[1].split(" ")]
    maps["to_convert"] = []

    is_start_num = True
    for index, num in enumerate(nums):
        if is_start_num:
            print(num)
            maps["to_convert"].append((num, num+nums[index+1]))
            is_start_num = False
        else:
            is_start_num = True

    current_map = empty_map()
    new_map = True
    map_name = ""
    for line in lines[2:]:
        if new_map:
            # Get header
            map_name = line.split(" ")[0]
            new_map = False
            continue

        if line == "":
            # Empty line, save map to maps
            maps[map_name] = current_map
            current_map = empty_map()
            new_map = True
            continue

        # Parse map line
        dest_start, source_start, range_len = [int(x) for x in line.split(" ")]
        current_map["conversions"].append((dest_start, source_start, range_len))
    
    maps[map_name] = current_map
    current_map = empty_map()
    new_map = True
    
    return maps

def get_index_from_map(this_map, index):
    # Search though conversion ranges for this index
    for conversion in this_map["conversions"]:
        if index in range(conversion[1], conversion[1]+conversion[2]):
            return (index + conversion[0] - conversion[1])
    # None found, just return the index. It is not mapped to anything
    return index

def get_reverse_index_from_map(this_map, index):
    # Search though conversion ranges for this index
    for conversion in this_map["conversions"]:
        if index in range(conversion[0], conversion[0]+conversion[2]):
            return (index + conversion[1] - conversion[0])
    # None found, just return the index. It is not mapped to anything
    return index

if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines] # Remove newline char
    
    maps = get_maps(lines)

    loc_min = 0
    loc_max = 50_000_000
    # location = 31161857
    location = (loc_max+loc_min)/2
    found = False
    humidity = temperature = light = water = fertilizer = soil = seed = 0
    while not found:
        location = int((loc_max+loc_min)/2)
        present = False
        humidity = get_reverse_index_from_map(maps["humidity-to-location"], location)
        temperature = get_reverse_index_from_map(maps["temperature-to-humidity"], humidity)
        light = get_reverse_index_from_map(maps["light-to-temperature"], temperature)
        water = get_reverse_index_from_map(maps["water-to-light"], light)
        fertilizer = get_reverse_index_from_map(maps["fertilizer-to-water"], water)
        soil = get_reverse_index_from_map(maps["soil-to-fertilizer"], fertilizer)
        seed = get_reverse_index_from_map(maps["seed-to-soil"], soil)

        # print(location, humidity, temperature, light, water, fertilizer, soil, seed)

        for range_start, range_end in maps["to_convert"]:
            if seed in range(range_start, range_end):
                present = True
                loc_max = location-1
        
        if not present:
            loc_min = location+1
        
        if loc_min >= loc_max:
            location = loc_min
            break
    

    output = location

    print(f"Output: {output}")
    print(f"Took {time.time()-start_time}s")