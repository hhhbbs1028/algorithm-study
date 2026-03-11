import sys
input = sys.stdin.readline
n, m = map(int, input().split())
h = list(map(int, input().split()))
diff = [0]*(n+1) 

for _ in range(m):
    a, b, k = map(int, input().split())
    diff[a-1]+=k
    diff[b]-=k

for i in range(1, n):
    diff[i] += diff[i-1]

for i in range(n):
    h[i] += diff[i]
print(" ".join(str(i) for i in h))