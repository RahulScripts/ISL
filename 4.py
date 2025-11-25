# Greedy Best-First Search (uses only heuristic, not path cost)

import heapq

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(pos):
    x, y = pos
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            yield (nx, ny)

def greedy_best_first(start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), start))
    came_from = {}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for nbr in neighbors(current):
            if nbr not in visited:
                heapq.heappush(open_set, (heuristic(nbr, goal), nbr))
                came_from[nbr] = current
    return None

if __name__ == "__main__":
    print("Path:", greedy_best_first(start, goal))
