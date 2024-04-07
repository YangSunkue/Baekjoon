# 1. 일치하지 않는다면, [x-1][y], [x][y-1] 중 더 큰 값을 입력한다.
# 2. 일치한다면, [x-1][y-1] 값에서 +1한 값을 입력한다.
a1 = input()  # ACAYKP
b1 = input()  # CAPCAK  -> ACAK

a = [[] for _ in range(len(a1) + 1)]
b = [[] for _ in range(len(b1) + 1)]
for i in range(1, len(a)):
    a[i] = a1[i-1]

for i in range(1, len(b)):
    b[i] = b1[i-1]

# 첫번째 줄 부터 공식을 적용하기 위해 길이를 1 늘린다
dp =  [[0 for _ in range(len(a))] for _ in range(len(b))]
for x in range(1, len(b)):
    for y in range(1, len(a)):
        if b[x] == a[y]:  # 값이 같다면
            dp[x][y] = dp[x-1][y-1] + 1
        else:  # 값이 다르다면
            dp[x][y] = max(dp[x-1][y], dp[x][y-1])

print(dp[-1][-1])