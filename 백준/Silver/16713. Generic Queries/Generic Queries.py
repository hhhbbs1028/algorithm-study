import sys
input = sys.stdin.readline
n, q = map(int, input().split())
a = list(map(int, input().split()))

prefix = [0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i]^a[i]

ans = 0
for _ in range(q):
    s, e = map(int, input().split())
    ans ^= prefix[e] ^ prefix[s-1]
print(ans)