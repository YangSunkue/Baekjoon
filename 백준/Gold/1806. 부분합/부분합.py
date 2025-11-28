import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

left = 0
cur_sum = 0
result = N + 1

for right in range(N):
    cur_sum += numbers[right]

    while cur_sum >= S:
        result = min(result, right - left + 1)
        cur_sum -= numbers[left]
        left += 1

print(0 if result == N + 1 else result)