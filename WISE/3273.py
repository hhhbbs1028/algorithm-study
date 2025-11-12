n = int(input())
nums = list(map(int, input().split()))
x = int(input())

count=0
# print(nums)
for a in nums:
    b = x-a
    if b in nums and a<b:
        count+=1
        
print(count)