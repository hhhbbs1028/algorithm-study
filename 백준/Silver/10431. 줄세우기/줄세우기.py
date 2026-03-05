p = int(input()) #1 ≤ P ≤ 1000

for tc in range(p):
    h = list(map(int, input().split()))[1:]
    score = 0
    for i in range(20):
        for j in range(i, 20):
            if h[i]>h[j]:
                score+=1
    print(tc+1, score)