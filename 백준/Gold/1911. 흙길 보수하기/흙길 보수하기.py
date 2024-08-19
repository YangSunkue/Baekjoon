import sys
input = sys.stdin.readline

# N개의 웅덩이, L길이의 널빤지
N, L = map(int, input().split())
water = []

# 겹치는 웅덩이는 들어오지 않는다
# 웅덩이 좌표 : [1, 6] -> 1 2 3 4 5
for _ in range(N):
    water.append(list(map(int, input().split())))
sortedWater = sorted(water, key=lambda x: (x[0])) # 시작 위치 기준으로 정렬

def fix(size, L):
    if size % L >= 1:
        return size // L + 1
    else:
        return size // L

def solve():

    result = 0
    finalFix = -1

    # 웅덩이가 1개뿐일 경우
    if N == 1:
        size = sortedWater[0][1] - sortedWater[0][0]
        return fix(size, L)

    # 웅덩이가 여러개일 경우
    for i in range(N):
        size = sortedWater[i][1] - sortedWater[i][0] # 웅덩이 크기
        
        if size < 0: # 웅덩이 크기가 음수일 경우
            try:
                if finalFix >= sortedWater[i+1][0]: # 덮인 부분이 다음 웅덩이에 겹쳤다면 다음 웅덩이 시작 지점 미루기
                    sortedWater[i+1][0] = finalFix + 1
            except:
                # 마지막 웅덩이일 경우
                continue
            continue
        fixResult = fix(size, L)
        result += fixResult
        finalFix = sortedWater[i][0] + (L * fixResult) - 1 # 마지막으로 널빤지 덮인 위치(인덱스)

        try:
            if finalFix >= sortedWater[i+1][0]: # 덮인 부분이 다음 웅덩이에 겹쳤다면 다음 웅덩이 시작 지점 미루기
                sortedWater[i+1][0] = finalFix + 1
        except:
            # 마지막 웅덩이일 경우
            continue
    
    return result

print(solve())