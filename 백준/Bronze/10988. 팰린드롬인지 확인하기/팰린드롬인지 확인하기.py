import sys
input = sys.stdin.readline

word = input().strip()

l = 0
r = len(word) - 1
result = 1
while l < r:
    if word[l] != word[r]:
        result = 0
        break
    l += 1
    r -= 1

print(result)