N, M = map(int, input().split())
num_list= []
maxi = []

for i in range(N):
    temp_list = list(map(int, input().split()))
    #num_list.append(temp_list)
    maxi.append(min(temp_list))
        

answer = max(maxi)


print(num_list)
print(answer)
