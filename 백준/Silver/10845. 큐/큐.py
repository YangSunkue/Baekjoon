from collections import deque
import sys
input = sys.stdin.readline

queue = deque([])
for _ in range(int(input())):
    command = input().strip()

    if command.startswith('push'):
        _, value = command.split(' ')
        queue.append(value)

    elif command == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)

    elif command == 'size':
        print(len(queue))
    
    elif command == 'empty':
        if queue: print(0)
        else: print(1)
    
    elif command == 'front':
        if queue: print(queue[0])
        else: print(-1)
    
    elif command == 'back':
        if queue: print(queue[-1])
        else: print(-1)