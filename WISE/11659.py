n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.insert(0,0)
acc = [0]*(n+1)
for i in range(1, n+1):
    acc[i] = acc[i-1]+nums[i]

for _ in range(m):
    i, j = map(int, input().split())
    print(acc[j]-acc[i-1])

