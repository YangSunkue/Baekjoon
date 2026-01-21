"""
실버 3
그리디
"""
from collections import defaultdict
import sys
input = sys.stdin.readline

string = input().strip()
words = defaultdict(int)
for c in string:
    words[c] += 1

cnt = 0
for c in words:
    if words[c] % 2 == 1:
        cnt += 1
    if cnt >= 2:
        print("I'm Sorry Hansoo")
        sys.exit()

sorted_words = sorted(words.items())  # 알파벳 사전순 정렬

result = ''
middle = ''
for c, cnt in sorted_words:
    if cnt % 2 == 1:
        middle = c
    result += c * (cnt // 2)

temp = result
result += middle
for i in range(len(temp) -1, -1, -1):
    result += temp[i]

print(result)