import sys
sys.setrecursionlimit(10**9)  # 재귀호출 최대 깊이를 늘려준다

pre = []  # 전위순회 순서 입력받기
while True:
    try:
        n = int(sys.stdin.readline())
        pre.append(n)
    except:
        break

def postOrder(nodeList):  # 전위순회 결과를 입력받는다 생각지 말고, 그냥 노드 리스트를 입력받는다 생각하면 이해가 편함
    if len(nodeList) == 0:  # 빈 리스트라면 return
        return
    
    left, right = [], []
    root = nodeList[0]  # root노드 기준으로 작은값, 큰값으로 나눈다
    for i in range(1, len(nodeList)): # root노드 다음값부터 반복문 진행
        if nodeList[i] > root:  # root보다 큰 값이 나온다면, 해당 값과 그 이후값은 모두 오른쪽 서브트리에 위치함
            left = nodeList[1:i]
            right = nodeList[i:]
            break  # 두 그룹으로 나누었다면 반복 종료
    else:  # 만약 두 그룹으로 나누지 못했다면( root보다 큰 값이 없었다면 )
        left = nodeList[1:]  # 전부 left로 보내기
    
    postOrder(left) # 왼쪽 그룹으로 여행을 보내기 ( 갔다 오면서 알아서 왼쪽값 출력함 )
    postOrder(right) # 오른쪽 그룹으로 여행을 보내기 ( 갔다 오면서 알아서 오른쪽값 출력함)
    print(root) # 왼, 오 다 출력했으면 루트 노드 출력

postOrder(pre)