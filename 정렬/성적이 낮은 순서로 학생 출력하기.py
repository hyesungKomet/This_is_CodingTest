n = int(input())

#sol1 - 기본 정렬 라이브러리 사용
score_dic = []

for i in range(n):
    name, score = input().split()
    score = int(score)
    score_dic.append((name, score))

result = sorted(score_dic, key = (lambda x: x[1]))

for i in result:
    print(i[0], end=' ')

#sol2 - 계수 정렬 사용~ 하려했는데...웨안뒈...점수 중복의 경우
# 점수 중복으로정렬은 되어도 거기에 맞는 사람 이름 정렬이 왤케 잘 안되지...

m = int(input())

seq = []

#james 30 john 25 hailey 100

for i in range(m):
    name2, score2 = input().split()
    score2 = int(score2)
    seq.append((name2, score2))

seq = sorted(seq, key = lambda x:x[1])

for i in seq:
    print(i[0], end=' ')
