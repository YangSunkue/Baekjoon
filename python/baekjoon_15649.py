def dfs(graph, selected, m):  # 숫자목록, 현재선택된숫자리스트, 모을 숫자의 개수
    if len(selected) == m: # 선택된 숫자가 m개면 출력
        print(*selected)  # ex) [1, 2, 3]  ->  1 2 3 이렇게 출력됨
        return # 출력을 했으면 상위 노드로 돌아가 다른 경우의 수 찾음
    
    for i in range(1, len(graph)):  # 1부터 n까지 탐색
        if not visited[i]: # 방문 안했었다면 값 추가, 이 숫자를 점유한다는 느낌
            visited[i] = True  # 숫자는 중복되면 안 되니까, 하위 노드에서 이 숫자를 쓰지 않도록 True로 해둔다(점유한다)
            selected.append(i)
            dfs(graph, selected, m)  # 다음 값 추가를 위해 재귀 호출
            selected.pop() # 하위 노드들을 전부 탐색했다면 백트래킹, 값을 빼고 visited를 False로 만들어 다음 경우의 수를 탐색하게 함
            visited[i] = False # 이 숫자 점유를 해제한다

n, m = map(int, input().split())

graph = [i for i in range(n + 1)] # 인덱스와 노드번호를 동기화 하기 위해 크기를 1 늘린다
visited = [False] * (n + 1) # 마찬가지로 동기화를 위해 크기를 1 늘린다

dfs(graph, [], m)