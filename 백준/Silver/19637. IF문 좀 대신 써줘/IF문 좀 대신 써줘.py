import sys
input = sys.stdin.readline

"""
캐릭터 전투력에 맞는 칭호 순서대로 출력

N: 칭호의 개수 1 ~ 100,000
M: 캐릭터 개수 N ~ 100,000


전투력, 칭호가 저장된 리스트를 만들고, 그 리스트 "인덱스" 이분탐색
[['weak', 10000], ['normal', 100000], ['strong', 1000000] .... ]

0 ~ 9까지 10개 칭호 가정
4(mid) 부터 검증, 해당 상한선보다 전투력 낮으면 end 감소. 
end 감소했을경우 result에 칭호명 넣기. 마지막에 출력.

"""

"""이분탐색으로 적절한 칭호를 찾는 함수"""
def find_title_by_power(arr, power):

    start = 0
    end = len(arr) - 1
    result = arr[start][0]

    while start <= end:

        mid = (start + end) // 2

        if arr[mid][1] >= power:
            result = arr[mid][0]
            end = mid - 1
        
        else:
            start = mid + 1
    
    # 칭호 리턴
    return result

N, M = map(int, input().split())

"""
칭호, 전투력 상한선 입력받기
[['weak', 10000], ['normal', 100000], ['strong', 1000000] .... ]
"""
title_and_power = []
for _ in range(N):

    title, power = input().strip().split()
    title_and_power.append([title, int(power)])

"""전투력 별 칭호 찾아 출력"""
for _ in range(M):

    cur_power = int(input())
    print(find_title_by_power(title_and_power, cur_power))