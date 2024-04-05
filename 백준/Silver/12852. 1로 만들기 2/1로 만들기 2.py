import sys
input = sys.stdin.readline

x = int(input())
d = [0] * (x + 1)
path = ['' for _ in range(x + 1)]
path[1] = '1'

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    prev = i - 1

    if i % 3 == 0 and d[i // 3] + 1 < d[i]:
        d[i] = d[i // 3] + 1
        prev = i // 3
    
    if i % 2 == 0 and d[i // 2] + 1 < d[i]:
        d[i] = d[i // 2] + 1
        prev = i // 2
    path[i] = str(i) + " " + path[prev]

print(d[x])
print(path[x])