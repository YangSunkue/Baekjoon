import sys
input = sys.stdin.readline

N = int(input()) # 부등호 개수
boo = list(input().split()) # 부등호 리스트

result = []

visited = [False] * 10 # depth는 숫자 개수만큼

def compare(a, b, op):
    if op == '>':
        if a < b: return False
    elif op == '<':
        if a > b: return False
    return True

# 깊이, 현재숫자(문자열)
def backTracking(depth, num):

    # 숫자가 완성되었다면 결과 리스트에 추가
    if depth == N + 1:
        result.append(num)
        return
    
    for i in range(10):
        if not visited[i]:
            if depth == 0 or compare(num[-1], str(i), boo[depth-1]):
                visited[i] = True
                backTracking(depth + 1, num + str(i))
                visited[i] = False

backTracking(0, '')
print(max(result))
print(min(result))