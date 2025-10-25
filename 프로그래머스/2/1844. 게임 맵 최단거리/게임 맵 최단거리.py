from collections import deque

def solution(maps):
    """
    0: 벽
    1: 길
    """
    
    def can_go(x, y):
        if 0 <= x < n and 0 <= y < m and maps[x][y] == 1 and not visited[x][y]:
            return True
        return False
    
    # 행, 열
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 1)])  # 시작 좌표 삽입 (x, y, 거리)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        cx, cy, cd = queue.popleft()
        
        # 상대방 진영에 도착했을 경우 종료
        if cx == (n - 1) and cy == (m - 1):
            return cd
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if can_go(nx, ny):
                queue.append((nx, ny, cd + 1))
                visited[nx][ny] = True
    
    return -1