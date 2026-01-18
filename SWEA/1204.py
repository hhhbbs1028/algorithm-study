T = int(input())
for t in range(1, T+1):
    n = int(input())
    score = list(map(int, input().split()))
    score_count = [0]*101

    for s in score:
        score_count[s] += 1

    max_index=0
    for b in range(101):
        if score_count[b]==max(score_count):
            if b>max_index:
                max_index=b

    print("#%d %d"%(t, max_index))