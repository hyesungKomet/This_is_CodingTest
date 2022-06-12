# 피벗(Pivot)이라는 기준을 두고 피벗보다 큰 데이터와 작은 데이터 교환
# 호어 분할(Hoare Partition): 리스트에서 첫번째 데이터를 피벗으로!
# 재귀함수로 구현(피벗 기준 분리가 끝나면 왼, 오른쪽에서 다시 피벗 정해서 퀵정렬)

# 퀵 정렬의 시간 복잡도
# O(NlogN) (평균 시간 복잡도)
# 예를 들어 8개의 수를 정렬할 때 피벗을 딱 중간으로 잡으면
# 쪼개질 때 1 -> 2 -> 4 -> 8로 쪼개져서 약 log8(이때 밑은 항상 2!)가 된다
# 1000개일 때는 log1000이 약 10으로 매우 줄어듦
# but 데이터가 거의 정렬된 상태에서 첫번째 원소를 피벗으로 설정하면 비효율적
# 심하면 최대 O(N^2)까지도 된다
#  -> C++의 내장 라이브러리나 파이썬의 기본 정렬 라이브러리는 log(NlogN)을
# 보장하기 위해 피벗값 설정시 추가적인 로직이 더해진다

array = [5,7,9,0,3,1,6,2,4,8]
array2 = array

# 전통적인 방식의 퀵 정렬
def quick_sort(array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start #피벗은 첫 번째 원소(호어 분할)
    left = start + 1 #여기서 left는 피벗 기준이 아닌 전체 데이터상의 왼쪽!
    right = end
    while left<= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 왼쪽의 큰 데이터가 오른쪽의 작은 데이터 인덱스보다 클 때 
        if left > right: # == 엇갈렸을 때
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈린게 아니면 작은 데이터와 큰 데이터 교체
            array[right], array[left] = array[left], array[right]

    # 분할 이후 왼쪽 부분과 오른쪽 부분 각각 정렬 수행(재귀함수)
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
    # right 인덱스에 pivot 인덱스의 값이 들어갔으니 이렇게 됨


# 파이썬의 장점을 살린 퀵 정렬
def quick_sort_py(array):
    # 리스트 원소가 1개 이하면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소(호어 분할)
    tail = array[1:] # 피벗 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분 각각 정렬 수행 후 전체 리스트 반환
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)



quick_sort(array, 0, len(array)-1)
print(array)

print(quick_sort_py(array2))
