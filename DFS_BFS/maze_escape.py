from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))


# bfs는 모든 간선의 거리가 동일(1)하고, 같은 레벨의 노드끼리 차례로 탐색하므로
# 먼저 탐색하는 노드가 최단거리
# 최단거리 보장


# 구조
# 시작 노드 queue에 저장
# 큐가 빌 때까지 반복
#     큐의 가장 왼쪽 노드와 연결된 노드들을 차례로 탐색
#     방문하지 않았다면 큐에 삽입