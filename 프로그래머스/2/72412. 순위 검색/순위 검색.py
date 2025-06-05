from collections import defaultdict
from itertools import product
import bisect

def solution(info, query):
    
    def get_all_combinations(conditions):
        """
        무관('-')을 포함한 2^4(16)개의 조합을 만듭니다.
        """
        choices = []
        for condition in conditions:
            choices.append([condition, '-'])
        
        # 16개 조합 리턴
        return list(product(*choices))
    
    def parse_query(q):
        """
        쿼리를 조건과 코테점수로 나누어 리턴합니다.
        """
        parts = q.replace(' and ', ' ').split()
        conditions = tuple(parts[:4])
        target_score = int(parts[-1])
        
        return conditions, target_score
    
    def binary_search(scores, target):
        """
        이분 탐색
        scores 리스트에서 target 이상인 요소의 개수를 리턴합니다.
        """
        idx = bisect.bisect_left(scores, target)
        return len(scores) - idx
        
    
    """모든 쿼리 경우의 수를 key로 가지고, 점수 리스트를 value로 매핑하는 딕셔너리"""
    score_dict = defaultdict(list)
    
    """
    모든 지원자 데이터 전처리
    "-"(무관) 데이터를 포함한 모든 경우의 수를 key로 하는 딕셔너리 생성
    value엔 key조건에 해당하는 지원자의 점수 리스트 할당
    """
    for person in info:
        parts = person.split()
        conditions = parts[:4]
        score = int(parts[-1])
        
        # 생성되거나/존재하는 모든 key에 점수 추가
        for combination in get_all_combinations(conditions):
            score_dict[combination].append(score)
    
    """이분 탐색을 위한 점수 리스트 정렬"""
    for key in score_dict:
        score_dict[key].sort()
        
    """메인 로직"""
    result = []
    
    for q in query:
        
        # 쿼리 파싱
        conditions, target_score = parse_query(q)
        
        # 쿼리에 맞는 점수 리스트 가져오기
        scores = score_dict[conditions]
        
        # 이분 탐색으로 target_score 이상인 개수 구하기
        count = binary_search(scores, target_score)
        result.append(count)
        
    return result