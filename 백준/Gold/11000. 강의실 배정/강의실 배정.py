# 골드5 -> 그리디, 자료구조, 정렬, 우선순위 큐
import heapq
import sys
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort()

pq = []
heapq.heappush(pq, data[0][1]) # 가장 처음 시작한 강의의 끝나는 시간 저장 ( 우선순위가 된다 )

for i in range(1, N):
    if data[i][0] >= pq[0]: # 다음 시작하는 강의가, 가장 빨리 끝나는 강의와 겹치지 않으면 큐에서 빼준다
        heapq.heappop(pq)
    heapq.heappush(pq, data[i][1]) # 다음 시작하는 강의 큐에 넣기

print(len(pq))