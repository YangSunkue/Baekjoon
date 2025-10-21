from collections import deque

def solution(maps):
    
    """
    레버 거친 후 탈출
    
    1. 레버까지 최단거리 구하기
    2. 레버부터 출구까지 최단거리 구하기
    3. 1과 2를 더하기
    
    레버에 갈 수 없다면 -1
    레버에 갔지만, 탈출구에 갈 수 없다면 -1
    """
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]
    lex, ley = len(maps), len(maps[0])
    
    def get_start():
        for x in range(lex):
            for y in range(ley):
                if maps[x][y] == 'S':
                    return (x, y)
    
    def get_visited():
        return [[False for _ in range(ley)] for _ in range(lex)]
        
    def can_go(x, y, visited):
        if 0 <= x < lex and 0 <= y < ley and visited[x][y] == False and maps[x][y] != 'X':
            return True
        return False
    
    def BFS(sx, sy, sd, target, visited):
        
        visited[sx][sy] = True
        queue = deque([(sx, sy, sd)])
        while queue:
            
            cx, cy, cd = queue.popleft()
            
            # 레버 좌표 + 레버까지 거리 리턴
            if target == 'L' and maps[cx][cy] == target:
                return (cx, cy, cd)
            
            # 끝까지 거리 리턴
            if target == 'E' and maps[cx][cy] == target:
                return cd
            
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                
                if can_go(nx, ny, visited):
                    visited[nx][ny] = True
                    queue.append((nx, ny, cd + 1))
        
        return (0, 0, -1) if target == 'L' else -1
    
    # 레버부터 찾고
    visited = get_visited()
    sx, sy = get_start()
    lx, ly, ld = BFS(sx, sy, 0, 'L', visited)
    if ld == -1:
        return ld
    
    # 레버에서 시작하여 출구 찾기
    visited = get_visited()
    result = BFS(lx, ly, ld, 'E', visited)
    return result