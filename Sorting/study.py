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

insertion_sort()
