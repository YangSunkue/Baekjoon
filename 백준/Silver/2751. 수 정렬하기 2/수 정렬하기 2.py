import sys
n = int(sys.stdin.readline())
d = []
for i in range(n):
    d.append(int(sys.stdin.readline().strip()))
d.sort()
for i in d:
    print(i)