from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 인접 리스트로 변환
adj_list = defaultdict(list)
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    
    for j in range(1, N + 1):
        if i == j:
            continue

        if data[j - 1] == 1:
            adj_list[i].append(j)

travel = list(map(int, input().split()))  # 여행 경로
visited = set()

queue = deque([travel[0]])
visited.add(travel[0])
while queue:
    cur_node = queue.popleft()

    for adj_node in adj_list[cur_node]:
        if adj_node in visited:
            continue

        visited.add(adj_node)
        queue.append(adj_node)

travel = set(travel)
for t in travel:
    if t not in visited:
        print('NO')
        break
else:
    print('YES')