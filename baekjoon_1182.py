n, s = map(int, input().split())  # 숫자의 개수, 목표 숫자
numList = list(map(int, input().split()))  # 숫자 리스트
number = []  # 계산에 사용할 리스트
cnt = 0  # 경우의 수 저장할 변수


def back(start):  # 시작 인덱스 입력받기
    global cnt
    if sum(number) == s and len(number) > 0:  # 합이 s와 같고, 원소가 1개 이상일 때 ( 공집합 제외 해야 하니까 )
        cnt += 1  # 찾았으니 경우의 수 + 1

    for i in range(start, len(numList)):  # 입력받은 인덱스부터, numList의 끝까지 진행한다
        number.append(numList[i])  # 현재 인덱스에 해당하는 숫자를 계산 리스트에 추가
        print(number)
        back(i+1)  # 다음 인덱스도 계산하러 가기, 재귀 호출. # 리스트 인덱스로 바로 접근하는 게 아니라 인자로써 주기 때문에 인덱스 에러 안뜬다
                    # 그냥 다음 반복문이 실행되지 않을 뿐이다
        number.pop()  # i가 포함된 경우의 수 다 구했으니, i + 1이 포함된 경우의 수 구하러 가기


back(0)
print(cnt)