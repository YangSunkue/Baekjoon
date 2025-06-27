import sys
input = sys.stdin.readline

N = int(input())
reqs = list(map(int, input().split()))
budget = int(input())

reqs.sort()
left = 1
right = max(reqs)
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    total = 0
    for req in reqs:
        if req > mid:
            total += mid
        else:
            total += req
    
    if total <= budget:
        answer = mid 
        left = mid + 1
    else:
        right = mid - 1

print(answer)