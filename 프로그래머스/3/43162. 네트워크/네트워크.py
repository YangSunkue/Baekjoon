from collections import deque

def solution(n, computers):
    
    table = [[] for _ in range(n)]
    
    # 연결리스트 형태 변경
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
                
            if computers[i][j] == 1:
                table[i].append(j)
    
    visited = [False] * n
    
    # BFS 함수        
    def bfs(start):
        
        queue = deque([])
        queue.append(start)
        
        while queue:
            
            node = queue.popleft()
            visited[node] = True
            
            for next in table[node]:
                if not visited[next]:
                    queue.append(next)
    
    # 메인 로직
    result = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            result += 1
    
    return result