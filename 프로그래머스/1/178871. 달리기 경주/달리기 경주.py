def solution(players, callings):
    
    players_dict = dict()  # {'mumu': 0, 'soe': 1, ...}
    for i, player in enumerate(players):
        players_dict[player] = i
    
    for winner in callings:
        winner_rank = players_dict[winner]
        loser_rank = winner_rank - 1
        loser = players[loser_rank]
        
        players_dict[winner] -= 1
        players_dict[loser] += 1
        players[winner_rank] = loser
        players[loser_rank] = winner
    
    return players