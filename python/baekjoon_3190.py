import sys
from collections import deque

n = int(sys.stdin.readline())  # 보드의 크기
k = int(sys.stdin.readline())  # 사과의 개수
apple = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]  # 사과의 위치

l = int(sys.stdin.readline())  # 방향 전환 횟수
change = []
for _ in range(l):
    changeSec, changeDir = input().split()
    changeSec = int(changeSec)
    change.append([changeSec, changeDir])

diList = ['' for _ in range(change[-1][0] + 1)] # 인덱스와 초를 맞추기 위해 + 1
for i in change:
    diList[i[0]] = i[1]  # di의 i번 인덱스가 초, i번의 데이터는 방향

# 0, 1, 2, 3 => 북, 동, 남, 서
# whereCount % 4 의 값에 따라 방향을 전환한다
# whereCount 값은 D면 + 1 , L이면 - 1
# 0 -> x-1 / 1 -> y+1 / 2 -> x+1 / 3 -> y-1
whereCount = 1

sec = 0 # 결과 저장(초)
snake = deque()
snake.append((1,1)) # 시작 위치 저장
while True:
    sec += 1
    # 현재 방향에 따라 1칸 진행
    if whereCount % 4 == 1:
        if (snake[-1][0], snake[-1][1] + 1) in snake: # 자기자신과 부딪힌다면 탈락
            break
        else:
            snake.append((snake[-1][0], snake[-1][1] + 1))
    elif whereCount % 4 == 2:
        if (snake[-1][0] + 1, snake[-1][1]) in snake: # 자기자신과 부딪힌다면 탈락
            break
        else:
            snake.append((snake[-1][0] + 1, snake[-1][1]))
    elif whereCount % 4 == 3:
        if (snake[-1][0], snake[-1][1] - 1) in snake: # 자기자신과 부딪힌다면 탈락
            break
        else:
            snake.append((snake[-1][0], snake[-1][1] - 1))
    else:
        if (snake[-1][0] - 1, snake[-1][1]) in snake: # 자기자신과 부딪힌다면 탈락
            break
        else:
            snake.append((snake[-1][0] - 1, snake[-1][1]))

    # 진행했는데 벽에 닿으면 탈락
    if snake[-1][0] > n or snake[-1][0] <= 0 or snake[-1][1] > n or snake[-1][1] <= 0:
        break
    
    if list(snake[-1]) not in apple: # 진행했는데 사과가 없을 때 꼬리를 자른다
        snake.popleft()
    else: # 사과를 먹으면 사과를 없앤다
        apple.remove(list(snake[-1]))

    # 초+방향 리스트는 마지막 방향전환 초 + 1 만큼의 길이이기 때문에, 현재 초가 더 길어지면 방향전환하지 않는다.
    if len(diList) > sec:
        if diList[sec] == 'L':
            whereCount -= 1
        elif diList[sec] == 'D':
            whereCount += 1

print(sec)