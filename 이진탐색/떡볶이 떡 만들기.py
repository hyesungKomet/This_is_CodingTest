# 전형적인 이진 탐색 문제이자 파라메트릭 서치(Parametric Search 유형의 문제)
# Parametric Search는 최적화 문제를 결정 문제(예, 아니오로 답하는 문제)로
# 바꾸어 해결하는 기법 ,ex) 범위 내의 조건 만족하는 가장 큰 값 찾아라!

# 높이 H의 범위를 반복해서 조정하며 좁혀간다!
# 탐색 범위가 1~10억까지이니 순차탐색은 시간초과될 것! 이진 탐색 떠올리기!


# sol1: 재귀 함수로 처리하기
def binary_search(arr, target, start, end):
    if start>end:
        return None
    
    mid = (start+end) // 2
    gift = 0
    for i in arr:
        if i>mid:
            gift += (i-mid)
    if target == gift:
        return mid
    elif target<gift:
        return binary_search(arr, target, mid+1, end)
    elif target>gift:
        return binary_search(arr, target, start, mid-1)



n, m = map(int, input().split())

ricecakes = list(map(int, input().split()))

start = 0
end = max(ricecakes)

print(binary_search(ricecakes, m, start, end))


# sol2: 반복문으로 처리하기

result = 0
while(start<=end):
    
    mid = (start+end) // 2
    gift = 0
    for i in ricecakes:
        if i>mid:
            gift += (i-mid)
            
    
    if m<=gift:
        # 최대한 덜 잘랐을 때가 정답이므로 일단 result에 기록!
        result = mid           
        start = mid+1
    elif m>gift:
        end=mid-1

print(result)
