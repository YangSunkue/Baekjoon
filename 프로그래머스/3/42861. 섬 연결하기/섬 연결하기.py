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
    
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    
    result = 0
    for cost in costs:
        
        x, y, c = cost[0], cost[1], cost[2]
        
        xroot = find(parent, x)
        yroot = find(parent, y)
        
        if xroot == yroot:
            continue
        
        union(parent, rank, x, y)
        result += c
    
    return result