from collections import defaultdict, deque

def solution(n, wires):
    """
    어떤 간선이든 1개 끊으면 송전탑 2개로 분할됨
    
    인접 리스트 만들기
    
    wires 반복
        wire 인접리스트에서 제거
        bfs 및 송전탑 개수세기, 절댓값 구해서 result 갱신
        wire 인접리스트에 다시 추가
    """
    def get_visited(n):
        return [False for i in range(n + 1)]  # 1 based
    
    def get_diff(visited):
        a = n - visited.count(True)
        b = n - a
        return abs(a - b)
    
    def BFS(start):
        
        queue = deque([start])
        visited = get_visited(n)
        
        while queue:
            
            cur_node = queue.popleft()
            
            for adj_node in graph[cur_node]:
                if not visited[adj_node]:
                    queue.append(adj_node)
                    visited[adj_node] = True
        
        return get_diff(visited)
    
    graph = defaultdict(list)
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    
    result = float('inf')
    for s, e in wires:
        graph[s].remove(e)
        graph[e].remove(s)
        
        diff = BFS(1)
        result = min(result, diff)
        
        graph[s].append(e)
        graph[e].append(s)
    
    return result