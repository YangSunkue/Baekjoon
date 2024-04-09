# 끝나는시간으로 정렬하지 않으면 일찍 시작하고 아주 늦게 끝나는 회의에 말릴 수 있다
# 시작시간으로 정렬해야 회의목록을 순차적으로 돌면서 진행 가능하다
import sys
input = sys.stdin.readline

N = int(input())  # 회의 개수
talkList = []  # 회의 리스트 (시작시간, 종료시간)
for _ in range(N):
    talkList.append(list(map(int, input().split())))

talkList.sort(key = lambda x: (x[1], x[0]))  # 회의 리스트 정렬 ( 끝나는시간으로 정렬 후 시작시간으로 정렬 )

cnt = 1  # 회의개수 셀 변수
end = talkList[0][1]  # 첫 회의 끝나는시간을 미리 초기화해둔다
for i in range(1, N):  # 회의 갯수 세기 시작
    if end <= talkList[i][0]:  # 회의 시작시간이 이전회의 끝나는시간과 같거나 크면 회의 + 1
        cnt += 1
        end = talkList[i][1]  # 회의시간 갱신

print(cnt)