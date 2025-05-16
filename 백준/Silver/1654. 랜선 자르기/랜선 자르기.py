import sys
input = sys.stdin.readline

K, N = map(int, input().split())
data = [int(input()) for _ in range(K)]

start = 1
end = max(data)

while start <= end:

    mid = (start + end) // 2
    count = 0

    for i in data:
        count += i // mid
    
    if count < N:
        end = mid - 1

    else:
        start = mid + 1

print(end)