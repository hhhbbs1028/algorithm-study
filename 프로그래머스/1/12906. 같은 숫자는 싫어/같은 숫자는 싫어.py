def solution(arr):
    answer = []
    temp = arr[0]
    answer.append(temp)
    for n in arr:
        if n!=temp:
            answer.append(n)
        temp = n
    return answer