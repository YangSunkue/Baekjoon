def solution(n, m, x, y, r, c, k):
    
    """
    1. 맨해튼 거리 구해서 d가 k 이하인지 확인 -> k초과면 impossible
    2. d에서 k까지 남은 이동횟수 짝수인지 확인 -> 홀수면 impossible
    
    3. 탐색시작, dlru 순서로 이동 시도 및 1,2 검증
    
    좌표검증 + 좌표 -1 
    """
    x -= 1
    y -= 1
    r -= 1
    c -= 1
    
    def get_manhatten(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    def can_go(x, y):
        return 0 <= x < n and 0 <= y < m
    
    directions = {'d': (1, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0)}
    
    distance = get_manhatten(x, y, r, c)
    if distance > k or (k - distance) % 2 == 1:
        return 'impossible'
    
    step = 0
    result = ''
    while step < k:
        
        for direction, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            
            if not can_go(nx, ny):
                continue
                
            distance = get_manhatten(nx, ny, r, c)
            if distance > k - (step + 1) or (k - (distance + step + 1)) % 2 == 1:
                continue
            
            step += 1
            x, y = nx, ny
            result += direction
            break
            
        else:
            return 'impossible'
    
    return result