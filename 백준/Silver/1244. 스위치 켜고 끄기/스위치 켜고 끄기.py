import sys
import math
input = sys.stdin.readline

"""
학생 한명 당 하나씩 스위치 번호를 준다

남학생
-> 자기가 받은 수의 배수 스위치를 켜거나 끈다
여학생
-> 자기가 받은 스위치 중심으로, 양옆이 같은 상태일 경우 바꾼다. 바꿨을 경우 범위를 늘려 그 다음도 검사하고 바꾼다.

학생들은 입력되는 순서대로 스위치의 상태를 차례로 바꾼다.
스위치의 마지막 상태를 출력

N: 스위치 개수
M: 학생 수
"""
def male(num, switches):
    
    idx = num
    while idx - 1 < len(switches):

        switches[idx - 1] = 1 - switches[idx - 1]
        idx += num

def female(num, switches):

    switches[num - 1] = 1 - switches[num - 1]
    
    left = num - 2
    right = num
    while left >= 0 and right < len(switches):
        
        if switches[left] == switches[right]:
            switches[left] = 1 - switches[left]
            switches[right] = 1 - switches[right]

        else:
            return
        
        left -= 1
        right += 1

N = int(input())
switches = list(map(int, input().split()))

"""학생 수 만큼 반복하여 스위치 상태를 바꾼다"""
for i in range(int(input())):

    # 성별, 번호
    sex, num = map(int, input().split())
    if sex == 1:
        male(num, switches)
    else:
        female(num, switches)

for i in range(math.ceil(len(switches) / 20)):
    text = switches[i*20 : i*20 + 20]
    print(' '.join(map(str, text)))
