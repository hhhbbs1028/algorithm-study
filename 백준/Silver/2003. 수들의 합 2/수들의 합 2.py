import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0 
for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += arr[j]
        if sum>=m:
            if sum==m:
                ans+=1
            break

print(ans)