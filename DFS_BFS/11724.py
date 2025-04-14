n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs_e(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs_e(i)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs_e(i)
        count+=1

print(count)

# def dfs(graph, start):
#     if not visited[start]:
#         visited[start] = True
#         check.remove(start)
#         # print(start, end=" ")

#     for i in range(m):
#         u, v = graph[i]
#         if u==start:
#             if not visited[v]:
#                 dfs(graph, v)
                
#         if v==start:
#             if not visited[u]:
#                 dfs(graph, u)

# re_graph = [[] for _ in range(n+1)]
# def arrange(graph):
#     for i in range(m):
#         u, v = graph[i]
#         re_graph[u].append(v)
#         re_graph[v].append(u)


# check = [ i for i in range(1, n+1)]
# # [1, 2, 3, 4, 5, 6]
# dfs(graph, 1)

# count = 1
# while(check):
#     for i in check:
#         dfs(graph,i)
#         count = count+1

print(count)


