from heapq import heappop, heappush
import time

# Pt 1 help from https://www.youtube.com/watch?v=2pDSooPLLkI

def solve(grid):
    seen = set()

    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, n = heappop(pq) # Heat loss, row, col, dir row, dir col, steps taken this dir

        if r == len(grid) -1 and c == len(grid[0]) -1:
            return hl

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))

        if n < 3 and (dr, dc) != (0,0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n+1))
        
        for ndr, ndc in [(0, 1), (1, 0), (0,-1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))


if __name__ == "__main__":
    grid = []
    with open("input.txt") as file:
        grid = [[int(char) for char in line.strip()] for line in file.readlines()]

    start_time = time.time()
    loss_pt1 = solve(grid)

    end_time = time.time()
    print(f"Solution Pt1: {loss_pt1}")
    # print(f"Solution Pt2: {max_energized}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")