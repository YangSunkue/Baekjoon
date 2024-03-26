import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    control = sys.stdin.readline().split()

    if control[0] == 'push':
        stack.append(int(control[1]))
    
    elif control[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    elif control[0] == 'size':
        print(len(stack))
    
    elif control[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif control[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

