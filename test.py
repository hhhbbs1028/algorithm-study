from collections import deque

def findPath(network_nodes, network_from, network_to, frequency):
    # 1. 인접 리스트 초기화 (1-based)
    graph = [[] for _ in range(network_nodes + 1)]

    # 2. 조건에 맞는 간선만 추가
    for i in range(network_nodes - 1):
        u = network_from[i]
        v = network_to[i]
        if abs(frequency[u - 1] - frequency[v - 1]) <= 1:
            graph[u].append(v)
            graph[v].append(u)

    # 3. 최장 거리 계산
    return longest_path_from_graph(graph, network_nodes)


def longest_path_from_graph(graph, n):
    def bfs_farthest_node(start):
        visited = [False] * (n + 1)
        dist = [0] * (n + 1)
        queue = deque([start])
        visited[start] = True
        farthest = start

        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if not visited[i]:
                    visited[i] = True
                    dist[i] = dist[v] + 1
                    queue.append(i)
                    if dist[i] > dist[farthest]:
                        farthest = i
        return farthest, dist[farthest]

    def bfs_component(start, visited):
        queue = deque([start])
        visited[start] = True
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)

    visited = [False] * (n + 1)
    max_dist = 0

    for i in range(1, n + 1):
        if not visited[i] and graph[i]:
            bfs_component(i, visited)
            u, _ = bfs_farthest_node(i)
            _, dist = bfs_farthest_node(u)
            max_dist = max(max_dist, dist)

    return max_dist
