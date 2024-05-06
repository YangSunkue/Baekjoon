import sys
input = sys.stdin.readline

# 과제 개수
N = int(input())
# 소요일, 마감일
DT = []
for i in range(N):
    DT.append(list(map(int, input().split())))

# 마감일 기준 내림차순 정렬
DT = sorted(DT, key=lambda x: x[1], reverse=True)

# 쉴 수 있는 시간 계산할 변수
day = DT[0][1]

# day와 마감일 중 작은 시간에서 소요일을 뺀다.
# 둘 중 더 큰 값은 의미가 없어진다.
# day가 길어도 마감일이 짧으면 마감일에 맞춰야 한다
# 과제의 마감일이 길어도 정작 남은 day가 짧으면 day에 맞춰야 한다. ( 특정 과제가 오랜 기간이 걸릴 경우 이럴 수 있다 )
for i in range(N):

    # 소요일, 마감일 
    s = DT[i][0]
    e = DT[i][1]

    # min(쉴 수 있는 시간, 마감일) 에서 소요일을 뺀다
    day = min(day, e) - s

print(day)