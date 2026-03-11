testcase = int(input())
for tc in range(testcase):
    h = list(map(int, input().split()))[1:]
    cnt = 0
    cur = []
    for i in range(20):
        j = 0 
        for _ in range(i):
            if h[i] < cur[j]:
                break
            j+=1
        cnt += i-j
        cur.insert(j, h[i])
        
    print(tc+1, cnt)
