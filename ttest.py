def dfs(graph, selected, m):
    if len(selected) == m:
        print(*selected)
        return
    
    for i in range(1, len(graph)):
        if visited[i] == False:
            visited[i] = True # i라는 숫자 점유하기, 중복 숫자가 있으면 안 되니 하위 노드에서 못 쓰도록
            selected.append(i)
            dfs(graph, selected, m)
            selected.pop() # 경우의 수 다 조사하고 왔으니 이전 노드로 돌아가기
            visited[i] = False # 점유 해제, 다음 경우의 수로 넘어가기
    
n, m = map(int, input().split())
graph = [i for i in range(n + 1)]
visited = [False] * (n + 1)

dfs(graph, [], m)