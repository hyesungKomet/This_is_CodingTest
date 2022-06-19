
# 6
# -1 /5
# /3 -1
# /3 /2
# /2 /3
# f(6)을 구할 때 세분화되면서
# f(5), f(3), f(2) 등이 쓰임! -> dynamic programming


x = int(input())


# 바텀업 방식 사용!
save = [0] * (x*5)
d = [0] * 30001 # dp테이블의 크기를 문제에서 설정한 범위로 그냥 해줌!
save[2] = 1
save[3] = 1
save[5] = 1

num = 2

while num != x:
    if save[num+1] == 0 or save[num+1] > save[num]:
        save[num+1] = save[num] + 1
    if save[num * 2] == 0 or save[num * 2] > save[num]:
        save[num * 2] = save[num] + 1
    if save[num * 3] == 0 or save[num * 3] > save[num]:
        save[num * 3] = save[num] + 1
    if save[num * 5] == 0 or save[num * 5] > save[num]:
        save[num * 5] = save[num] + 1
        
    num += 1

# 답안 예시 ---코드 잘 숙지하기!!---
for i in range(2, x+1):

    # 1 빼는 경우
    d[i] = d[i-1] + 1

    # 2, 3, 5로 나눌 수 있는 경우
    if i % 2 == 0:
        d[i] = min(d[i//2]+ 1, d[i])

    if i % 3 == 0:
        d[i] = min(d[i//3]+1, d[i])

    if i % 5 == 0:
        d[i] = min(d[i//5]+1, d[i])

        
    
    
print(save[x])
print(d[x])
