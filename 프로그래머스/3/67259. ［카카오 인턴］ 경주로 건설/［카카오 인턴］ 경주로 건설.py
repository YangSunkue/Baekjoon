from collections import deque

def solution(board):

    """
    visited 3차원 리스트 x y direction
    큐에 (x, y, 이전방향, cost)
    """

    def can_go(nx, ny):
        """
            갈수 있는 좌표라면 True
        """
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            return True
        return False
    
    def calculate_cost(prev_direction, direction, cost):
        """
            직선이면 100, 코너면 600 추가
        """
        if prev_direction == -1 or (prev_direction - direction) % 2 == 0:
            return cost + 100
        else:
            return cost + 600
    
    def is_should_update(nx, ny, direction, new_cost):
        """
            방문하지 않았거나, 더 효율적인 경로면 True
        """
        if visited[nx][ny][direction] == 0 or visited[nx][ny][direction] > new_cost:
            return True
        return False

    
    n = len(board)
    visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    queue = deque([(0, 0, -1, 0)])  # x, y, 이전방향, cost
    result = float('inf')
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 좌 상 우 하

    while queue:

        cx, cy, prev_direction, cost = queue.popleft()

        # 4방향 진행
        for direction, (dx, dy) in enumerate(directions):
            nx, ny = cx + dx, cy + dy

            if not can_go(nx, ny):
                continue

            new_cost = calculate_cost(prev_direction, direction, cost)

            # 목적지 도착했다면 결과 갱신
            if (nx, ny) == (n - 1, n - 1):
                result = min(result, new_cost)
                continue

            if is_should_update(nx, ny, direction, new_cost):
                queue.append((nx, ny, direction, new_cost))
                visited[nx][ny][direction] = new_cost
    
    return result