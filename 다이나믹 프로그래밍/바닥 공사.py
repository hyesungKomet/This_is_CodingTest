n = int(input())

d = [0] * 1001

# f(i) = f(i-2) * 2

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = d[i-2]*2 + d[i-1] % 796796 #나머지연산 한건 출력 조건에 있음!
    #d[i] = d[i-2]*2 + d[i-1]

print(d[n])
