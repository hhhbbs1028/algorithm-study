from collections import Counter
def solution(genres, plays):
    all = {}
    n = len(genres)
    for i in range(n):
        genre = genres[i]
        play = plays[i]
        
        if genre not in all:
            all[genre] = {}
            all[genre]['sum'] = 0
            all[genre]['songs'] = []
        
        all[genre]['songs'].append((i, play))
        all[genre]['sum']+=play
    
    answer = []
    for genre in list(sorted(all, key=lambda x:all[x]['sum'], reverse=True)):
        for (i, play) in list(sorted(all[genre]['songs'], key=lambda x:x[1], reverse=True))[:2]:
            answer.append(i)
    return answer