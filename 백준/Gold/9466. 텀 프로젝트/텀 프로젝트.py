import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

for _ in range(int(input())):
    N = int(input())
    choices = [0] + list(map(int, input().split()))

    visited = [False] * (N + 1)
    finished = [False] * (N + 1)
    team = [False] * (N + 1)

    def dfs(node):

        visited[node] = True
        next_node = choices[node]

        if not visited[next_node]:
            dfs(next_node)
        elif not finished[next_node]:
            temp = next_node
            while node != temp:
                team[temp] = True
                temp = choices[temp]
            team[node] = True
        
        finished[node] = True
    
    for node in range(1, N + 1):
        if not visited[node]:
            dfs(node)
    
    print(N - team.count(True))