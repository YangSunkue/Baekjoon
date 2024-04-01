from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
E = int(input())
indegree = [0 for _ in range(N + 1)]  # 진입차수 리스트
needs = [[0] * (N + 1) for _ in range(N + 1)]  # 부품 별 필요부품량 리스트
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    leaf, root, money = map(int, input().split())
    graph[root].append([leaf, money])  # 연결정보 저장
    indegree[leaf] += 1  # 연결될 때마다 간선 추가

def toy():
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:  # 진입차수가 0이면 큐에 추가
            queue.append(i)
    
    while queue:
        here = queue.popleft()

        for next, need in graph[here]:
            if sum(needs[here]) == 0:  # 기본부품일 경우 ( 기본부품은 필요량이 없다 )
                needs[next][here] += need  # 중간부품의 기본부품 필요량만큼 더한다
            else:  # 현재 노드가 중간부품일 경우
                for i in range(1, N + 1):
                    needs[next][i] += needs[here][i] * need  # 다음부품의 기본부품 필요량 부분에, 현재부품의 기본부품필요량과 다음부품의 현재부품 요구량을 곱해서 더한다
            indegree[next] -= 1  # 간선 지우기
            if indegree[next] == 0:  # 지웠는데 진입차수 0 되면 큐에 삽입
                queue.append(next)


toy()
for i in range(1, N + 1):
    if needs[N][i] >= 1:
        print(f'{i} {needs[N][i]}')