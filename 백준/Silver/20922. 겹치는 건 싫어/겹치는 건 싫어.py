from collections import defaultdict
import sys
input = sys.stdin.readline

"""
최장 연속 부분 수열 길이 구하기
같은 정수는 K개 까지 허용

N: 제공된 수열 길이
K: 같은 정수 허용 상한
numbers: 제공된 수열
num_count: 각 숫자 당 개수 세는 딕셔너리, 기본값 list

슬라이딩 윈도우

-> 숫자: 개수
-> 숫자가 K개가 넘었다면,
    left는 해당숫자 가장빠른위치 + 1 까지 진행하며 값 빼기 한 후
    right는 right + 1
    부분부터 다시 진행한다
"""

N, K = map(int, input().split())
nums = list(map(int, input().split()))
num_count = defaultdict(int)

left = 0
right = 0
result = 0
count = 0
while left <= right and right < N:
    
    num_count[nums[right]] += 1
    if num_count[nums[right]] > K:  # 중복 횟수 초과 시

        # left를 하나씩 올리면서 숫자당 개수 줄이기
        for i in range(left, N - 1):
            num_count[nums[i]] -= 1
            left += 1

            if nums[i] == nums[right]:
                break
        
        count = (right - left) + 1
    else:
        count += 1
        result = max(result, count)

    right += 1

print(result)