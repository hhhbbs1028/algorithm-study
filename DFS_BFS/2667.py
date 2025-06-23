
n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]

# ['0110100', '0110101', '1110101', '0000111', '0100000', '0111110', '0111000']

# 단지수 / 단지별 집의 수(오름차순)

visited = [[False]*n for _ in range(n)]


def dfs(i, j):
    visited[i][j]=True
    count=1

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for k in range(4):
        nx=i+dx[k]
        ny=j+dy[k]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny]==1:
            count+=dfs(nx, ny)
    return count

houses = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            houses.append(dfs(i, j))

houses.sort()
print(len(houses))
for h in houses:
    print(h)


