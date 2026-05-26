import heapq
from collections import deque
def solution(jobs):
    # 작업 요청 시점 / 작업 소요 시간
    # 작업 소요시간 짧은 것 - 작업 요청 시각 빠른 것 - 작업의 번호가 작은 것 
    # 반환(요청 - 종료)의 평균
    
    jobs.sort()
    queue = []
    n = len(jobs)
    t = 0
    c = 0
    qjobs = deque(jobs)
    while qjobs or queue:
        if not qjobs: # 남아있는 jobs 없을 경우
            time, start = heapq.heappop(queue)
            t += (time + max(start - t, 0))
            c += (t - start)
            print("queue 작업", (start, time))
                
        else:
            start, time = qjobs.popleft()
            if t >= start: # 그동안 작업 전부 queue에 append
                heapq.heappush(queue, (time, start))
                print("queue 추가", (start, time))
            else: 
                if queue:
                    qjobs.appendleft((start, time))
                    time, start = heapq.heappop(queue)
                    t += (time + max(start - t, 0))
                    c += (t - start)
                    print("queue 작업", (start, time))

                else: # 대기 중 작업 없음
                    t += (time + max(start - t, 0))
                    c += (t - start)
                    print("바로 작업", (start, time))
        
    answer = c // n
    return answer