from collections import defaultdict, deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):

    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))

    adj_list = defaultdict(list)
    indegree = [0] * (N + 1)

    for _ in range(K):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        indegree[e] += 1
    
    W = int(input())
    
    distances = [0] * (N + 1)
    queue = deque([])

    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            distances[i] = times[i]
    
    while queue:

        cur = queue.popleft()

        for adj_node in adj_list[cur]:
            distances[adj_node] = max(distances[adj_node], distances[cur] + times[adj_node])

            indegree[adj_node] -= 1
            if indegree[adj_node] == 0:
                queue.append(adj_node)
    
    print(distances[W])