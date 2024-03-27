import sys

n = int(sys.stdin.readline())  # 탑의 개수
towerList = list(map(int, sys.stdin.readline().split()))  # 탑 리스트
result = [0] * n  # 결과를 저장할 리스트
stack = [] # 레이저 수신 후보 탑 목록

for i in range(n):  # 탑 개수만큼 반복
    while stack:  # 현재 탑보다 더 작은 앞 탑들 지워가며 비교하기
        if towerList[stack[-1][0]] < towerList[i]: # 후보가 더 작을 경우 지운다
            stack.pop()
            
        else: # 레이저 수신 성공 시(앞 탑이 더 클 때) 인덱스번호 + 1 해서 결과에 저장
            result[i] = stack[-1][0] + 1
            break
            
    stack.append((i, towerList[i])) # 스택에 인덱스와 높이 저장

print(*result)