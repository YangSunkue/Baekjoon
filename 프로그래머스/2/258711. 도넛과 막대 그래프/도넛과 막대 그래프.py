def solution(edges):
    
    """
    차수 0: 독립된 막대 그래프
    차수 1: 막대 그래프 양 끝 점
    차수 2: 도넛 그래프, 8자 그래프 일부
    차수 3: 없음 또는 생성된 정점
    차수 4: 8자 그래프 중앙 점
    
    입차수 0이고 출차수 2이상: 생성된 정점
    생성된 정점의 출차수: 총 그래프 수
    
    모든 정점의 입/출차수를 전부 구해서 저장
    생성된 정점 특정, 생성된 정점과 연결된 정점들 입차수 1씩 줄이기
    
    각 그래프 별 차수를 이용해 , 모든 정점 순회하며 그래프 분류
    """
    
    in_degree = dict()
    out_degree = dict()
    
    for a, b in edges:
        in_degree[b] = in_degree.get(b, 0) + 1
        out_degree[a] = out_degree.get(a, 0) + 1
        in_degree.setdefault(a, 0)
        out_degree.setdefault(b, 0)
    
    created_node = -1
    for node in in_degree:
        if in_degree[node] == 0 and out_degree[node] >= 2:
            created_node = node
            break
    total_graphs = out_degree[created_node]
    
    for a, b in edges:
        if a == created_node:
            in_degree[b] -= 1
    
    solo_node = 0
    stick_ends = 0
    eight_centers = 0
    
    for node in in_degree:
        if node == created_node:
            continue
            
        total_degree = in_degree[node] + out_degree[node]

        if total_degree == 0:
            solo_node += 1
        elif total_degree == 1:
            stick_ends += 1
        elif total_degree == 4:
            eight_centers += 1
            
    stick = solo_node + (stick_ends // 2)
    eight = eight_centers
    donut = total_graphs - (stick + eight)
    
    return [created_node, donut, stick, eight]