T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_die = 0
    die = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            max_die = max(max_die, die)
            die = 0
            for k in range(M):
                for h in range(M):
                    die += flies[i+k][j+h]

    print("#%d %d"%(t, max_die))

    # 5<=N<=15
    # 2<=M<=N
    # 각 영역 파리 개수 30 이하