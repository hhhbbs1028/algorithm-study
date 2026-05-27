def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        if j==len(array):
            a = array[i-1:]
        else:
            a = array[i-1:j]
        a.sort()
        answer.append(a[k-1])
    return answer