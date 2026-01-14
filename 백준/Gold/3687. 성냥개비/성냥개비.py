"""
골드 2

그리디

소모량: 숫자
2개: 1
3개: 7
4개: 4
5개: 2, 3, 5
6개: 0, 6, 9
7개: 8

가장 작은 수:
    그리디

가장 큰 수:
    N 짝수일경우 -> 1 꽉채우기
    N 홀수일경우 -> 7 한개 + 1꽉채우기
"""
import sys
input = sys.stdin.readline

def can_make(matches: int, digits_count: int) -> bool:
    """matches 개 성냥으로 digits_count 자릿수를 만들 수 있는가"""
    if digits_count == 0:
        return matches == 0
    # digits_count 자릿수를 만들 수 있는 최소/최대 개수
    min_needed = 2 * digits_count
    max_needed = 7 * digits_count
    return min_needed <= matches <= max_needed


cost = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for _ in range(int(input())):

    N = int(input())

    digits = (N + 6) // 7
    min_result = ''
    remaining = N

    for pos in range(digits):
        start = 1 if pos == 0 else 0

        for num in range(start, 10):
            if can_make(remaining - cost[num], digits - pos - 1):
                min_result += str(num)
                remaining -= cost[num]
                break
    
    if N % 2 == 1:
        max_result = '7' + '1' * ((N - 3) // 2)
    else:
        max_result = '1' * (N // 2)
    
    print(min_result, max_result)