MAX = {
    "red": 12,
    "blue": 14,
    "green": 13
}

def is_solvable(line):
    parts = line.split(": ")
    game_no = parts[0].split(" ")[1]
    print("Game: ", game_no)

    draw_piles = parts[1].split("; ")
    possible = True
    for draw_pile in draw_piles: # Set of draws
        current = {
            "red": 0,
            "blue": 0,
            "green": 0
        }

        draws = draw_pile.split(", ")
        for draw in draws: # Number and color of each draw
            num, color = draw.split(" ")
            num = int(num)
            current[color] += num
            # print(draw)
        
        # print(current)
        for color in current:
            if current[color] > MAX[color]:
                possible = False
        
    if possible:
        print(line)
        return int(game_no)
    return 0

if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
    

    sum = sum([is_solvable(x.strip()) for x in lines])

    print(f"Sum: {sum}")