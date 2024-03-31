import sys

input = sys.stdin.readline
n = int(input())  # 수의 개수
numList = list(map(int, input().split()))  # 수열
add, sub, mul, div = map(int, input().split())  # +, -, *, //

maxValue = -1e9  # 완전히 작은 값으로 초기화해두면 이후 어떤 값이 들어와도 그 값이 최댓값이 되기 때문이다.
minValue = 1e9  # 완전히 큰 값으로 초기화해두면 이후 어떤 값이 들어와도 그 값이 최솟값이 되기 때문이다. 이 두개 다 관례적으로 이렇게 설정하는것임.

def dfs(i, calc):  # 현재 수열 번호, 임시 계산용 변수
    global add, sub, mul, div, maxValue, minValue

    if i == n: # 수열 끝에 왔을 경우 최대/최소값 계산
                # 수열 번호와 수열이 저장된 리스트의 인덱스 번호를 헷갈리지 말아햐 한다. 1번 값은 numList[0]에 저장되어 있다.
        maxValue = max(maxValue, calc)
        minValue = min(minValue, calc)

    else: # 현재 calc값에서 덧셈, 뺄셈, 곱셈, 나눗셈을 한 모든 경우의 수를 조사한다.
        if add > 0:
            add -= 1
            dfs(i + 1, calc + numList[i]) 
            add += 1  # 다음 경우의수도 조사하러 갈 수 있게 add를 돌려놓는다
        if sub > 0:
            sub -= 1
            dfs(i + 1, calc - numList[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, calc * numList[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(calc / numList[i]))  # calc // numList[i]를 하면, 음수일 경우 "내림"이 되기 때문에 값에 오류가 생긴다.
            div += 1

dfs(1, numList[0])
print(int(maxValue))
print(int(minValue))