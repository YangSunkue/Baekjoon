import sys
input = sys.stdin.readline

"""
-3 -2 -1 1 2 3 4
-5 -3 -1 1 2 3

합이 0보다 크면 -> right 줄이기
합이 0보다 작으면 -> left 올리기
"""

N = int(input())
liquid = list(map(int, input().split()))

def get_diff_from_zero(value):
    return 0 + abs(value)


diff = int(1e10)
result = None

left = 0
right = N - 1
while left < right:

    value = liquid[left] + liquid[right]
    cur_diff = get_diff_from_zero(value)

    if value == 0:
        result = (liquid[left], liquid[right])
        break

    elif value > 0:
        if cur_diff < diff:
            diff = cur_diff
            result = (liquid[left], liquid[right])
        right -= 1

    elif value < 0:
        if cur_diff < diff:
            diff = cur_diff
            result = (liquid[left], liquid[right])
        left += 1

print(*result)