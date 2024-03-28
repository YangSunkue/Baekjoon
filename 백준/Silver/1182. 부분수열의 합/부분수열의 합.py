n, s = map(int, input().split())  # 숫자 개수, 목표숫자
numList = list(map(int, input().split()))  # 숫자 리스트
cnt = 0  # 결과 저장 변수
number = []  # 계산용 리스트

def back(start):  # 시작 인덱스 입력받기
    global cnt
    if sum(number) == s and len(number) > 0:  # 숫자 합이 일치하고 원소가 1개 이상일 때 ( 공집합 제외 )
        cnt += 1
    
    for i in range(start, len(numList)):  # 입력받은 인덱스부터 숫자리스트 끝까지
        number.append(numList[i])  # 현재 숫자 더하기
        back(i + 1)  # 현재 숫자가 포함된 경우의 수 모두 구하러 가기 (재귀호출되어 numList 끝 숫자까지 간다)
        number.pop()  # 갔다 왔으니 다음 숫자 포함해서 경우의 수 구하러 가기

back(0)  # 0번 인덱스부터 시작
print(cnt)  # 계산된 cnt 출력