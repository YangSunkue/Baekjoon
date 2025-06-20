import sys
input = sys.stdin.readline

"""
사방이 쿠키인 위치가 심장
"""
""" 심장 좌표를 찾는 함수"""
def find_heart(N, cookie):
    # 심장은 처음과 마지막 행/열에는 존재하지 않는다
    for x in range(1, N - 1):
        for y in range(1, N - 1):

            # 사방이 쿠키면 심장이다
            if cookie[x][y] == '*' and cookie[x-1][y] == '*' and cookie[x+1][y] == '*' and cookie[x][y-1] == '*' and cookie[x][y+1] == '*':
                return (x, y)

"""심장을 기준으로 왼팔/오른팔/허리 길이를 구하는 함수"""
def count_upper_length(heart, direction, N, cookie):

    """
    최대 반복횟수
    왼쪽: y좌표
    오른쪽: N - (y좌표+1)
    아래쪽: N - (x좌표+1)
    """
    x, y = heart
    count = 0

    if direction == 'left':
        for i in range(1, y+1):
            if cookie[x][y - i] != '*':
                break
            count += 1

    elif direction == 'right':
        for i in range(1, (N-(y+1))+1):
            if cookie[x][y + i] != '*':
                break
            count += 1

    elif direction == 'down':
        for i in range(1, (N-(x+1))+1):
            if cookie[x + i][y] != '*':
                break
            count += 1
    
    return count

"""쿠키의 왼쪽/오른쪽 다리 길이를 구하는 함수"""
def count_leg_length(mid_lower_idx, direction, N, cookie):

    idx = tuple()
    count = 0

    if direction == 'left':
        idx = (mid_lower_idx[0] + 1, mid_lower_idx[1] - 1)
    elif direction == 'right':
        idx = (mid_lower_idx[0] + 1, mid_lower_idx[1] + 1)
    
    for i in range(N - idx[0]):
        if cookie[idx[0] + i][idx[1]] != '*':
            break
        count += 1
    
    return count
                
N = int(input())
cookie = [list(input().strip()) for _ in range(N)]
heart = find_heart(N, cookie)

left_arm = count_upper_length(heart, 'left', N, cookie)
right_arm = count_upper_length(heart, 'right', N, cookie)
mid = count_upper_length(heart, 'down', N, cookie)
left_leg = count_leg_length((heart[0] + mid, heart[1]), 'left', N, cookie)
right_leg = count_leg_length((heart[0] + mid, heart[1]), 'right', N, cookie)

length = []
length.append(left_arm)
length.append(right_arm)
length.append(mid)
length.append(left_leg)
length.append(right_leg)

print(heart[0] + 1, heart[1] + 1)
print(*length)