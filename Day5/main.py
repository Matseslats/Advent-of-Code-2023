from typing import List

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

    print(maps["to_convert"])
    current_map = empty_map()
    new_map = True
    map_name = ""
    for line in lines[2:]:
        if new_map:
            # Get header
            map_name = line.split(" ")[0]
            print(map_name)
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

if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines] # Remove newline char
    
    maps = get_maps(lines)

    min_location = 100000000000000
    for range_start, range_end in maps["to_convert"]:
        print(range_start, range_end)
        for seed in range(range_start, range_end):
            soil = get_index_from_map(maps["seed-to-soil"], seed)
            fertilizer = get_index_from_map(maps["soil-to-fertilizer"], soil)
            water = get_index_from_map(maps["fertilizer-to-water"], fertilizer)
            light = get_index_from_map(maps["water-to-light"], water)
            temperature = get_index_from_map(maps["light-to-temperature"], light)
            humidity = get_index_from_map(maps["temperature-to-humidity"], temperature)
            location = get_index_from_map(maps["humidity-to-location"], humidity)

            min_location = min(min_location, location)
        print(min_location)

    
    print(min_location)

    output = min_location

    print(f"Output: {output}")