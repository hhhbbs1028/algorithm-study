from itertools import combinations
import copy

n, m = map(int, input().split()) # (3 ≤ N, M ≤ 8)

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# 0 빈칸 / 1 벽 / 2 바이러스
# 안전 영역의 최대 크기를 출력

def dfs(i, j):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    for k in range(4):
        nx=i+dx[k]
        ny=j+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if g_copy[nx][ny]==0:
                g_copy[nx][ny]=2
                dfs(nx,ny)
                

empty_cells=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            empty_cells.append((i,j))
wall_combinations = list(combinations(empty_cells, 3))
# print(wall_combinations)

virus_cells=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            virus_cells.append((i,j))
# print(virus_cells)

counts=[]
for comb in wall_combinations:
    g_copy = copy.deepcopy(graph)
    for x,y in comb:
        g_copy[x][y]=1

    for x,y in virus_cells:
        dfs(x,y)

    count=0
    for i in range(n):
        for j in range(m):
            if g_copy[i][j]==0:
                count+=1
    counts.append(count)
print(max(counts))

