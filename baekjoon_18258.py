import sys
from collections import deque

n = int(sys.stdin.readline())

home = deque()

for _ in range(n):
    control = sys.stdin.readline().split()
    c = control[0]

    if c == 'push':
        home.append(int(control[1]))
    
    elif c == 'pop':
        if len(home) == 0:
            print(-1)
        else:
            print(home.popleft())

    elif c == 'size':
        print(len(home))
    
    elif c == 'empty':
        if len(home) == 0:
            print(1)
        else:
            print(0)
    
    elif c == 'front':
        if len(home) == 0:
            print(-1)
        else:
            print(home[0])
    elif c == 'back':
        if len(home) == 0:
            print(-1)
        else:
            print(home[-1])