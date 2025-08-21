import sys
input = sys.stdin.readline

"""
왼쪽, 또는 오른쪽으로만 모으면 된다.
이미 끝쪽에 모여 있는 공들은 움직일 필요가 없다.
움직이는 횟수 -> (빨or파 전체 공 개수 - 빨or파 양쪽 끝에 모인 개수)
"""
N = int(input())
balls = input()

"""각 공의 개수 구하기"""
red_count = balls.count('R')
blue_count = N - red_count

"""
4가지 케이스 구하기
1. 빨간 공을 왼쪽으로 모으기
2. 빨간 공을 오른쪽으로 모으기
3. 파란 공을 왼쪽으로 모으기
4. 파란 공을 오른쪽으로 모으기
"""
cases = []

# 1. 빨간 공을 왼쪽으로 모으기
count = 0
for i in range(N):
    if balls[i] == 'R':
        count += 1
    else:
        break
cases.append(red_count - count)

# 2. 빨간 공을 오른쪽으로 모으기
count = 0
for i in range(N - 1, -1, -1):
    if balls[i] == 'R':
        count += 1
    else:
        break
cases.append(red_count - count)

# 3. 파란 공을 왼쪽으로 모으기
count = 0
for i in range(N):
    if balls[i] == 'B':
        count += 1
    else:
        break
cases.append(blue_count - count)

# 4. 파란 공을 오른쪽으로 모으기
count = 0
for i in range(N - 1, -1, -1):
    if balls[i] == 'B':
        count += 1
    else:
        break
cases.append(blue_count - count)

print(min(cases))