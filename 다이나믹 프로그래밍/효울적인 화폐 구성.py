n, m = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

d = [0] * 10000

# 우선 화폐의 종류가 되는 금액은 만드는 데 최소 화폐 개수가 1개이니
# 이를 dp 테이블에 우선 담아준다.

# 점화식을 f(i) = min(f(i), f(i-k)+1)로 한건 맞았다! 매우 잘함 짝짝짝
# 답도 맞았다!! 다이나믹 프로그래밍의 장인이 되어가는건가ㅎㅎ

for i in range(n):
    d[coin[i]] = 1
# d[i] = j 는 i원을 만드는 데 최소 화폐 개수가 j개인 것이다

# 가장 작은 화폐의 종류에 해당하는금액부터 시작
for i in range(min(coin),m+1):
    # 임시 리스트에 가능한 경우 저장한 뒤 그 중 최솟값을 취한다
    temp = []
    for j in coin:
        if i-j>0 and d[i-j] != 0:
            temp.append(d[i-j]+1)

    # 안담긴 경우는 만들 수 없는 금액이므로 스킵
    if len(temp) == 0:
        continue
    d[i] = min(temp)


if d[m] == 0:
    print(-1)
else:
    print(d[m])

# 예시 답안

d = [10001] * (m+1) #10001은 만들 수 없음을 의미(m이 10000이하의 범위임)

# 다이나믹 프로그래밍 진행(바텀업)
d[0] = 0

for i in range(n):
    for j in range(coin[i], m+1):
        if d[j-coin[i]] != 10001: #d[j-coin[i]]의 방법이 존재한 경우
            d[j] = min(d[j], d[j-coin[i]]+1)
            # 나는 0으로 초기화했어서 min에서 0인 부분이 걸리는데
            # 여기선 10001로 해서 걸리지 않음

if d[m] == 10001:
    print(-1)
else:
    print(d[m])








