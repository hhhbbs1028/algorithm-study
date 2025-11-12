p = int(input())

for tc in range(p):
    h = list(map(int, input().split()))[1:]

    cnt = 0
    cur = []
    for i in range(20):
        for j in range(i):
            if h[i] < cur[j]:
                cnt += len(cur)-j
                cur.insert(j, h[i])
    