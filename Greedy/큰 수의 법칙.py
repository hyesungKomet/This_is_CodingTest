
N, M, K = map(int, input().split())

nums = input().split()
for i in range(len(nums)):
    nums[i] = int(nums[i])

#nums = list(map(int, input().split())) #이런 짧은 방식이 있다!


maxi = max(nums)    #가장 큰 수 저장
cnt = 0

for i in range(len(nums)):
    if nums[i] == maxi:
        del nums[i]

secmaxi = max(nums) #두 번째로 큰 수 저장

#nums.sort()
#first = nums[n-1]
#second = nums[n-2]     #이렇게 간단한 코드였다...!

#이부분은 낫베드..?
m = M
while (m>0):
    if m >= K:
        cnt += maxi * K
        m -= K
    else:
        cnt += maxi * m
        m == 0
    if m == 0:
        break
    m -= 1
    cnt += secmaxi

#이지만 반복문이 아닌 수식으로도 해결될 문제였다

#maxi_cnt = M // (K+1) * K + M % (K+1)
#secmaxi_cnt = M - maxi_cnt

answer = maxi_cnt * maxi + secmaxi_cnt * secmaxi
print(answer)
print(cnt)

            
    
