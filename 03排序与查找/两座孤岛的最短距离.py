from collections import deque
def find_islands(grid):
    islands = []
    visited = set()
    rows, cols = len(grid), len(grid[0])

    def bfs(r, c):
        island = set()
        queue = deque([(r, c)])
        while queue:
            x, y = queue.popleft()
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1" and (x, y) not in visited:
                island.add((x, y))
                visited.add((x, y))
                queue.append((x + 1, y))
                queue.append((x - 1, y))
                queue.append((x, y + 1))
                queue.append((x, y - 1))
        return island

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                island = bfs(r, c)
                if island:
                    islands.append(island)

    return islands


def shortest_bridge(grid):
    islands = find_islands(grid)
    bridge_length = float('inf')

    for i in range(len(islands)):
        for j in range(i + 1, len(islands)):
            bridge_length = min(bridge_length, find_bridge(islands[i], islands[j], grid))

    return bridge_length


def find_bridge(island1, island2, grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set(island1)
    queue = deque([(x, y, 0) for x, y in island1])

    while queue:
        x, y, length = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in island2:
                return length
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] != "1":
                visited.add((nx, ny))
                queue.append((nx, ny, length + 1))

    return float('inf')


if __name__=="__main__":
    grid=[]
    for i in range(int(input())):
        l=list(input())
        grid.append(l)
print(shortest_bridge(grid))
