"""
다이아 5
그리디
"""
import sys
input = sys.stdin.readline

N = int(input())
fac = list(map(int, input().split()))

def buy_one(pos) -> int:
    count = fac[pos]
    fac[pos] -= count
    return count * 3

def buy_two(pos) -> int:
    count = min(fac[pos], fac[pos + 1])
    fac[pos] -= count
    fac[pos + 1] -= count
    return count * 5

def buy_three(pos) -> int:
    count = min(fac[pos], fac[pos + 1], fac[pos + 2])
    fac[pos] -= count
    fac[pos + 1] -= count
    fac[pos + 2] -= count
    return count * 7

price = 0
for pos in range(N):

    if pos == N - 1 or fac[pos + 1] == 0:
        price += buy_one(pos)
        continue

    if pos == N - 2:
        price += buy_two(pos)
        price += buy_one(pos)
        continue

    if fac[pos + 1] > fac[pos + 2]:
        count = min(fac[pos], fac[pos + 1] - fac[pos + 2])

        fac[pos] -= count
        fac[pos + 1] -= count

        price += 5 * count
        price += buy_three(pos)
    else:
        price += buy_three(pos)
        price += buy_two(pos)
    
    price += buy_one(pos)


print(price)