n = int(input())

pos = [0] * n  # 퀸 위치 담을 리스트
flag_heng = [False] * n  # 행 배제
flag_a = [False] * ((n-1) * 2 + 1)  # 우상향 대각 배제
flag_b = [False] * ((n-1) * 2 + 1)  # 좌상향 대각 배제
count = 0  # 경우의 수 

def set(i):
    global count

    for j in range(n):
        if not flag_heng[j] and not flag_a[i + j] and not flag_b[(n-1) + i - j]: # 행 , 대각, 대각 안전할 때
            pos[i] = j  # i번째 열의 j번째 행에 퀸을 둔다
            if i == n - 1:  # 마지막 열에 퀸을 뒀을 때, 즉 경우의 수 하나를 찾았을 때
                count += 1
            else:  # 마지막 열이 아닐 때
                flag_heng[j] = flag_a[i + j] = flag_b[(n-1) + i - j] = True  # 퀸 공격범위 배제
                set(i + 1)  #  다음 열에 퀸 두러 가기( 7열까지 다 둔 후 돌아오게 된다 )
                # 7열까지 갔다 왔으므로, 다시 1열부터 경우의 수를 찾기 위해 공격범위 배제했던걸 돌려놓는다
                flag_heng[j] = flag_a[i + j] = flag_b[(n-1) + i - j] = False
                # 이후 for문이 반복된다

set(0)
print(count)