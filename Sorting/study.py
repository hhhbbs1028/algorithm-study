arr=[7,5,9,0,3,1,6,2,4,8]

# 선택정렬
def selection_sort():
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1, len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)
    # 파이썬에서 스와핑 : temp 사용 없이 바로 가능
    

# 삽입정렬 : 보통 사람이 하는 정렬, 카드 정렬
def insertion_sort():
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                print(arr)
            else:
                break
    print(arr) 

# 퀵정렬
def quick_sort(start, end):
    if start>=end:
        return
    pivot = start
    left = start + 1
    right = end
    while left<=right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(start, right-1)
    quick_sort(right+1, end)
    
# 파이썬의 장점을 살린 퀵 정렬 
def quick_sort_python(array):
    if len(array)<=1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left = [x for x in tail if x<=pivot]
    right = [x for x in tail if x>pivot]
    
    return quick_sort_python(left)+[pivot]+quick_sort_python(right)

# 계수정렬
def count_sort():
    count = [0]*max(arr)
    
    for i in range(len(arr)):
        count[arr[i]]+=1
    
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')
            