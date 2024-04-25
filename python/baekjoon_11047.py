N, money = map(int, input().split())  # 동전 종류, 돈

coinBox = []
for _ in range(N):
    coinBox.append(int(input()))

coinBox.reverse()
cnt = 0
for coin in coinBox:  # 큰 동전부터 차례로 대입된다
    if money >= coin:
        cnt += money // coin
        money = money % coin

print(cnt)