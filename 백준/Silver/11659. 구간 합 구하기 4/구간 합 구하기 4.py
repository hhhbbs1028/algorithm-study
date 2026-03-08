n, m = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0]
for k in range(n):
    sums.append(sums[k]+nums[k])

for _ in range(m):    
    i, j = map(int, input().split())
    print(sums[j]-sums[i-1])