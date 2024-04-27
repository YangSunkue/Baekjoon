import sys
input = sys.stdin.readline

N = int(input())
cp = []
for i in range(N):
    cp.append(list(map(int, input().split())))

# 총 거리 저장 변수, 아껴지는 거리 저장 변수
distance = 0
diff = 0

for i in range(N - 1):

    # 각 체크포인트 사이의 거리 계산
    point = abs(cp[i][0] - cp[i+1][0]) + abs(cp[i][1] - cp[i+1][1])  # i -> i + 1

    # 총 거리 계산
    distance += point

    # N은 건너뛸 수 없다
    if i == N - 2: break
    
    point2 = abs(cp[i+1][0] - cp[i+2][0]) + abs(cp[i+1][1] - cp[i+2][1])  # i + 1 -> i + 2
    point3 = abs(cp[i][0] - cp[i+2][0]) + abs(cp[i][1] - cp[i+2][1])  # i -> i + 2

    if diff < abs(point + point2) - point3:
        diff = abs(point + point2) - point3

distance -= diff

print(distance)