def max_region(grid):
    unvisited = {(x,y)
                for (x, row) in enumerate(grid)
                for (y, char) in enumerate(row)
                if bool(char)}

    region = []
    while unvisited:
        size = []
        visit_dfs(next(iter(unvisited)), unvisited, size)
        region.append(sum(size))
    return max(region) + 1

def neighbours(position):
    for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1):
        yield position[0] + dx, position[1] + dy

def visit_dfs(position, unvisited, size):
    unvisited.remove(position)
    for neighbour in neighbours(position):
        if neighbour in unvisited:
            size.append(1)
            visit_dfs(neighbour, unvisited, size)


def main():
    grid = [[1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 0]]

    grid2 = [[1, 0, 1, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0]]

    print (max_region(grid2))


if __name__ == "__main__":
    main()
