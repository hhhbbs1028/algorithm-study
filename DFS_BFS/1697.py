from collections import deque
n, k = map(int, input().split())

# x -> 2x or x+-1
# bfs

MAX = 100001
visited = [False]*MAX
distance = [0]*MAX

queue = deque([n])
visited[n] = True

while queue:
    v = queue.popleft()
    path = [v-1, v+1, v*2]
    
    if(v==k):
        print(distance[v])
        break
    
    for i in path:
        if 0<=i<MAX and not visited[i]:
            distance[i] = distance[v] + 1
            queue.append(i)
            visited[i] = True