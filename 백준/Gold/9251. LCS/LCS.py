a = [[]]  # dp테이블과 인덱스를 동기화하기 위해 빈 리스트를 추가한다.
b = [[]]

for i in list(input()):
    a.append(i)
for i in list(input()):
    b.append(i)

# 0행과 0열 값을 모두 0으로 맞춰준다.
# 첫번째 비교부터 공식을 적용하려면 이전 값이 존재해야 하기 때문에 맞춰주는 것.
dp = [[0 for _ in range(len(a))] for _ in range(len(b))]

for x in range(1, len(b)):
    for y in range(1, len(a)):
        if b[x] == a[y] :  # 문자열이 일치할 경우
            dp[x][y] = dp[x-1][y-1] + 1  # 좌측위 방향 값에서 +1 더한 값
        else:  # 문자열이 일치하지 않으면
            dp[x][y] = max(dp[x][y-1], dp[x-1][y])  # 왼쪽, 위쪽 중 큰 값

print(dp[-1][-1])