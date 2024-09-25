# 문자열, 슬라이딩 윈도우
from collections import deque
import sys
input = sys.stdin.readline

S, P = map(int, input().split()) # DNA 길이, 비번 길이
DNA = input().rstrip()
ACGT = list(map(int, input().split()))

def slidingWindow():

    # 결과 담을 변수
    result = 0

    # 큐에 초기값 집어넣기
    queue = deque()
    for i in range(P):
        queue.append(DNA[i])
    
    # ACGT 개수 미리 세놓기
    A = queue.count('A')
    C = queue.count('C')
    G = queue.count('G')
    T = queue.count('T')

    idx = P # 다음 문자 가져올 인덱스

    # 빠져나가는 것과 들어오는 알파벳의 개수만 변화시킨다
    while queue:

        if A >= ACGT[0] and C >= ACGT[1] and G >= ACGT[2] and T >= ACGT[3]:
            result += 1
        
        # 앞 문자열을 뺀다
        string = queue.popleft()
        if string == 'A': A -= 1
        elif string == 'C': C -= 1
        elif string == 'G': G -= 1
        elif string == 'T': T -= 1

        # 뒤에 문자열을 더한다
        if idx >= len(DNA): # 남은 DNA문자가 없으면 break
            break

        string2 = DNA[idx]
        queue.append(string2)

        if string2 == 'A': A += 1
        elif string2 == 'C': C += 1
        elif string2 == 'G': G += 1
        elif string2 == 'T': T += 1

        idx += 1 # 다음 문자열을 가리키도록 인덱스 증가

    return result


print(slidingWindow())