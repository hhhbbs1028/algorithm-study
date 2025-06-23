n = int(input())

graph = []

# 맵 그리기
for _ in range(n):
    graph.append(list(map(int, input().split())))


def dfs(i, j):
    x = [1,-1,0,0]
    y = [0,0,1,-1]
    visited[i][j]=True
    
    for d in range(4):
        dx=i+x[d]
        dy=j+y[d]
        if 0<=dx<n and 0<=dy<n and not visited[dx][dy]:
            dfs(dx, dy)


def count_map(graph, water):
    count=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>water:
                "수위 넘음"
            if not visited[i][j]:
                "not visited"
            if graph[i][j]>water and not visited[i][j]:
                print("수위 ",water, "일 때 1 count 1증가", count)
                dfs(i, j)
                count+=1
    return count

m_water = set()
for i in range(n):
    for j in range(n):
        if graph[i][j] not in m_water:
            m_water.add(graph[i][j])

print(m_water)
c=0
for w in m_water:
    visited = [[False]*n for _ in range(n)]
    c_m = count_map(graph, w)
    print("count : ", c_m)
    if c<c_m:
        c=c_m
print(c)