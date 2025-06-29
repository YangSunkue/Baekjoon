import sys
input = sys.stdin.readline

"""
1. 1 ~ N 까지 공백없이 이어서 썼다.
2. 수의 일부가 지워졌고, 부분수열만 남았다.
3. 이 부분수열을 만족하는 최소 N을 구하자.
"""

S = input().strip()

s_idx = 0
n = 1

while s_idx < len(S):

    num = str(n)

    for digit in num:
        if s_idx < len(S) and S[s_idx] == digit:
            s_idx += 1
    
    if s_idx >= len(S):
        break

    n += 1

print(n)