from collections import deque
import sys

input = sys.stdin.readline
N, E = map(int, input().split())  # 노드, 간선
indegree = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    root, edge = map(int, input().split())  # 연결정보 입력받기
    graph[root].append(edge)  
    indegree[edge] += 1  # 진입차수 + 1

def topological():
    queue = deque()
    result = []

    for i in range(1, N + 1):  # 진입차수 확인하여 0인 노드 큐에 삽입
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        here = queue.popleft()  # 큐에서 노드 꺼내기
        result.append(here)  # 꺼낸 노드 결과 리스트에 삽입 ( 큐에서 꺼낸 순서대로 위상 순서이다 )

        for i in graph[here]:  # 현재 노드 연결정보에 대하여 반복한다
            indegree[i] -= 1  # 간선을 끊어준다
            if indegree[i] == 0:  # 끊었는데 진입차수가 0이라면 큐에 삽입한다
                queue.append(i)
            
    return result  # 모든 노드 돌았으면 결과 반환

result = topological()
for re in result:
    print(re, end=' ')