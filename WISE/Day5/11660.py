import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0]*(n+1)]
for _ in range(n):
    ar = list(map(int, input().split()))
    ar.insert(0,0)
    arr.append(ar)
acc = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        acc[i][j] = acc[i][j-1]+acc[i-1][j]-acc[i-1][j-1]+arr[i][j]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(acc[x2][y2]-acc[x2][y1-1]-acc[x1-1][y2]+acc[x1-1][y1-1])