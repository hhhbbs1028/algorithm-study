import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))

a_sum = [0]*(n+1)
for i in range(1, n+1):
    a_sum[i] = a_sum[i-1]+a[i-1]

count = 0
for i in range(n):
    for j in range(n-1, -1, -1):
        if a_sum[j+1]-a_sum[i]==m:
            count+=1

print(count)