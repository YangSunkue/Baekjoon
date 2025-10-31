from heapq import heappush, heappop

def solution(land, height):

    def can_go(nx, ny):
        return 0 <= nx < le and 0 <= ny < le and not visited[nx][ny]

    le = len(land)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = []
    heappush(queue, (0, 0, 0))
    visited = [[False] * le for _ in range(le)]

    result = 0
    while queue:
        cost, cx, cy = heappop(queue)

        if visited[cx][cy]:
            continue
        visited[cx][cy] = True

        result += cost

        for _, (dx, dy) in enumerate(directions):
            nx, ny = cx + dx, cy + dy

            if can_go(nx, ny):
                temp_cost = abs(land[cx][cy] - land[nx][ny])

                if temp_cost > height:
                    new_cost = temp_cost
                else:
                    new_cost = 0
                
                heappush(queue, (new_cost, nx, ny))
    
    return result