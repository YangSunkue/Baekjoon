n = int(input())

def hanoi(no, start, end, mid): # no번 원반을 start에서 end로 옮긴다
    if no == 1: # 원반이 1개라면 위에 방해되는 원반이 없으니 즉시 옮긴다
        print(start, end)
        return
    
    else:
        hanoi(no-1, start, mid, end) # 2개 이상이면 위에 방해되는 원반을 치운다 
        print(start, end) # 방해되는거 치웠으니 원래 옮기려던거 목표자리에 옮긴다
        hanoi(no-1, mid, end, start) # 치워둔것도 목표자리에 옮긴다



if n <= 20:
    print(2 ** n - 1) # 최소횟수 출력
    hanoi(n, 1, 3, 2) # 경로 출력

else:
    print(2 ** n - 1) # 경로 출력 안해도 되니 최소횟수만 출력