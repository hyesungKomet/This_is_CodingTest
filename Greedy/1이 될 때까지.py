#이건 반복문이 아닌 수식으로 끝낼만한것같다..!

N, K = map(int, input().split())
cnt = 0

# n=17 -> -1 /4 -1 --> 3
# 17 4 -> /4 /4 -1
# 18 4 -> /4 /4 -2
# 97 4 -> -1 /4 /4 -2 /4 
#         96 24  6  4  1

while(N != 1):
    if N % K != 0:
        cnt += (N%K)
        N -= (N%K)
    else:
        N = N // K
        cnt += 1
    
print(cnt)
