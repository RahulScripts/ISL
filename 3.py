# A* pathfinding on a simple grid (0 = free, 1 = obstacle)

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
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(pos):
    x, y = pos
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            yield (nx, ny)

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current_cost, current = heapq.heappop(open_set)

        if current == goal:
            # reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for nbr in neighbors(current):
            tentative_g = current_cost + 1
            if tentative_g < g_score.get(nbr, float('inf')):
                g_score[nbr] = tentative_g
                priority = tentative_g + heuristic(nbr, goal)
                heapq.heappush(open_set, (priority, tentative_g, nbr))
                came_from[nbr] = current
    return None

if __name__ == "__main__":
    path = a_star(start, goal)
    print("Path:", path)
