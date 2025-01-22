# 실버1 -> 구현, 자료구조, 문자열, 해시
# 들어간 순서 해시 테이블로 저장해두기
# 나온 차량 순서 기준으로, 이후 나올 차량의 "들어올 때 인덱스"를 찾아서
# 나온 차량의 들어올 때 인덱스가 한 번이라도 더 클 경우 result += 1

N = int(input())
go_in = dict()
come_out = []

for i in range(N):
    go_in[input()] = i
for i in range(N):
    come_out.append(input())

result = 0
for i in range(len(go_in) - 1):
    # 현재 나온 차량의, 들어올 때 순서
    out_car = go_in[come_out[i]]

    # 이후 나올 차량의, 들어올 때 순서와 비교하여 추월일 경우 추가
    for j in range(i+1, len(go_in)):
        if out_car > go_in[come_out[j]]:
            result += 1
            break

print(result)