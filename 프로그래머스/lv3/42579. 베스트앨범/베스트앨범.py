def solution(genres, plays):
    answer = []
    music = {}
    # 장르당 두개씩
    for i, t in enumerate(plays):
        if genres[i] not in music:
            music[genres[i]] = []
        music[genres[i]].append([i, t])
    music_sort = sorted(music.items(), key=lambda x: sum(y[1] for y in x[1]), reverse=True)

    for genre, songs in music_sort:
        songs_sorted = sorted(songs, key=lambda x: x[1], reverse=True)[:2]
        for song in songs_sorted:
            answer.append(song[0])
    return answer