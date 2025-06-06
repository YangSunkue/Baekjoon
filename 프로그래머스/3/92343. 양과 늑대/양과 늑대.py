from collections import defaultdict, deque

def solution(info, edges):
    
    """인접 딕셔너리 만들기 (부모 -> 자식 단방향)"""
    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)
    
    """큐 기본값 설정"""
    # list는 삭제/탐색연산 느려서 set 쓴다
    # 어차피 상태관리 visited로 하고 완전탐색이라 순서 상관없기에 set
    queue = deque([(1, 0, set(graph[0]))])
    
    visited = set()
    max_sheep = 1  # 루트 노드는 무조건 양이다. 최소 1마리
    
    """메인 BFS 로직"""
    while queue:
        sheep, wolf, possible = queue.popleft()
        
        # 이미 방문한 상태라면 continue
        state = (sheep, wolf, tuple(sorted(possible)))
        if state in visited:
            continue
        visited.add(state)
        
        # 양 최대 마릿수 갱신
        max_sheep = max(max_sheep, sheep)
        
        # 양, 늑대 노드 나누기
        sheep_nodes = [node for node in possible if info[node] == 0]
        wolf_nodes = [node for node in possible if info[node] == 1]
        
        # 양 노드는 전부 방문
        for node in sheep_nodes:
            new_possible = possible.copy()  # 내용물이 int(불변) 이므로 copy 안전
            new_possible.remove(node)  # 방문할 노드 삭제
            new_possible.update(graph[node])  # 방문 가능 노드 추가 (list여도 update에 의해 각각 set요소로 들어감)
            
            queue.append((sheep + 1, wolf, new_possible))
        
        # 늑대 노드는 안전할 경우 방문
        for node in wolf_nodes:
            if sheep > wolf + 1:
                new_possible = possible.copy()
                new_possible.remove(node)
                new_possible.update(graph[node])
                
                queue.append((sheep, wolf + 1, new_possible))
    
    return max_sheep