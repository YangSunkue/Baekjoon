import sys
input = sys.stdin.readline

"""
1. 모든 요청을 줄 수 있다면 다 준다
2. 상한액을 정해서, 상한액 이상인 요청엔 상한액만 준다. 상한액 이하의 요청은 그대로 준다

이것도 이분탐색..?
"""

N = int(input())
reqs = list(map(int, input().split()))
budget = int(input())

def calc(limit, arr):
    """
    상한가를 고려해, 지급해야 할 금액 계산
    limit: 상한가
    """
    left = 0
    right = len(arr) - 1

    limit_idx = 0

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] >= limit:
            right = mid - 1
            limit_idx = mid
        
        else:
            left = mid + 1
    
    left_sum = sum(arr[:limit_idx])
    right_sum = limit * len(arr[limit_idx:])

    return left_sum + right_sum



if sum(reqs) <= budget:

    """예산이 충분할 경우"""
    print(max(reqs))

else:

    """예산이 부족할 경우, 상한가 기준 이분탐색"""
    reqs.sort()
    left = 1
    right = reqs[-1] - 1

    while left <= right:

        # mid는 현재 상한가
        mid = (left + right) // 2
        total = calc(mid, reqs)

        # 예산이 딱 맞는다면 바로 리턴 (최적 상한가)
        if total == budget:
            right = mid
            break

        elif total > budget:
            right = mid - 1

        else:
            left = mid + 1
    
    print(right)