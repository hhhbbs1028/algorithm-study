import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += a[j]
        if sum==m:
            ans+=1
print(ans)