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

# XOR 성질
# - 같은 수끼리 XOR -> 0
# - 0과 XOR 시 그대로
# - 교환/결합법칙 성립
# - prefix 누적 -> 앞부분 상쇄