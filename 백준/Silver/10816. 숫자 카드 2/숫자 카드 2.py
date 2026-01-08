"""
실버 4
해시
"""
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
commands = list(map(int, input().split()))

cards_dict = defaultdict(int)
for card in cards:
    cards_dict[card] += 1

result = []
for command in commands:
    result.append(cards_dict[command])

print(*result)