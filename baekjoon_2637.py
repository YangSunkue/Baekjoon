from collections import deque
import sys

input = sys.stdin.readline
N = int(input())  # 노드(부품) 개수
E = int(input())  # 간선 개수
indegree = [0 for _ in range(N + 1)]  # 진입차수 담을 리스트
needs = [[0] * (N + 1) for _ in range(N + 1)]  # 부품별 요구부품량 담을 리스트
graph = [[] for _ in range(N + 1)]  # 연결정보 담을 리스트
for _ in range(E):
    leaf, root, money = map(int, input().split())
    graph[root].append([leaf, money])
    indegree[leaf] += 1

def toy():
    queue = deque()
    for i in range(1, N + 1):  # 진입차수 0인 노드들 큐에 삽입(기본부품들)
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        here = queue.popleft()  # 큐에서 노드 빼기
        for next, need in graph[here]:  # 현재노드 인접리스트에 대하여 반복
            if sum(needs[here]) == 0:  # 현재노드가 기본부품일 경우( 기본부품은 요구량이 없다 )
                needs[next][here] += need
            else:  # 현재노드가 중간부품일 경우
                for i in range(1, N + 1): # 중간부품의 모든 필요부품을 훑으며, 완성품의 중간부품 필요량만큼 일일이 곱해서 추가해준다
                    needs[next][i] += needs[here][i] * need
            
            indegree[next] -= 1  # 간선 지우기
            if indegree[next] == 0:  # 간선 지웠는데 진입차수 0 되면 큐에 삽입하기
                queue.append(next)


toy()
for i in range(1, N + 1):
    if needs[N][i] >= 1:  # 완성품의 필요부품 리스트에 기본부품이 존재할 경우 출력 ( 기본부품이 4개가 아닐 수도 있다 )
        print(f'{i} {needs[N][i]}')