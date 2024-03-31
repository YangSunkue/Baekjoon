from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
indegree = [0 for _ in range(N + 1)]  # 진입차수를 저장할 리스트, 값은 0으로 초기화해 둔다
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    root, edge = map(int, input().split())
    graph[root].append(edge)  # 연결정보 저장
    indegree[edge] += 1  # 진입차수 + 1

def topological():
    queue = deque()
    result = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        node = queue.popleft()  # 큐에서 노드 빼기
        result.append(node)  # 뺀 노드 결과에 저장 ( 큐에서 빠지는 순서가 위상 순서이다 )

        for i in graph[node]:  # 해당 노드와 연결된 노드들에 대한 반복
            indegree[i] -= 1  # 간선 지워준다
            if indegree[i] == 0:  # 만약 진입차수가 0이 되었다면 큐에 삽입
                queue.append(i)

    return result

print(topological())


# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4