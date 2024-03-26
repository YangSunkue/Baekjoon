n = int(input())

def hanoi(no, start, end, mid):
    if no == 1:
        print(start, end) 
        return
    
    else:
        hanoi(no-1, start, mid, end)
        print(start, end)
        hanoi(no-1, mid, end, start)



if n <= 20:
    print(2 ** n - 1) # 최소횟수 출력
    hanoi(n, 1, 3, 2) # 경로 출력

else:
    print(2 ** n - 1) # 경로 출력 안해도 되니 최소횟수만 출력