
# 점화식 생각하기!!
# a(i)  = max(a(i-1), a(i-2)+k) 여기서 k는 i번째 식량창고의 식량의 양
# 포인트: a(i)를 구할 때 a(i-3), a(i-4)는 신경쓸 필요가 없다
# 이전에 a(i-1), a(i-2)를 구할 때 이미 따졌기 때문!


n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

# 다이나믹 프로그래밍(바텀업 방식)

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])


print(d[n-1])

