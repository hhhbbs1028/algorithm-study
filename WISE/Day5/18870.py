n = int(input())
nums = list(map(int, input().split()))
# count = [[] for _ in range(len(nums))]
# for i in range(len(nums)):
#     for j in range(i, len(nums)):
#         if nums[i]<nums[j] and nums[i] not in count[j]:
#             count[j].append(nums[i])
#         elif nums[i]>nums[j] and nums[j] not in count[i]:
#             count[i].append(nums[j])

# for c in count:
#     print(len(c), end=" ")

s_nums = {}
for n in nums:
    if n in s_nums:
        s_nums[n]+=1
    else:
        s_nums[n]=1

for n in nums:
    c = 0
    for m in s_nums:
        if m<n:
            c+=s_nums[m]
    print(c, end=" ")