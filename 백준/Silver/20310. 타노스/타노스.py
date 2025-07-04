import sys
input = sys.stdin.readline

"""
0이 앞에 최대한 많아야 한다

1은 앞부터 지우고
0은 뒤부터 지우면 되지않나

1. 리스트로 받아서 , 지우지 말고 -1로 교체 (지우는 연산 오버헤드 방지)
2. 앞부터 -1이 아닐 경우 출력
"""

S = list(map(int, input().strip()))

"""0, 1 개수 세기"""
count = [0] * 2  # 0의 개수, 1의 개수 저장할 리스트
for num in S:
    if num == 0:
        count[0] += 1
    else:
        count[1] += 1

"""앞부터 1 지우기"""
deleted_one = 0
for i in range(len(S)):
    if S[i] == 1:
        S[i] = -1
        deleted_one += 1

    if deleted_one >= (count[1] // 2):
        break

"""뒤부터 0 지우기"""
deleted_zero = 0
for i in range(len(S) - 1, -1, -1):
    if S[i] == 0:
        S[i] = -1
        deleted_zero += 1

    if deleted_zero >= (count[0] // 2):
        break

result = ''.join(str(x) for x in S if x != -1)
print(result)