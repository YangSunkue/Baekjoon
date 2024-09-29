# 이분 탐색
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
test = [int(input()) for _ in range(N)]

# 이분 탐색
def binarySearch():

    start = min(test)
    end = max(test) * M
    result = end

    while start <= end:

        mid = (start + end) // 2
        total = 0

        # 임의의 시간 동안 몇명을 심사하는지 계산
        for i in range(N):
            total += mid // test[i]

        # 전부 또는 더 많이 심사했을 경우
        if total >= M:
            end = mid - 1
            result = min(result, mid) # 최소시간 갱신

        # 덜 심사했을 경우       
        else:
            start = mid + 1

    return result

print(binarySearch())