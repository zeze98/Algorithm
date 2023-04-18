def solution(players, callings):
    answer = []
    idx = {i: players for i, players in enumerate(players)}
    play = {players: i for i, players in enumerate(players)}
    for i in callings:
        now = play[i]
        front = now - 1
        front_player = idx[front]

        idx[now] = front_player
        idx[front] = i

        play[i] = front
        play[front_player] = now
    answer = list(idx.values())
    return answer