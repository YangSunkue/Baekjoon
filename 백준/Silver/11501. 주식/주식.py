import sys
input = sys.stdin.readline

"""
1. 가장 큰값부터 순서대로, 해당 값의 왼쪽에 있는 모든 값 다 사서 기준값에 팔기
2. 원본 테이블 우측부터 진행. (최대값 정렬리스트는 set사용)
3. 원본에서 삭제되는값들 + 기준값은 discard로 set에서 전부 순회하며 지우기
4. 삭제되고 남은 원본 기준으로 이어서 작업 실행

[1, 3, 1, 10, 2, 9, 3, 10, 5]
[10, 9, 5, 3, 2, 1]
"""

for _ in range(int(input())):

    N = int(input())
    values = list(map(int, input().split()))

    # 중복제거 후 최댓값 순 정렬하기
    sorted_values_set = set(values)
    sorted_values = sorted(list(sorted_values_set), reverse=True)  # 최댓값 리스트

    # 원본 리스트가 빌 때까지 진행
    result = 0
    cur_max_idx = -1
    while values:
        cur_max_idx += 1
        
        # 뒤쪽부터 탐색
        for i in range(len(values) - 1, -1, -1):
            
            # 최대값 만난 경우 좌측 것들 다 사서 최대값에 팔기
            cur_max = sorted_values[cur_max_idx]
            if values[i] == cur_max:
                sell_values = values[:i + 1]  # 팔고 나서 삭제할 값들
                values = values[i + 1:]  # 팔고 남은 값들 (이어서 계산할 애들)

                # 이득 계산 후 최댓값 리스트에서 지우기
                for v in sell_values:
                    result += (cur_max - v)
                break
    
    print(result)