# 수학, 조합론, 해시 테이블
import sys
input = sys.stdin.readline

# 테스트 케이스 개수만큼 반복
N = int(input())
for _ in range(N):

    n = int(input()) # 의상 개수
    clothes = {}

    # 의상 입력받기, 의상 이름은 필요가 없음
    for _ in range(n):
        _, category = input().split()
        clothes[category] = clothes.get(category, 0) + 1 # 의상 종류 증가시키기
    
    # 경우의 수 계산
    total = 1
    for _, value in clothes.items():
        total *= value + 1
    
    # 아무 옷도 입지 않은 경우를 제외하고 출력
    print(total - 1)