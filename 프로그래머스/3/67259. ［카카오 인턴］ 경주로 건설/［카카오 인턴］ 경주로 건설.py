from collections import deque

def solution(board):
    
    def can_go(nx, ny):
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            return True
        return False
    
    def calculate_cost(prev_direction, direction, cost):
        if prev_direction == -1 or (prev_direction - direction) % 2 == 0:
            return cost + 100
        else:
            return cost + 600
    
    def is_should_update(nx, ny, direction, new_cost):
        if visited[nx][ny][direction] == 0 or visited[nx][ny][direction] > new_cost:
            return True
        return False
    
    n = len(board)
    visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    queue = deque([(0, 0, -1, 0)])
    result = float('inf')
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    while queue:
        cx, cy, prev_direction, cost = queue.popleft()
        if (cx, cy) == (n - 1, n - 1):
            result = min(result, cost)
            continue
        
        for direction, (dx, dy) in enumerate(directions):
            nx, ny = cx + dx, cy + dy
            
            if can_go(nx, ny):
                new_cost = calculate_cost(prev_direction, direction, cost)
                
                if is_should_update(nx, ny, direction, new_cost):
                    queue.append((nx, ny, direction, new_cost))
                    visited[nx][ny][direction] = new_cost
    
    return result