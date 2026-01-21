"""
실버 1
그리디
"""
from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

heapify(data)
for _ in range(M):

    one = heappop(data)
    two = heappop(data)

    heappush(data, one + two)
    heappush(data, one + two)

print(sum(data))