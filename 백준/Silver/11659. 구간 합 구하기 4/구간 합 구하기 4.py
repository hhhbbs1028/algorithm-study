import itertools

n, m = map(int, input().split())
nums = list(map(int, input().split()))
acc = list(itertools.accumulate(nums, initial=0))

for _ in range(m):
    i, j = map(int, input().split())
    print(acc[j]-acc[i-1])