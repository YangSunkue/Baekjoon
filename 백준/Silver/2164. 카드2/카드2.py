from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
cards = deque(range(1, N + 1))

while len(cards) > 1:

    cards.popleft()
    card = cards.popleft()
    cards.append(card)

print(cards.pop())