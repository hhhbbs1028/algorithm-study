n = int(input())
arr = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))
sorted_arr = sorted(set(arr))

def ifExist(number):
    l,r = 0, len(sorted_arr)-1
    while l<=r:
        m = (l+r) // 2
        if sorted_arr[m] > number:
            r = m-1     
        elif sorted_arr[m] < number:
            l = m+1
        elif sorted_arr[m]==number:
            return True
    
for number in numbers:
    print(1) if ifExist(number) else print(0)