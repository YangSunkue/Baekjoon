# 골드5 -> 그리디, 자료구조, 정렬, 우선순위 큐

import heapq
import sys
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort()

# 첫번째 시작하는 수업의 종료시간을 저장
# 종료시간은 우선순위가 됨
pq = []
heapq.heappush(pq, data[0][1])

for i in range(1, N):
    # 다음 수업과 진행중인 수업이 중복되지 않을 경우 진행중 수업 빼기
    if data[i][0] >= pq[0]:
        heapq.heappop(pq)
    heapq.heappush(pq, data[i][1])

print(len(pq))