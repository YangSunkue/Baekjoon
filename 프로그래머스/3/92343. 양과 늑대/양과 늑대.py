from collections import defaultdict, deque

def solution(info, edges):
    
    """
    그래프 구성: 부모 -> 자식 인접 리스트
    노드를 방문했을 때, 어떤 새로운 노드들이 열리는지 알기 위함
    """
    graph = defaultdict(list)  # 왜 이건 list고
    for parent, child in edges:
        graph[parent].append(child)
    
    """
    BFS 초기 설정
    상태: (양의 수, 늑대 수, 방문 가능한 노드들의 집합)
    {1,2}
    루트 노드를 방문한 후의 초기 상태
    """
    queue = deque([(1, 0, set(graph[0]))])  # 이건 왜 set이지
    max_sheep = 1  # 최대 양의 수 (최소 1마리)
    
    """
    중복 상태 방지를 위한 visited set
    같은 상태를 여러 번 방문하는 것을 방지
    """
    visited = set()  # 이것도 왜 set?
    
    """
    메인 로직
    """
    while queue:
        # possible: {1,2}
        sheep, wolf, possible = queue.popleft()
        
        # 현재 상태를 해시 가능한 형태로 변환하여 중복 체크
        state = (sheep, wolf, tuple(sorted(possible)))  # frozenset으로 바꾸면안되나?
        if state in visited:
            continue
        visited.add(state)
        
        # 최대 양의 수 갱신
        max_sheep = max(max_sheep, sheep)
        
        # 방문 가능한 노드들을 양과 늑대로 분류
        sheep_nodes = [node for node in possible if info[node] == 0]
        wolf_nodes = [node for node in possible if info[node] == 1]
        
        # 양이 있는 노드 방문
        for node in sheep_nodes:
            new_possible = possible.copy()  # 현재 방문 가능한 노드들 복사
            new_possible.remove(node)  # 방문할 노드는 제거
            new_possible.update(graph[node])  # 방문할 노드의 자식들 추가
            
            queue.append((sheep + 1, wolf, new_possible))
        
        # 늑대 노드는 안전할 때만 방문
        for node in wolf_nodes:
            if sheep > wolf + 1:
                new_possible = possible.copy()
                new_possible.remove(node)
                new_possible.update(graph[node])
                
                queue.append((sheep, wolf + 1, new_possible))
    
    return max_sheep