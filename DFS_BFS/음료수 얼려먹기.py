n, m = map(int, input().split())

#얼음판 방문여부 체크용 배열
#visited = [[0] * m for _ in range(n)]

ice = []

#얼음판 입력받기
for i in range(n):
    ice.append(list(map(int, input())))
cnt=0

#0인 얼음판 탐색하는 함수

#이전 DFS 메소드에는 방문체크용 배열, 실제 체크할 그래프를 따로 인수로 뒀는데
#여기서는 얼음판자체가 0,1로 되어있고 이중 0을 1로 바꿔줌으로써 방문체크까지 가능하니
#얼음판 하나로도 가능하다
def ice_hole(x,y):
    #visited[x][y] = 1

    #범위를 벗어나면 종료하기
    #나는 범위에 해당하는 4가지를 if문으로 나누려고 했는데
    #이렇게 범위에 벗어날 때 종료하는 방식이 더 깔끔한듯!
    if x>=n or x<0 or y>=m or y<0:
        return False

    if ice[x][y]==0:
        #방문체크
        ice[x][y]=1

        ice_hole(x+1,y)
        ice_hole(x-1,y)
        ice_hole(x,y+1)
        ice_hole(x,y-1)
        return True
    return False
        
    '''    
    if ice[x+1][y]==0 and visited[x+1][y]==0:
        ice_hole(ice, x+1, y, visited)
    
    if ice[x-1][y]==0 and visited[x-1][y]==0:
        ice_hole(ice, x-1, y, visited)

    if ice[x][y+1]==0 and visited[x][y+1]==0:
        ice_hole(ice, x, y+1, visited)

    if ice[x][y-1]==0 and visited[x][y-1]==0:
        ice_hole(ice, x, y-1, visited)
    '''

    
for i in range(n):
    for j in range(m):
        if ice_hole(i,j):
            cnt+=1


print(cnt)
