# 선택 정렬의 시간 복잡도
# N + (N-1) + (N-2) + ... + 2 = N x (N+1) / 2
# -> O(N^2) : 2중 반복문 사용되어서

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #swap

print(array)
