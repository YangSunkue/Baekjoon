import sys
input = sys.stdin.readline

# 웅덩이 개수, 널빤지 길이
N, L = map(int, input().split())
w = []
for _ in range(N):
    w.append(list(map(int, input().split())))
water = sorted(w, key=lambda x: (x[0])) # 웅덩이 시작지점 기준으로 정렬

def fix(size):
    if size % L >= 1:
        return (size // L) + 1
    else:
        return size // L

def solve():

    result = 0 # 널빤지 개수 세는 변수
    finalFix = -1 # 마지막으로 덮인(가장 뒤) 널빤지 인덱스

    if N == 1:
        size = water[0][1] - water[0][0]
        return fix(size)
    
    for i in range(N):
        size = water[i][1] - water[i][0]

        if size < 0: # 웅덩이 크기가 음수일 경우 ( 미뤄졌다면 음수일 가능성이 있다 )

            # 여기서도 겹친부분 체크 꼭 해줘야함.
            # 아래쪽 체크부분은 바로 다음 웅덩이만 미뤄주기 때문.
            try:
                if finalFix >= water[i+1][0]:
                    water[i+1][0] = finalFix + 1
            except: # 맨 마지막 웅덩이라면 continue
                continue
            continue

        fixResult = fix(size)
        result += fixResult
        finalFix = water[i][0] + (L * fixResult) - 1

        try:
            if finalFix >= water[i+1][0]: # 덮은 부분이 다음 시작지점과 겹친다면 시작지점 미루기
                water[i+1][0] = finalFix + 1
        except: # 맨 마지막 웅덩이라면 continue
            continue
    
    return result

print(solve())