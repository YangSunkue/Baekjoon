from heapq import heappush, heappop
import sys
input = sys.stdin.readline

"""
    보석 N개
    무게 M
    가격 V

    가방 K개
    최대무게 C
    가방 한 개당 한 개의 보석만 넣을 수 있다
"""

# 보석개수, 가방개수
N, K = map(int, input().split())

gems = []  # [(무게, 가격), (무게, 가격), ...]
for _ in range(N):
    M, V = map(int, input().split())
    gems.append((M, V))
gems.sort(key=lambda x: x[0])  # 무게 낮은 순 정렬

bags = []  # [최대무게, 최대무게, 최대무게, ...]
for _ in range(K):
    C = int(input())
    bags.append(C)
bags.sort()                    # 무게 낮은 순 정렬

result = 0
max_heap = []
gems_idx = 0
for bag in bags:

    for i in range(gems_idx, N):
        # 보석이 가방보다 무거우면 break
        if gems[i][0] > bag:
            gems_idx = i
            break

        heappush(max_heap, (-gems[i][1], gems[i][0]))  # (-가격, 무게) -> 비싼 걸 먼저 pop

    # 보석이 전부 힙에 담겼을 경우
    else:
        gems_idx = N


    # 현재 가방에 담을 수 있는 보석 중 가장 비싼 것 pop
    if not max_heap:
        continue
    price, weight = heappop(max_heap)

    result += -price

print(result)