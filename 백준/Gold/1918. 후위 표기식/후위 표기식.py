import sys
input = sys.stdin.readline

string = input().strip()

priority = {'*': 2, '/': 2, '+': 1, '-': 1}
stack = []
result = ''
for c in string:

    if c.isupper():
        result += c
    
    elif c == '(':
        stack.append(c)

    elif c == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    
    else:
        while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[c]:
            result += stack.pop()
        stack.append(c)

while stack:
    result += stack.pop()

print(result)