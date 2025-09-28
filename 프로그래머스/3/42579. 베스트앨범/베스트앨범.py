from collections import defaultdict

def solution(genres, plays):

    genres_dict = defaultdict(lambda: [0, []])  # {장르: [재생횟수, [노래1, 노래2...]]}
    for i in range(len(genres)):
        key = genres[i]
        genres_dict[key][0] += plays[i]
        genres_dict[key][1].append(i)

    plays_dict = defaultdict(int)
    for i, p in enumerate(plays):
        plays_dict[i] = p

    # 재생횟수 내림차순 정렬
    genres_dict = dict(sorted(genres_dict.items(), key=lambda x: -x[1][0]))
    plays_dict = dict(sorted(plays_dict.items(), key=lambda x: (-x[1], x[0])))
    
    result = []
    for key in genres_dict:
        
        data = genres_dict[key][1]  # [1, 2, 3 ..]
        if len(data) == 1:
            result.append(data[0])
        else:
            first = None
            second = None
            for p in plays_dict:  # {1: 200, 2 :100 ...}
                if p in data:
                    if first == None:
                        first = p
                    else:
                        second = p
                        break
            
            result.append(first)
            result.append(second)
    
    return result