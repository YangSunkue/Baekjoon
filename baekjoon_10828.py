import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    control = sys.stdin.readline().split()
    c = control[0]

    if c == 'push':
        stack.append(int(control[1]))
    
    elif c == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    elif c == 'size':
        print(len(stack))
    
    elif c == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif c == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])