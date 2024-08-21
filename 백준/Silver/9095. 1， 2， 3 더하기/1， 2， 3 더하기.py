import sys
input = sys.stdin.readline

N = int(input())

# num-1, num-2, num-3  경우의 수들에서 각각 1, 2, 3을 한번씩만 더해주면 num의 경우의 수가 된다.
# 즉 num-1, num-2, num-3 경우의 수를 모두 합치면 된다.
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