def find_snake(H, W, grid):
    # Helper function to get the next cell in different directions
    def get_next_cell(i, j, di, dj):
        return i + di, j + dj

    # Possible directions: down, right, diagonally down-right
    directions = [(0, 1), (1, 0), (1, 1)]
    snake = 'snuke'

    # Iterate through each cell in the grid
    for i in range(H):
        for j in range(W):
            # If the current cell contains 's'
            if grid[i][j] == snake[0]:
                # Try each direction
                for di, dj in directions:
                    found = True
                    cells = [(i+1, j+1)]
                    for k in range(1, len(snake)):
                        ni, nj = get_next_cell(i, j, di*k, dj*k)
                        # If the next cell is out of the grid or does not contain the right letter, break
                        if ni >= H or nj >= W or grid[ni][nj] != snake[k]:
                            found = False
                            break
                        cells.append((ni+1, nj+1))
                    # If we found the snake in this direction, return the cells
                    if found:
                        return cells

    return []


H, W = map(int, input().split())
grid = [input() for _ in range(H)]
cells = find_snake(H, W, grid)
for cell in cells:
    print(*cell)
