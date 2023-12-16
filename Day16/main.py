import time

def print_grid(grid):
    for y,_ in enumerate(grid):
        for x,_ in enumerate(grid[0]):
            if grid[y][x] == 0:
                print('.',end="")
            else:
                print("#",end="")
        print()


def get_new_dir(char, dir):
    if char == '.':
        return [dir]
    if char == '/':
        if dir == 'N':
            return ['E']
        elif dir == 'E':
            return ['N']
        elif dir == 'S':
            return ['W']
        elif dir == 'W':
            return ['S']
    elif char == '\\':
        if dir == 'N':
            return ['W']
        elif dir == 'E':
            return ['S']
        elif dir == 'S':
            return ['E']
        elif dir == 'W':
            return ['N']
    elif char == '|':
        if dir == 'E' or dir == 'W':
            return ['N', 'S']
        else:
            return [dir]
    elif char == '-':
        if dir == 'N' or dir == 'S':
            return ['E', 'W']
        else:
            return [dir]
    else:
        print("Unknown char", char)


def simulate(grid):
    beams = [{
        "x": 0,
        "y": 0,
        "dir": 'E'
    }]
    energies = [[0 for y in range(len(grid[0]))] for x in range(len(grid))]

    visits= {}
    while len(beams) > 0:
        # Loop through pointers
        beam = beams.pop(0)
        # print(len(beams), beam)
        beam_tuple = (beam['x'], beam['y'], beam['dir'])
        if visits.get(beam_tuple) != None:
            # print("Looped", beam_tuple)
            continue
        visits[beam_tuple] = True
        if beam['x'] >= 0 and beam['x'] < len(grid[0]) and beam['y'] >= 0 and beam['y'] < len(grid):
            # Update the energy in the grid
            energies[beam['y']][beam['x']] += 1
            # Update the position of the beam
            new_dirs = get_new_dir(grid[beam['y']][beam['x']], beam['dir'])
            for new_dir in new_dirs:
                new_beam = {
                    'x': beam['x'],
                    'y': beam['y'],
                    'dir': new_dir
                }
                if new_dir == 'N':
                    new_beam['y'] -= 1
                elif new_dir == 'E':
                    new_beam['x'] += 1
                elif new_dir == 'S':
                    new_beam['y'] += 1
                elif new_dir == 'W':
                    new_beam['x'] -= 1
                beams.append(new_beam)


    return energies



def count_energies(energies):
    energized = 0
    for y,_ in enumerate(energies):
        for x,_ in enumerate(energies[0]):
            if energies[y][x] > 0:
                energized += 1
    return energized


if __name__ == "__main__":
    grid = []
    with open("input.txt") as file:
        grid = [line.strip() for line in file.readlines()]

    start_time = time.time()

    energies = simulate(grid)

    energized = count_energies(energies)

    end_time = time.time()
    print(f"Solution Pt1: {energized}")
    print(f"Solution Pt2: {0}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
