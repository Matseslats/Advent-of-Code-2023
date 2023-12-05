from typing import List

def empty_map() -> dict:
    map = {}
    for i in range(100):
        map[i] = i

    return map

def get_maps(lines: List[str]) -> dict:
    maps = {
        "to_convert": []
    }
    maps["to_convert"] = [int(x) for x in lines[0].split(": ")[1].split(" ")]
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
            print(current_map)
            maps[map_name] = current_map
            current_map = empty_map()
            new_map = True
            continue

        # Parse map line
        dest_start, source_start, range_len = [int(x) for x in line.split(" ")]
        for i in range(range_len):
            current_map[source_start+i] = dest_start+i

        print(line)
    
    print(current_map)
    maps[map_name] = current_map
    current_map = empty_map()
    new_map = True
    
    return maps

if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines] # Remove newline char
    
    maps = get_maps(lines)

    min_location = 100000000000000
    for seed in maps["to_convert"]:
        soil = maps["seed-to-soil"][seed]
        fertilizer = maps["soil-to-fertilizer"][soil]
        water = maps["fertilizer-to-water"][fertilizer]
        light = maps["water-to-light"][water]
        temperature = maps["light-to-temperature"][light]
        humidity = maps["temperature-to-humidity"][temperature]
        location = maps["humidity-to-location"][humidity]

        min_location = min(min_location, location)

        print(location)
    
    print(min_location)

    output = min_location

    print(f"Output: {output}")