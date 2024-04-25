import sys
input = sys.stdin.readline

N = int(input()) # 정사각형 변의 길이
house = []  # 지도 입력받기
for _ in range(N):
    house.append(list(input().rstrip()))

