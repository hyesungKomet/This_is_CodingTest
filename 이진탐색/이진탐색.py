#이진 탐색: 반으로 쪼개가며 탐색
# 데이터가 절반씩 줄어들기에 시간 복잡도는 O(logN)
# 데이터가 1000만 단위 이상으로 넘어가면 이진 탐색같은 O(logN)의 속도가 필요!
# 자주 출제되니 코드 외우다시피하기!
# 재귀함수로 또는 반복문으로 구현

# 이진 탐색은 정렬 후 탐색해야함

# step1: 시작점, 끝점 확인 후 중간점 설정(이 때 실수면 소수점 이하 버리기)
# step2: 중간점의 데이터와 타겟 비교 -> 타겟이 더 작으면 왼쪽, 더 크면 오른쪽을 확인
# step3: 타겟이 더 작았다면 시작점은 그대로, 끝점을 중간점-1로 해서 다시 step1로 돌아가기(재귀함수!)

def binary_search(array, target, start, end):
    # 이 때 인수인 array는 정렬된 리스트여야겠죠?ㅋ
    if(start>end):
        return None
    
    # 중간값은 소숫점이 있을 땐 내림을 해준다(몫 구하기)
    mid = (start+end) // 2
    
    # 찾았을 때 인덱스 반환
    if array[mid] == target:
        return mid
    
    # 타겟이 중간지점보다 작을 때 중간보다 왼쪽에서 다시 이진 탐색 수행
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    # 타겟이 중간지점보다 클 때 중간보다 오른쪽에서 다시 이진 탐색 수행
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    
n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다")
else:
    print("{}번째 녀썩! 잡았다 요놈!!!".format(result+1))
    
# 빠르게 입력받기
# 이진 탐색 등의 문제에서 1000만 이상의 데이터를 입력받을 때 input()을 쓰면 
# 시간 초과로 오답 판정을 받을 수 있다 -> sys 라이브러리 활용

import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()
# rstrip를 써야 readline()으로 입력했을 때 입력 후 엔터가 줄 바꿈 기호로
# 입력되는데, 이 공백 문자가 제거된다!

print(input_data)

# 이진 탐색 트리
# 부모 노드보다 왼쪽 자식 노드가 작다
# 부모 노드보다 오른쪽 자식 노드가 크다

# 이진 탐색 트리는 자료구조 때 다뤘으니 참고하기...
# 데이터베이스에서 이같은 트리 자료구조로 방대한 양의 데이터를 관리한다...!