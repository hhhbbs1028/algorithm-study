t = int(input())
for _ in range(t):
    nums = list(input())
    check = [ [] for i in range(11)]
    for i in range(len(nums)):
        check[int(nums[i])].append(i)
    c = True
    for i in range(10):
        position = check[i]
        if len(position)!=0:
            if len(position)!=2:
                c = False
            else:
                if abs(position[1]-position[0]-1)!=i:
                    c = False
    
    print("yes" if c else "no")