def solution(edges):
    
    """
    차수 1: 막대 그래프의 끝점 (막대 그래프당 2개)
    차수 2: 8자 그래프의 일반점들 / 도넛 그래프의 모든 정점
    차수 4: 8자 그래프의 중심점 (8자 그래프당 1개)
    
    입차는 없고 출차가 2 이상 : 생성된 정점
    생성된 정점의 출차수 : 총 그래프 개수
    
    -> 생성된 정점, 막대 그래프의 끝점, 8자 그래프의 중심점은 degree 정보로 특정 가능
    -> 차수 1, 차수4 정점 개수를 세서 막대/8자 그래프 개수 특정
    -> 총 그래프 수 - 막대+8자 그래프 수 = 도넛 그래프 수
    
    단, 생성된 정점과 연결된 정점의 입차수를 1빼야 한다.
    -> 예외 처리 : 고립된 막대 그래프
    -> 차수가 0인 정점은, 막대 그래프이다.
    """
    
    """각 정점의 입/출차수를 계산한다"""
    in_degree = dict()
    out_degree = dict()
    
    for a, b in edges:
        out_degree[a] = out_degree.get(a, 0) + 1
        in_degree[b] = in_degree.get(b, 0) + 1
        out_degree.setdefault(b, 0)
        in_degree.setdefault(a, 0)
    
    """생성된 정점을 찾는다"""
    created_node = -1
    for node in in_degree:
        if in_degree[node] == 0 and out_degree[node] >= 2:
            created_node = node
            
    # 총 그래프 수는 생성된 정점의 출차수 개수
    total_graphs = out_degree[created_node]
    
    """생성 정점과 연결된 정점의 입차수를 1 깎는다"""
    for a, b in edges:
        if a == created_node:
            in_degree[b] -= 1
    
    """차수0, 차수1, 차수4 정점 개수를 센다"""
    solo_node = 0
    stick_ends = 0
    eight_centers = 0
    
    for node in in_degree:
        if node == created_node:
            continue
        
        # 정점의 총 차수
        total_degree = in_degree[node] + out_degree[node]
        
        if total_degree == 0:
            solo_node += 1
        elif total_degree == 1:
            stick_ends += 1
        elif total_degree == 4:
            eight_centers += 1
    
    """각 그래프 수를 계산한다"""
    stick = solo_node + (stick_ends // 2)
    eight = eight_centers
    donut = total_graphs - (stick + eight)
    
    return [created_node, donut, stick, eight]