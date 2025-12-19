import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

for _ in range(int(input())):
    N = int(input())
    choice = [0] + list(map(int, input().split()))

    visited = [False] * (N + 1)
    finished = [False] * (N + 1)
    team = [False] * (N + 1)

    def dfs(cur):

        visited[cur] = True
        next_node = choice[cur]

        if not visited[next_node]:
            dfs(next_node)
        elif not finished[next_node]:
            temp = next_node
            while temp != cur:
                team[temp] = True
                temp = choice[temp]
            team[cur] = True

        finished[cur] = True
    
    for node in range(1, N + 1):
        if not visited[node]:
            dfs(node)
    
    print(N - team.count(True))