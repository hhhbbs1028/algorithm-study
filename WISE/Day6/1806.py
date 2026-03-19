import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
# 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이

ans = 100000
sum, nidx = 0, 0
for i in range(n):
    while sum < s and nidx < n:
        sum+=arr[nidx]
        nidx+=1
    if sum >= s and ans>nidx-i:
        ans = nidx-i
    sum-=arr[i]
if ans == 100000: ans=0
print(ans)
