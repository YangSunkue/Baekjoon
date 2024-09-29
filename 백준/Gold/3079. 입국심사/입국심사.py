# 이분 탐색
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 심사대 개수, 인원
test = [int(input()) for _ in range(N)] # 심사하는데 걸리는 시간

# 이분 탐색
def binarySearch():

    start = min(test)
    end = max(test) * M
    result = end

    while start <= end:

        mid = (start + end) // 2
        total = 0

        # 특정 시간(mid)에 대하여 몇 명을 심사하는지 계산한다
        for i in range(N):
            total += mid // test[i]
        
        # 전부 심사했거나 더 많이 심사했을 경우
        if total >= M:
            end = mid - 1
            result = min(result, mid) # 최적의 답을 갱신한다
        
        # 적게 심사했을 경우
        else:
            start = mid + 1

    return result

print(binarySearch())