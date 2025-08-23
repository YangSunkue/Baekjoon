import sys
input = sys.stdin.readline

"""
a의 총 개수 범위에서 b의 개수 -> 교환횟수

원형 인덱스 구하기: 인덱스 % length
각 인덱스를 시작점으로 length번 계산하면 됨
"""

data = input().strip()
a_count = data.count('a')
if a_count == len(data):
    print(0)
    sys.exit()

# 초기 b 개수 세기
b_count = 0
for i in range(a_count):
    if data[i] == 'b':
        b_count += 1
result = b_count  # 결과 저장할 변수

# 슬라이딩 윈도우로 범위별 b개수 세기
left = 1
right = a_count
for _ in range(len(data)):
    if data[left - 1] == 'b':
        b_count -= 1
    if data[right] == 'b':
        b_count += 1
    
    result = min(result, b_count)

    left += 1
    right = (right + 1) % len(data)

print(result)