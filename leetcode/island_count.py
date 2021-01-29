def island_count(*grid):
    unvisited = {(x,y)
                for (y, row) in enumerate(grid)
                for (x, char) in enumerate(row)
                if bool(int(char))}

    number_of_islands  = 0
    while unvisited:
        visit_dfs(next(iter(unvisited)), unvisited)
        number_of_islands += 1
    return number_of_islands


def neighbours(position):
    for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):
        yield position[0] + dx, position[1] + dy

def visit_dfs(position, unvisited):
    unvisited.remove(position)
    for neighbour in neighbours(position):
        if neighbour in unvisited:
            visit_dfs(neighbour, unvisited)
