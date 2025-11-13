n, c = map(int, input().split())
nums = list(map(int, input().split()))
s_nums = []

for i in range(len(nums)):
    idx=-1
    c=0
    for j in range(len(s_nums)):
        a, b = s_nums[j]
        if nums[i]==a:
            idx = j
            c = b
            break
    
    if idx<0:
        s_nums.append((nums[i], 1))
    else:
        s_nums[j] = nums[i], c+1


s_nums = sorted(s_nums, key=lambda x: x[1], reverse=True)
for num, c in s_nums:
    for _ in range(c):
        print(num, end=" ")


# 1. 해시값 추가 방법
# 2. 해시값 in 사용 방법
# 3. 튜플 in 사용법
# 4. 튜플에서 index 사용방법
# 5. 튜플에서 값 추가 방법 -> temp 처럼 따로 하는 방법밖에 없는지