import sys
input = sys.stdin.readline

N, K = map(int, input().split())

medals = [[] for _ in range(N)]
for _ in range(N):
    country, *medal = map(int, input().split())
    medals[country - 1] = medal

# 순위대로 정렬
medals.sort(key = lambda x: (x[0], x[1], x[2]), reverse=True)

# 공동 순위를 고려해 정확한 순위 부여
medals[0].append(1)
prev = medals[0]
for i in range(1, N):

    # 메달이 같을 경우 동순위 부여
    if prev[:3] == medals[i]:
        medals[i].append(prev[-1])
    
    # 다음 순위 부여
    else:
        medals[i].append(prev[-1] + 1)
        prev = medals[i]

print(medals[K-1][-1])