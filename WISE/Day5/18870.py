import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
s_nums = sorted(list(set(nums)))
for i in nums:
    idx = s_nums.index(i)
    print(idx, end=" ")