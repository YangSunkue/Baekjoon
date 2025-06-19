import sys
input = sys.stdin.readline

N, K = map(int, input().split())

medals = []
for _ in range(N):
    country, *medal = map(int, input().split())
    medal.append(country)  # 국가 번호 추가해서 저장
    medals.append(medal)

# 순위대로 정렬
medals.sort(key = lambda x: (x[0], x[1], x[2]), reverse=True)

# 공동 순위를 고려해 정확한 순위 부여
medals[0].append(1)
prev = medals[0]
for i in range(1, N):

    # 메달이 같을 경우 동순위 부여
    if prev[:3] == medals[i][:3]:
        medals[i].append(prev[-1])
    
    # 다음 순위 부여
    else:
        medals[i].append(i + 1)
        prev = medals[i]


for medal in medals:
    if medal[-2] == K:
        print(medal[-1])
        break