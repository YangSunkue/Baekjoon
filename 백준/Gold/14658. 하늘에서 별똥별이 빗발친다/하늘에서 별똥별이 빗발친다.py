import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(K)]

x_idxs = set()
y_idxs = set()
for x, y in stars:
    x_idxs.add(x)
    y_idxs.add(y)

result = 0
for x1 in x_idxs:
    for y1 in y_idxs:

        count = 0
        for x, y in stars:
            if x1 <= x <= (x1 + L) and y1 <= y <= (y1 + L):
                count += 1
        result = max(result, count)

print(K - result)