import sys
input = sys.stdin.readline

K, N = map(int, input().split())
data = [int(input()) for _ in range(K)]

start = 1
end = max(data)
while start <= end:

    mid = (start + end) // 2
    count = 0

    for lan in data:
        count += lan // mid
    
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)