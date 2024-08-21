import sys
input = sys.stdin.readline

N = int(input())

def plus(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return plus(num-1) + plus(num-2) + plus(num-3)

for _ in range(N):
    print(plus(int(input())))