def get_power(dict):
    product = 1
    for color in dict:
        product *= dict[color]
    
    return product

def is_solvable(line):
    MAX = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    parts = line.split(": ")
    game_no = parts[0].split(" ")[1]
    print("Game: ", game_no)

    draw_piles = parts[1].split("; ")
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
            MAX[color] = max(MAX[color], current[color])
        
    return get_power(MAX)

if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.readlines()
    

    sum = sum([is_solvable(x.strip()) for x in lines])

    print(f"Sum: {sum}")