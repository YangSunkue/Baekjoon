import sys
input = sys.stdin.readline

string = input().strip()
bomb = list(input().strip())
bln = len(bomb)

stack = []
for c in string:
    stack.append(c)
    if stack[-bln:] == bomb:
        del stack[-bln:]

print(''.join(stack)) if stack else print('FRULA')