# 우선 모든 경우의 수 수열을 만드는 코드를 짠다
# depth가 0일 땐 바로 재귀 돌린다
# depth가 0이 아니라면 "이전 숫자와 비교해 더 클 경우" 재귀 돌린다
# num은 str 형태로 전달되며, 비교할 때만 int로 변환해 비교한다
# 수열이 완성되면 str형태의 num을 중간에 공백을 추가해서 result 리스트에 담는다
# result 리스트의 완성된 수열들을 차례로 출력한다
import sys
input = sys.stdin.readline

# 1 ~ N 까지의 수 / M개를 고른다
N, M = map(int, input().split())
visited = [False] * (N + 1) # 수와 인덱스를 맞추기 위해 + 1 한다
result = []

# 조건 검사 함수
def compare(a, b):
    if a > b:
        return False
    return True

def backTracking(depth, num):
    
    # 수열이 완성되었다면 result에 넣기
    if depth == M:
        result.append(' '.join(num))
        return
    
    for i in range(1, N + 1):
        if not visited[i]:

            if depth == 0 or compare(int(num[-1]), i):
                visited[i] = True
                backTracking(depth + 1, num + str(i))
                visited[i] = False

backTracking(0, '')
for re in result:
    print(re)