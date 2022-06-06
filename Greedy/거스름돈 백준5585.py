# 백준 #5585

n = int(input())
remainder = 1000 - n

cnt = 0

#sol 1

#n = 380 remainder = 620 q500 = 1 r500 = 120 q100 = 1 r100 = 20 q50 = 0 r50 = 20 q10 = 2
#divmod 나름 쓸만하다
q500, r500  = divmod(remainder, 500)
q100, r100 = divmod(r500, 100)
q50, r50 = divmod(r100, 50)
q10, r10 = divmod(r50, 10)
q5, r5 = divmod(r10, 5)
q1 = r5

#sol 2

#500, 100, 50, 10, 5, 1을 리스트에 담아서 반복문 돌리는게 더 깔끔하다
count = 0
coin_types = [500, 100, 50, 10, 5, 1]
for coin in coin_types:
    count += remainder // coin
    remainder = remainder % coin
    
cnt = (q500+q100+q50+q10+q5+q1)
print(cnt)
print(count)
