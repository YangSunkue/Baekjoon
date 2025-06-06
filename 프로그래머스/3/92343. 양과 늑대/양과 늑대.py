from collections import defaultdict, deque

def solution(info, edges):
    
    graph = defaultdict(list)
    
    for parent, child in edges:
        graph[parent].append(child)
    
    visited = set()
    max_sheep = 1
    queue = deque([(1, 0, set(graph[0]))])
    
    while queue:
        sheep, wolf, possible = queue.popleft()
        
        state = (sheep, wolf, tuple(sorted(possible)))
        if state in visited:
            continue
        visited.add(state)
        
        max_sheep = max(max_sheep, sheep)
        
        sheep_nodes = [node for node in possible if info[node] == 0]
        wolf_nodes = [node for node in possible if info[node] == 1]
        
        for node in sheep_nodes:
            new_possible = possible.copy()
            new_possible.remove(node)
            new_possible.update(graph[node])
            
            queue.append((sheep + 1, wolf, new_possible))
        
        for node in wolf_nodes:
            if sheep > wolf + 1:
                new_possible = possible.copy()
                new_possible.remove(node)
                new_possible.update(graph[node])
                
                queue.append((sheep, wolf + 1, new_possible))
        
    return max_sheep