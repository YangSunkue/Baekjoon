import sys
input = sys.stdin.readline

# N일, K만큼 감소
N, K = map(int, input().split())
# 키트의 근육 증가량
kit = list((map(int, input().split())))
for i in range(len(kit)):
    kit[i] -= K

visited = [False] * N

cnt = 0
def dfs(depth, sum):
    global cnt

    if depth == N:
        cnt += 1
        return
    
    for i in range(N):
        if not visited[i] and sum + kit[i] >= 0:
            visited[i] = True
            dfs(depth + 1, sum + kit[i])
            visited[i] = False

dfs(0, 0)
print(cnt)