import sys
sys.setrecursionlimit(50*50)

def dfs(x, y, cabbage):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    if cabbage[x][y] == 1:
        cabbage[x][y] = 0
        dfs(x-1, y, cabbage)
        dfs(x+1, y, cabbage)
        dfs(x, y-1, cabbage)
        dfs(x, y+1, cabbage)
        return True
    return False
    

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    # 가로 m, 세로 n
    cabbage = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        # X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)
        cabbage[y][x] = 1
    
    
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j, cabbage)==1:
                result+=1 
    
    print(result)


# 아이스크림 문제와 비슷한 유형
# map에서 그룹할 수 있는 개수 물어보기
# def dfs(x, y, cabbage):
#     if x<=-1 or x>=n or y<=-1 or y>=m:
#         return False
    
#     if cabbage[x][y] == 1:
#         cabbage[x][y] = 0
#         dfs(x-1, y, cabbage)
#         dfs(x+1, y, cabbage)
#         dfs(x, y-1, cabbage)
#         dfs(x, y+1, cabbage)
#         return True
#     return False
# 형식 외우기! 
# 범위 벗어나면 False, 가능하면 True return, 상하좌우 탐색 
# 메인 함수 : map에서 dfs True 리턴할 경우 count+1 