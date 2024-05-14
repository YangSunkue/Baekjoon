import sys
input = sys.stdin.readline

# N : 포켓몬 종류
# P : 포켓몬
# M : P에 대한 총 사탕 개수
# K : P를 진화시키기 위해 필요한 사탕 개수
# 진화시킬 수 있는 총 마릿수 , 가장 많이 진화시킨 포켓몬 출력
# 총 마릿수가 동일할 경우 일찍 나타는 애 출력하면 됨. max < 마릿수
# 진화시키면 사탕 2개 추가로 줌

N = int(input())
monster = []
KM = []

for i in range(N):
    monster.append(input().strip())
    KM.append(list(map(int, input().split())))

upgrade = 0
maxCount = int(-1e9)
maxMonster = ''
for i in range(N):
    candy = KM[i][1]  # 가지고 있는 사탕 개수
    count = 0 # 포켓몬별로 몇번 진화시켰는지

    while(True):
        if candy >= KM[i][0]:  # 필요 수 보다 가진 사탕이 같거나 많으면
            candy -= KM[i][0] - 2
            upgrade += 1
            count += 1
        else: break
    if count > maxCount:
        maxCount = count
        maxMonster = monster[i]
    
print(upgrade)
print(maxMonster)