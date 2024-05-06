import sys
input = sys.stdin.readline

# 일수, 일 근육 감소량
N, K = map(int, input().split())

# 키트별 근육 증가량
kit = list(map(int, input().split()))
for i in range(N):
    kit[i] -= K

# 결과 경우의 수를 담을 변수
cnt = 0

# 방문 체크 리스트
visited = [False] * N

# 백트래킹 진행
def backTraking(depth, sum):

    global cnt

    # 최대 깊이에 도달했다면 cnt + 1
    if depth == N:
        cnt += 1
        return
    
    for i in range(N):
        if not visited[i] and sum + kit[i] >= 0:
            visited[i] = True
            backTraking(depth + 1, sum + kit[i])
            visited[i] = False

backTraking(0, 0)
print(cnt)