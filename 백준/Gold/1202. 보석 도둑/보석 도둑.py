from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

gems.sort(key=lambda x: x[0])
bags.sort()

result = 0
max_heap = []
gems_idx = 0
for bag in bags:
    
    for i in range(gems_idx, N):
        if bag < gems[i][0]:
            gems_idx = i
            break

        heappush(max_heap, -gems[i][1])
    
    else:
        gems_idx = N
    
    if max_heap:
        result += -heappop(max_heap)

print(result)