import sys

n, m = map(int, sys.stdin.readline().split())  # 나무의 수 / 요구 벌목량
tree = list(map(int, sys.stdin.readline().split()))  # 나무 리스트
tree.sort(reverse=True)  # 내림차순 정렬 (큰 나무부터)

result = 0

# 이분 탐색으로 적절한 "높이"를 탐색한다
start = 1    # 최소 높이
end = max(tree)    # 최대 높이
while start <= end:   # start가 end보다 높아지면 탐색을 끝낸다
    mid = (start + end) // 2

    cutTree = 0
    for i in tree:    # 높이(mid)를 설정하고 일일이 벌목을 해본다
        if i > mid:    # 나무가 더 높으면 벌목해서 저장한다
            cutTree += i - mid
        else:    # 나무가 같거나 낮다면 어차피 진행해도 벌목 못하니까 break 한다
            break

    if cutTree >= m:    # 더 많이 벌목했다면 높이 증가
        start = mid + 1
    else:    # 적게 벌목했다면 높이 감소
        end = mid - 1
    
print(end)