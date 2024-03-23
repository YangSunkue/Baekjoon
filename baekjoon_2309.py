hobit = [] # 난쟁이 리스트

for _ in range(9): # 9명 입력받음
    hobit.append(int(input()))

kee = sum(hobit) # 9명 난쟁이 키의 합을 구해둔다
def hobit7(hobit):
    for i in range(len(hobit)-1): # 가능한 모든 경우의 수 인덱스를 구해서 반복한다
        for j in range(len(hobit)):
            if j > i:
                if kee - (hobit[i] + hobit[j]) == 100:  # 난쟁이 2명을 뺀 키가 100 이라면 정답
                    a = hobit[i]
                    b = hobit[j]
                    hobit.remove(a) # 난쟁이 삭제
                    hobit.remove(b)
                    hobit.sort() # 정렬
                    for i in hobit: # 결과 출력
                        print(i)

                    return # 답을 찾으면 출력 후 함수 종료
                    
hobit7(hobit)