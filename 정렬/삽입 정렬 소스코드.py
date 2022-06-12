# 삽입 정렬의 시간 복잡도
# 똑같이 2중 반복문이라 O(N^2)
# but 거의 정렬된 상태의 리스트에 쓰면 빠르게 동작한다!

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    for j in range(i, 0, -1): #인덱스 i부터 1까지 감소하며 반복
        if array[j] < array[j-1]: #한칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: #자기보다 작은 데이터를 만나면 그 자리에서 멈춘다
            break

print(array)
