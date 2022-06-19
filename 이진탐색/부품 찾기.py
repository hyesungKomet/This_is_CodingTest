# sol1 재귀함수 이용한 이진 탐색
def search(arr, target, start, end):
    
        if start>end:
            return None

        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            return search(arr, target, start, mid-1)

        elif arr[mid] < target:
            return search(arr, target, mid+1, end)

# sol2 반복문 이용한 이진 탐색
def binary_search(arr, target, start, end):
    while start<=end:

        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            end = mid-1

        elif arr[mid] < target:
            start = mid+1
    return None




n = int(input())

things = list(map(int, input().split()))
# 계수 정렬용 리스트 따로 복사
things2 = things

m = int(input())

check = list(map(int, input().split()))

things.sort()

for target in check:
    
    if search(things, target, 0, n-1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')

# sol3 계수 정렬 이용
print()
sorting = [0] * (max(things)+1)

for element in things2:
    sorting[element]+=1

for target in check:
    if sorting[target] == 0:
        print('no', end=' ')
    else:
        print('yes', end=' ')


# sol4 집합 자료형(set()) 이용

N = int(input())
# 가계에 있는 전체 부품 번호를 입력받아서 집합 자료형에 기록
array = set(map(int, input().split()))

M = int(input())

x = list(map(int, input().split()))

print(array)

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
