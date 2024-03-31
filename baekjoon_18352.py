import sys

input = sys.stdin.readline
n = int(input())
numList = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxValue = -1e9
minValue = 1e9

def DFS(i, calc):
    global add, sub, mul, div, maxValue, minValue

    if i == n:  # 수열의 끝에 오면 최대/최솟값 구하기, 수열번호와 인덱스번호 헷갈리지 말자.
                # 수열번호가 1이면 인덱스번호는 0
        maxValue = max(maxValue, calc)
        minValue = min(minValue, calc)

    else:
        if add > 0:
            add -= 1
            DFS(i+1, calc + numList[i])  # 덧셈연산을 한 경우의 수 구하러 가기
            add += 1  # 구하고 왔으면 다른연산을 한 경우의 수도 구하러 가야 하니 다시 돌려놓기
        if sub > 0:
            sub -= 1
            DFS(i+1, calc - numList[i])
            sub += 1
        if mul > 0:
            mul -= 1
            DFS(i+1, calc * numList[i])
            mul += 1
        if div > 0:
            div -= 1
            DFS(i+1, int(calc / numList[i]))  # calc // numList[i] 를 하면, "내림" 해 버려서 음수일 경우 문제가 생긴다
            div += 1

DFS(1, numList[0])  # 수열의 첫번째 번호, 첫번째 숫자 인자로 넣고 DFS 실행
print(int(maxValue))
print(int(minValue))