def solution(dirs):
    
    """
    처음 걸어본 길이 구하기

    11 * 11 테이블, (5,5) 시작
    visited: (sx, sy, ex, ey) -> 출발점, 도착점
    """
    
    def can_go(x, y):
        if 0 <= x <= 10 and 0 <= y <= 10:
            return True
        return False
    
    def is_first(sx, sy, ex, ey):
        road = (sx, sy, ex, ey)
        if road in visited:
            return False
        return True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = []
    result = 0
    x, y = 5, 5
    for i in range(len(dirs)):

        direction = None
        if dirs[i] == 'U': direction = 0
        if dirs[i] == 'D': direction = 1
        if dirs[i] == 'L': direction = 2
        if dirs[i] == 'R': direction = 3

        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if can_go(nx, ny):
            if is_first(x, y, nx, ny):
                result += 1
                visited.append((x, y, nx, ny))
                visited.append((nx, ny, x, y))
            
            x = nx
            y = ny
    
    return result