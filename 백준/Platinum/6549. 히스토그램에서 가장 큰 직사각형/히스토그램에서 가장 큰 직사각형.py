import sys
input = sys.stdin.readline

while True:
    data = list(map(int, input().split()))
    n = data[0]
    nodes = data[1:]

    if n == 0:
        break

    stack = []
    max_size = 0
    nodes.append(0)

    for i, h in enumerate(nodes):
        while stack and nodes[stack[-1]] > h:
            height = nodes[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_size = max(max_size, height * width)

        stack.append(i)
    
    print(max_size)