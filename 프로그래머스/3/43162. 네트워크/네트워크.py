from collections import defaultdict, deque

def solution(n, computers):
    
    def BFS(start):
        
        queue = deque([start])
        visited.add(start)
        
        while queue:
            
            cur_node = queue.popleft()
            
            for adj_node in adj_list[cur_node]:
                if adj_node not in visited:
                    queue.append(adj_node)
                    visited.add(adj_node)
    
    # 인접 행렬 -> 인접 리스트 변환
    adj_list = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                adj_list[i].append(j)
    
    visited = set()
    result = 0
    for node in range(n):
        if node not in visited:
            BFS(node)
            result += 1
    
    return result