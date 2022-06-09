N, M = map(int, input().split())
x, y, head = map(int, input().split())

#방문한 위치 지정 위한 맵 초기화
gameMap = [[0] * M for _ in range(N)]

#시작좌표 방문처리
gameMap[x][y] = 1

pos = []

for n in range(N):
    pos.append(list(map(int, input().split())))

#북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

### 왼쪽으로 회전하는 함수 생성이 포인트였다..!
### 처음 받은 방향(동서남북)을 인덱스로 활용(dx, dy)하며
### 방문했는지 여부를 판단하는 문제의 중요한 키였다
def turn_left():
    global head
    head -= 1
    if head == -1:
        head = 3
    

cnt = 1 #처음 방문했으니 1
turn_time = 0

while True:
    turn_left() #처음엔 북쪽향함 -> 왼쪽으로 돌아야됨

    tempX = x+dx[head]
    tempY = y+dy[head]

    #나는 가장자리를 방문할 경우 그다음 인덱스는
    #초과할 수 있어서 그걸 따로 예외처리했지만
    #문제 조건에서 가장자리는 다 바다라고 했으니
    #그런 경우는 애초에 고려하지 않아도 됐다..!
    if gameMap[tempX][tempY] == 0 and pos[tempX][tempY] == 0:
        gameMap[tempX][tempY] = 1
        x = tempX
        y = tempY
        cnt+=1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        tempX = x - dx[head]
        tempY = y - dy[head]
        #뒤로 갈 수 있을 때
        if pos[tempX][tempY] == 0:
            x = tempX
            y = tempY
        else:
            break
        turn_time = 0
print(cnt)
'''    
    for arr in arrows:
        if 0<=x+arr[0]<N and 0<=y+[arr[1]]<M:
            if pos[x+arr[0]][y+arr[1]] == 0:
                pos[x+arr[0]][y+arr[1]] = 2
                x, y = x+arr[0],y+arr[1]
                noWay =False
                cnt+=1
                continue
            else:
                continue
        else:
            continue
    if noWay == True:
        if pos[originX][originY] == 2:
            x, y = originX, originY
        else:
            break
          
'''

