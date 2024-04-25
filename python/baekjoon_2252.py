from collections import deque
import sys

input = sys.stdin.readline
N, E = map(int, input().split())  # 노드, 간선 입력받기
indegree = [0 for _ in range(N + 1)]  # 진입차수 저장할 리스트
graph = [[] for _ in range(N + 1)]  # 연결정보 저장할 리스트
for _ in range(E):  # 연결정보 입력받기
    root, edge = map(int, input().split())
    graph[root].append(edge)
    indegree[edge] += 1  # 진입차수 추가하기

def solve():
    queue = deque()  # 덱 사용
    result = []

    for i in range(1, N + 1):  # 진입차수가 0인 노드를 큐에 삽입
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:  # 큐에서 노드 꺼내기, 결과 리스트에 담기 (  큐에서 꺼내진 순서대로 위상 순서 )
        here = queue.popleft()
        result.append(here)

        for i in graph[here]:  # 현재 노드에 연결된 간선 끊기
            indegree[i] -= 1
            if indegree[i] == 0:  # 끊었는데 진입차수가 0이면 큐에 삽입한다
                queue.append(i)
    
    return result

result = solve()
for re in result:  # 결과 출력
    print(re, end=' ')