from collections import deque

def solution(places):
    """
    거리 3이상 이어야 함
    단, 파티션으로 막혀있으면 허용
    
    P: 응시자
    O: 빈칸
    X: 파티션
    
    각 P를 기준으로 상하좌우 BFS(?) 하되, depth 2 까지만 간다
    -> 만약 다른 P를 만났다면 0 리턴
    -> visited 활용
    """
    
    
    def create_visited():
        """새로운 visited 리스트를 리턴한다."""
        return [[False for _ in range(5)] for _ in range(5)]
    
    def can_go(x, y, dist, place, visited):
        """진행 가능하면 True, 아니면 False 리턴한다."""
        if 0 <= x < 5 and 0 <= y < 5 and place[x][y] != 'X' and not visited[x][y] and dist <= 2:
            return True
        return False
        
    def search(sx, sy, place, visited):
        """
        맨해튼 거리 2 내에 P가 있으면 False를 리턴한다.
        X는 통과하지 않는다.
        """
        visited[sx][sy] = True
        queue = deque([(sx, sy, 0)])  # x, y, 거리
        
        while queue:
            x, y, dist = queue.popleft()
            
            # 거리 2내에 사람 있다면 False 리턴
            if 0 < dist <= 2 and place[x][y] == 'P':
                return False
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if can_go(nx, ny, dist + 1, place, visited):
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
        
        return True
        
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 5개 교실 검사
    result = []
    for place in places:
        
        # 각 응시자 기준 검사
        visited = create_visited()
        should_break = False
        for x in range(5):
            for y in range(5):
                
                # 거리두기 검사
                if place[x][y] == 'P':
                    if not search(x, y, place, visited):
                        should_break = True
                        break
                        
            if should_break:
                break
        
        # 거리두기를 지키지 않았다면 0, 지켰다면 1
        if should_break:
            result.append(0)
        else: result.append(1)
    
    return result
    