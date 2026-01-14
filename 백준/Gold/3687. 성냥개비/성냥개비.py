"""
골드 2


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
def get_min_digit_count(n):
    """n개 성냥개비로 만들 수 있는 최소 자릿수"""
    if n == 0:
        return 0
    return (n + 6) // 7

cost = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def can_make(matches, digits):
    """matches개로 digits 자리를 만들 수 있는지 확인"""
    if digits == 0:
        return matches == 0
    # digits 자리를 만들수 있는 최소/최대 개수
    min_needed = digits * 2  # 전부 1로
    max_needed = digits * 7  # 전부 8로
    return min_needed <= matches <= max_needed

for _ in range(int(input())):

    N = int(input())

    # 최소값 구하기
    digit_count = get_min_digit_count(N)
    min_result = ''
    remaining = N

    for pos in range(digit_count):
        start = 1 if pos == 0 else 0

        for digit in range(start, 10):
            if can_make(remaining - cost[digit], digit_count - pos - 1):
                min_result += str(digit)
                remaining -= cost[digit]
                break
    
    if N % 2 == 1:
        max_result = '7' + '1' * ((N - 3) // 2)
    else:
        max_result = '1' * (N // 2)
    
    print(min_result, max_result)