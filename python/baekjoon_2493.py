import sys

n = int(sys.stdin.readline()) # 탑 개수
towerList = list(map(int, sys.stdin.readline().split())) # 탑 목록
result = [0] * n # 결과 리스트
stack = [] # 후보 탑을 저장할 스택

for i in range(n):
    while stack:
        if towerList[stack[-1][0]] < towerList[i]:  # stack의 후보가 현재 탑보다 낮으면 pop 한다
            stack.pop()
        else:
            result[i] = stack[-1][0] + 1  # stack의 후보가 레이저를 받으면 result에 추가한다
            break

    stack.append((i, towerList[i])) # 현재 탑을 stack에 추가한다 ( 다음 탑이랑 또 비교해야 하니까 )

print(*result)