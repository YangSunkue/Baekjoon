import sys
input = sys.stdin.readline

"""
슬라이딩 윈도우 + 이분탐색
"""

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

def sliding_window(length):
    """S이상 찾으면 즉시 True 리턴"""

    value = sum(numbers[:length])
    if value >= S:
        return True
    
    for i in range(length, N):
        value -= numbers[i - length]
        value += numbers[i]

        if value >= S:
            return True
        
    return False

# 이분탐색으로 수열길이 탐색
left = 1
right = N
result = 1_000_000
while left <= right:

    mid = (left + right) // 2

    if sliding_window(mid):
        result = min(result, mid)
        right = mid - 1
    else:
        left = mid + 1

if result == 1_000_000: result = 0
print(result)