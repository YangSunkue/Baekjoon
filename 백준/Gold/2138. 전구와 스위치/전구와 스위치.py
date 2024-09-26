# 그리디
import sys
input = sys.stdin.readline

N = int(input())
origin = list(map(int, input().strip()))
target = list(map(int, input().strip()))

# 1번 인덱스 전구부터 하나씩 누를지 말지 결정하는 함수
def solve(A, B):

    press = 0

    for i in range(1, N):
        if A[i-1] == B[i-1]: # 이전 전구가 같다면 누르지 않는다
            continue

        else: # 이전 전구가 다르다면 누른다
            press += 1

            A[i-1] = 1 - A[i-1]
            A[i] = 1 - A[i]
            if i+1 < N: A[i+1] = 1 - A[i+1] # i+1번이 존재한다면 바꿔준다
    
    return press if A == B else int(1e9)

# 첫 번째 스위치를 누르지 않은 경우
string = origin[:]
result = solve(string, target)

# 첫 번재 스위치를 누른 경우
origin[0] = 1 - origin[0]
origin[1] = 1 - origin[1]
result = min(result, solve(origin, target) + 1) # 두 개를 비교해서 result 결정

# 정답 출력
print(result) if result != int(1e9) else print(-1)