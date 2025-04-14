# BFS/DFS 음료수 얼려먹
# [1, 1, 1], 
# [0, 0, 0], 
# [1, 1, 1]

global count
count = 0

def dfs(x,y):
    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우 이동 시 x 변화량
    dy = [0, 0, -1, 1]  # 상, 하, 좌, 우 이동 시 y 변화량
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and icemap[nx][ny]==0:
            dfs(nx, ny)


def divideIce():
    global count

    for i in range(n):
        for j in range(m): 
            if icemap[i][j]==0 and not visited[i][j]:
                count += 1
                dfs(i,j)

def solutionDfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if icemap[x][y] == 0:
        icemap[x][y] = 1
        solutionDfs(x-1, y)
        solutionDfs(x, y-1)
        solutionDfs(x+1, y)
        solutionDfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())
icemap = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

divideIce()
print(count)

# solution DFS 
for i in range(n):
    for j in range(m):
        if solutionDfs(i,j) == True:
            result+=1
            
# global 선언을 함수 내부에서도 정의해야 사용 가능
# list를 사용할 때 *를 사용할 경우 같은 참조 사용 -> for range로 바꾸기
