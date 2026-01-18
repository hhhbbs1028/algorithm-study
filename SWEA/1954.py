T = int(input())
for t in range(1, T+1):
    print("#%d"%t)
    n = int(input())
    # n=1일 때 주의하기
    
    p = [[0]*n for _ in range(n)]
    c = 1 # 기록할 값
    d = 0 # direction idx
    cr = 0
    cc = 0
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    # r, c 증가하는 방향 True 
    for _ in range(n*n):
        p[cr][cc] = c
        if not (0<=cr+dr[d]<n and 0<=cc+dc[d]<n and p[cr+dr[d]][cc+dc[d]]==0):
            d = (d+1)%4
        cr += dr[d]
        cc += dc[d]
        c+=1
    for i in range(n):
        for j in range(n):
            print(p[i][j], end=" ")
        print("")