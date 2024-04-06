import sys

input = sys.stdin.readline

N = int(input())
talkList = []
for _ in range(N):
    talkList.append(list(map(int, input().split())))

talkList.sort(key = lambda x: (x[1], x[0]))

diff = talkList[0][1]
cnt = 1
for i in range(1, N):  # 회의 하나씩 반복
    if diff <= talkList[i][0]:
        cnt += 1
        diff = talkList[i][1]

print(cnt)

# [[0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]