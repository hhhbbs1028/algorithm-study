n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums_all = [0]*1000001
count=0
for num in nums:
    nums_all[num]+=1
for num in nums:
    if x-num>0 and num>(x//2):
        if nums_all[x-num]!=0:
            count+=1
print(count)