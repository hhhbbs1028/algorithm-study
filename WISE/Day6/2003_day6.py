import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

nidx, sum, ans = 0, 0, 0
for x in arr:
    while sum < m and nidx < n:
        sum += arr[nidx]
        nidx += 1
    if sum == m:
        ans += 1
    sum -= x
print(ans)