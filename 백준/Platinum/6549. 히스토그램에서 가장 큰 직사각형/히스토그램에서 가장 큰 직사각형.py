import sys
input = sys.stdin.readline

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    
    walls = data[1:]
    walls.append(0)

    max_size = 0
    stack = []
    for i in range(len(walls)):
        while stack and walls[stack[-1]] > walls[i]:
            height = walls[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_size = max(max_size, height * width)

        stack.append(i)

    print(max_size)