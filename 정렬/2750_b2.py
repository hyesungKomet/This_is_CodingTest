# 2750

# n이 1000이하이므로 O(n^2)인 선택, 삽입정렬 등을 사용해도 된다

# 나는 계수정렬을 사용해봐따 -> 중복이 없어서 메리트가 없으...

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
'''
sorting = [0] * (max(arr)+1)

for i in arr:
    sorting[i] += 1

for i in range(len(sorting)):
    if sorting[i] > 0:
        for j in range(sorting[i]):
            print(i)
'''

arr.sort()
for i in arr:
    print(i)
