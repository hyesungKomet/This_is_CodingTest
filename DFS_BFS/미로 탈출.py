from collections import deque


#나는 방문한 지점에 몇번째 탐색인지 횟수를 입력하는 배열 visited를 따로 만들어서
#BFS 횟수를 적으려고 했으나 기존 미로 배열에 횟수를 입력하면 된다
#어떻게 하면 횟수를 잘 기록하나 에서 막혔는데
#그냥 기존거+1을 해주면 되는 거였다

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

maze2 = maze
#visited = [[0]*m for _ in range(n)]

queue = deque()
#cnt = 0
def bfs(tempX, tempY):
    #global cnt
    queue.append([tempX,tempY])
    maze[tempX][tempY] = 1
    #visited[tempX][tempY] = cnt

    while queue:
        
        tempX, tempY = queue.popleft()
        
       

        #maze[tempX][tempY] = 0
        
        #print("({}, {})".format(tempX,tempY))
        
        
        if tempX-1>=0:
            if maze[tempX-1][tempY] == 1:# and visited[tempX-1][tempY] == 0:
                queue.append([tempX-1, tempY])
                maze[tempX-1][tempY] = maze[tempX][tempY] + 1
                
        if tempX+1<n:
            if maze[tempX+1][tempY] == 1:# and visited[tempX+1][tempY] == 0:
                queue.append([tempX+1, tempY])
                maze[tempX+1][tempY] = maze[tempX][tempY] + 1
                #visited[tempX+1][tempY] = cnt

        if tempY-1>=0:
            if maze[tempX][tempY-1] == 1:# and visited[tempX][tempY-1] == 0:
                queue.append([tempX, tempY-1])
                maze[tempX][tempY-1] = maze[tempX][tempY] + 1
                #visited[tempX][tempY-1] = cnt

        if tempY+1<m:
            if maze[tempX][tempY+1] == 1:# and visited[tempX][tempY+1] == 0:
                queue.append([tempX, tempY+1])
                maze[tempX][tempY+1] = maze[tempX][tempY] + 1
                #visited[tempX][tempY+1] = cnt

#sol2 dx, dy로 깔끔하게 푼 해설 풀이

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs_ans(x, y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # x, y 범위가 벗어나는 경우
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            # 미로의 벽(0)에 해당하는 경우
            if maze2[nx][ny] == 0:
                continue

            # 미로를 처음 방문하는 경우
            if maze2[nx][ny] == 1:
                maze2[nx][ny] = maze2[x][y]
    
        
        
bfs(0,0)
bfs_ans(0,0)
print("my sol: \n", maze)
print("answer: ", maze[n-1][m-1])
print("ans sol: \n", maze2)
print("answer: ", maze2[n-1][m-1])

#print(cnt)
#print(visited)

        
        
