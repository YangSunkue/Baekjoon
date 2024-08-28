import sys
input = sys.stdin.readline

number = [int(input()) for _ in range(28)]
number.sort()

for i in range(1, 31):
    if i not in number:
        print(i)