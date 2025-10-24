"""
    최소 신장 트리
    union-find 활용, 같은 집합일 경우 연결하지 않는다.
    
    중복된 연결은 주어지지 않으며, 모든 노드를 연결해야 한다
    -> 모든 다리를 건설 시도하되, 사이클이 생길 경우 pass
"""

def find(parent, x):
    
    if parent[x] == x:
        return x
    
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def solution(n, costs):
    
    costs.sort(key = lambda x: x[2])  # 비용 오름차순 정렬
    
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    
    result = 0
    for cost in costs:
        
        x, y, c = cost[0], cost[1], cost[2]
        
        xroot = find(parent, x)
        yroot = find(parent, y)
        
        # 이미 연결되었으면 continue
        if xroot == yroot:
            continue
        
        # 다리 건설
        union(parent, rank, x, y)
        result += c
    
    return result