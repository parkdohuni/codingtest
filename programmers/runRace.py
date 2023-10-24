def solution(players, callings):
    player_rank = {player: int(idx) for idx, player in enumerate(players)}

    for call in callings:
        cur_rank = player_rank[call]

        player_rank[call] -= 1
        player_rank[players[cur_rank - 1]] += 1

        players[cur_rank - 1], players[cur_rank] = call, players[cur_rank - 1]

    return players


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
