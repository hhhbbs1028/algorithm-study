n = int(input())

ocean = []
for _ in range(n):
    ocean.append(list(map(int, input().split())))
# 0: 빈 칸
# 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위치
# 4 3 2 1
# 0 0 0 0
# 0 0 9 0
# 1 2 3 4

for i in range(n):
    for j in range(n):
        if(ocean[i][j]==9):
            x = i
            y = j
            break

count = 0
size = 2
ocean[x][y] = 0
eat = 0

def check_eat():
    global size
    global eat
    if(eat == size):
        size+=1
        eat = 0 

def calculate_distace(start, fish):
    print(start, fish)
    distance = 0
    fishx = fish[0]
    fishy = fish[1]
    x = start[0]
    y = start[1] 

    count = 0
    while((x!=fishx or y!=fishy) and count<n*n):
        if(0<=fishx<x<n):
            if(ocean[x-1][y]>size): continue
            else:
                distance+=1
                x-=1
        if(0<=x<fishx<n):
            if(ocean[x+1][y]>size): continue
            else:
                distance+=1
                x+=1

        if(0<=fishy<y<n):
            if(ocean[x][y-1]>size): continue
            else:
                distance+=1
                y-=1
        if(0<=y<fishy<n):
            if(ocean[x][y+1]>size): continue
            else:
                distance+=1
                y+=1
        count+=1
    return distance

while(True):
    fishes = []
    for i in range(n):
        for j in range(n):
            if(0<ocean[i][j]<=size):
                fishes.append((i,j))

    if(len(fishes)==0): break

    fishx = fishy = n
    min_distance = 2*n
    for (i, j) in fishes:
        print("calculate distance : ", i, j)
        distance = calculate_distace((x,y), (i,j))
        
        print("end calculate distance")
        if distance<min_distance:
            min_distance = distance
            fishx = i
            fishy = j
    
    print("out of calculate distance")
    count+=min_distance
    if(ocean[fishx][fishy]==size): eat+=1
    ocean[fishx][fishy] = 0
    x, y = fishx, fishy
    check_eat()

print(count)
