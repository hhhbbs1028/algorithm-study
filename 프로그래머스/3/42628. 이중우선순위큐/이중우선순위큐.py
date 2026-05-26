import heapq
def solution(operations):
    answer = []
    heapq.heapify(answer)
    for operation in operations:
        operator, operand = operation.split()
        if operator == 'I':
            heapq.heappush(answer, int(operand))
        elif operator == 'D':
            try:
                if operand == '1': # 최댓값 삭제
                    answer = [-x for x in answer]
                    heapq.heapify(answer)
                    heapq.heappop(answer)
                    answer = [-x for x in answer]
                    heapq.heapify(answer)
                elif operand =='-1': # 최솟값 삭제
                    heapq.heappop(answer)
            except IndexError:
                print("IndexError")
                continue
    if not answer:
        return [0,0]
    else:
        ma, mi = max(answer), min(answer)
        return ([ma, mi])