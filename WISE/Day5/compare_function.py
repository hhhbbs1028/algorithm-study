from functools import cmp_to_key

def compare(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    else:
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            return 0

arr = [('a', 2), ('b', 1), ('c', 2)]
print(sorted(arr, key=cmp_to_key(compare)))