from collections import defaultdict
import bisect
def solution(info, query):
    """
    순위 검색 - 딕셔너리 방법
    비트마스킹 없이 itertools.product 사용
    """

    # 1. 모든 가능한 조건 조합 생성하는 함수
    def get_all_combinations(conditions):
        """
        ['java', 'backend', 'junior', 'chicken'] 
        → [('java', 'backend', 'junior', 'chicken'),
           ('java', 'backend', 'junior', '-'),
           ('java', 'backend', '-', 'chicken'),
           ...]
        """
        from itertools import product

        # 각 조건에 대해 [원래값, '-'] 조합 생성
        choices = []
        for condition in conditions:
            choices.append([condition, '-'])

        # 모든 조합 생성 (2^4 = 16개)
        return list(product(*choices))

    # 2. 딕셔너리 초기화
    score_dict = defaultdict(list)

    # 3. 지원자 정보 전처리
    for person in info:
        parts = person.split()
        conditions = parts[:4]  # [언어, 직군, 경력, 소울푸드]
        score = int(parts[4])

        # 모든 가능한 조합에 점수 추가
        for combination in get_all_combinations(conditions):
            score_dict[combination].append(score)

    # 4. 모든 점수 리스트 정렬 (이분탐색용)
    for key in score_dict:
        score_dict[key].sort()

    # 5. 쿼리 파싱 함수
    def parse_query(q):
        """
        "java and backend and junior and pizza 150"
        → ('java', 'backend', 'junior', 'pizza', 150)
        """
        parts = q.replace(' and ', ' ').split()
        conditions = tuple(parts[:4])
        target_score = int(parts[4])
        return conditions, target_score

    # 6. 이분탐색으로 개수 구하기
    def count_scores_above(scores, target):
        """정렬된 리스트에서 target 이상인 개수 반환"""
        idx = bisect.bisect_left(scores, target)
        return len(scores) - idx

    # 7. 각 쿼리 처리
    results = []
    for q in query:
        conditions, target_score = parse_query(q)

        # 해당 조건의 점수 리스트 가져오기
        scores = score_dict[conditions]

        # target_score 이상인 개수 구하기
        count = count_scores_above(scores, target_score)
        results.append(count)

    return results