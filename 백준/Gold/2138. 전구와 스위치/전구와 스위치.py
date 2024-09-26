# 그리디
# 전구의 상태는 꺼짐/켜짐 두 개뿐이다. 즉 2번 누르면 원래대로 돌아간다.
# 따라서 각 스위치를 0번 또는 1번 누르는 두 가지 경우의 수가 전부이다.
# 목표로 하는 전구상태를 만들어 가면서 스위치를 하나씩 누르거나/누르지 않으면 한 번의 순회로 정답을 도출할 수 있다.
# 앞->뒤 방향으로 진행할 경우, i-1번 스위치는 i번 스위치에 최종적으로 영향을 받는다
# 즉 i번 스위치를 눌러 i-1번 전구를 목표 상태로 맞춰 놓았다면, 이후에는 고려할 필요가 없다. 즉, 고정된다.
# 단, 첫번째 스위치는 비교할 i-1번 전구가 없으므로 누르거나/누르지않거나 2가지 경우의 수를 고려한다.
# 이렇게 하면 모든 경우의 수를 고려할 수 있다.
# 전구를 앞에서부터 1개씩 목표와 똑같이 맞춰간다고 생각하면 된다.
# 부분에서의 최적의 해 : i-1번 전구 1개 맞추기
# 전구를 1개씩 맞춰가면 최종적으로 정답에 도달 -> 그리디
import sys

N = int(input())
origin = list(input().strip())
target = list(input().strip())

def solve(A, B):

    press = 0

    for i in range(1, N):
        if A[i-1] == B[i-1]: # 이전 전구 상태가 같을 경우 다음으로 넘어간다
            continue

        else: # 이전 전구 상태가 다를 경우 스위치 누른다
            press += 1

            for j in range(i-1, i+2):
                if j < N:
                    if A[j] == '0': A[j] = '1'
                    else: A[j] = '0'
    
    # 목표 달성했으면 누른 횟수 리턴, 못했다면 INF 리턴
    return press if A == B else int(1e9)

# 첫번째 스위치를 누르지 않은 경우
string = origin[:]
result = solve(string, target)

# 첫번째 스위치를 누른 경우와 비교해서 result 결정
string = origin[:]
for i in range(2):
    if string[i] == '0': string[i] = '1'
    else: string[i] = '0'
result = min(result, solve(string, target) + 1) # 첫번째 누르고 시작했으니 + 1 해준다

print(result) if result != int(1e9) else print(-1)