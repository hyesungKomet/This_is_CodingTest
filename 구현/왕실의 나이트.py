position = input()
x, y = position[0], position[1]
numX = ord(x) - 96 #96이라고 하면 못알아먹으니까 ord('a') 가 좋겠지요 훠훠
numY = int(y)

cnt = 0

#이렇게 경우의 수를 if문으로 하나하나 나누기 이전에 리스트로 담아볼 생각!
#내부 벡터는 바꿀필요없으니 튜플로!
ways = [(2,1), (1,2), (2,-1), (1,-2), (-2,1), (-1,2), (-2,-1), (-1,-2)]

for way in ways:
    posX, posY = numX+way[0], numY+way[1]
    if 1<=posX<=8 and 1<=posY<=8:
        cnt += 1

print(cnt)
