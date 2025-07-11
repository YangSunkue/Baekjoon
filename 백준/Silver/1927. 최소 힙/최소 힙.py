import heapq
import sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):

    num = int(input())
    if num == 0:
        if not heap:
            print(num)
        else:
            print(heapq.heappop(heap))
    
    elif num >= 1:
        heapq.heappush(heap, num)