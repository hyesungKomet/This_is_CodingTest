# 백준 #11047
# 거스름돈 문제와 매우 유사

n, money = map(int, input().split())
coin_types = []
for i in range(n):
    coin_types.append(int(input()))

coin_types.sort(reverse = True)
count = 0

for coin in coin_types:
    count += money // coin
    money = money % coin
    
print(count)
