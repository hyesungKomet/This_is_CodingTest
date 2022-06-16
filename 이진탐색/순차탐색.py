#순차 탐색 시간 복잡도
#최대 N번의 비교 연산 필요 -> 최악의 경우 O(N)

#순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    #각 원소 하나하나 확인
    for i in range(len(array)):
        if array[i] == target:
            return i+1 #현재 위치 반환
        
print("생성할 원소 개수 입력한 뒤 한 칸 띄고 찾을 문자열 입력: ")
input_data = input().split()
n = int(input_data[0]) #원소의 개수
target = input_data[1]

print("적은 원소 개수만큼 문자열 입력(단 구분은 띄어쓰기 한 칸으로): ")
array = input().split()

#순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))