from collections import defaultdict

def solution(genres, plays):

    """
    장르별 총재생수 기준 정렬
    장르별 고유번호, 재생수 기준 정렬해서 담기
    """

    genres_dict = defaultdict(list)  # 장르: [(고유번호, 재생수), ...]
    plays_dict = defaultdict(int)    # 장르: 총 재생수

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        genres_dict[genre].append((i, play))
        plays_dict[genre] += play
    
    # 총재생수 기준 장르 정렬 [(장르, 재생수)]
    sorted_dict = sorted(plays_dict.items(), key=lambda x: -x[1])

    result = []
    for genre, _ in sorted_dict:
        sorted_songs = sorted(genres_dict[genre], key=lambda x: (-x[1], x[0]))
        result.extend([idx for idx, _ in sorted_songs[:2]])
    
    return result