import sys
sys.setrecursionlimit(10**9) # 재귀호출 최대값 늘리기

arr = []
while True:  # 전위 순회 순서 입력받기
    try:
        n = int(sys.stdin.readline())
        arr.append(n)
    except:
        break

def postorder(pre):
    # 배열이 비어있다면 return
    if len(pre) == 0:
        return
    
    left, right = [], [] # 왼/오로 나눌 배열
    root = pre[0] # 받은 배열의 루트 노드를 기준으로 설정

    for i in range(1, len(pre)): # 루트를 기준으로 작은값/큰값으로 나눈다
        if pre[i] > root: # 큰 값 이후의 값들은 모두 right로 보냄
            left = pre[1:i]
            right = pre[i:]
            break
    else: # break가 실행되지 않고 for문이 그냥 끝났다면
        left = pre[1:] # 전부 왼쪽으로 보낸다
    
    # 왼쪽, 오른쪽 순으로 재귀호출하며 후위순회 순서를 출력한다
    postorder(left)
    postorder(right)
    print(root)

postorder(arr)