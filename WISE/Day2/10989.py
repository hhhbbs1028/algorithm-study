n = int(input())
nums = [0]*10001
# 10,000보다 작거나 같은 자연수

for _ in range(n):
    nums[int(input())]+=1

for i in range(10001):
    if nums[i]!=0:
        for j in range(nums[i]):
           print(i)    