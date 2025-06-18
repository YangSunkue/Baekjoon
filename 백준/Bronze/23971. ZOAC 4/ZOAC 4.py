import math
"""
H: 행
W: 열

각 참가자별 띄워야 할 칸
N: 세로 칸
M: 가로 칸
"""
H, W, N, M = map(int, input().split())

# 가로, 세로 사람 수를 구해서 곱하기
y_person = math.ceil(H / (N+1))
x_person = math.ceil(W / (M+1))

print(y_person * x_person)