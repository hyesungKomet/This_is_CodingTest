# A의 원소의 합이 최대가 되려면
# A의 가장 작은 원소부터 B의 가장 큰 원소와 바꾸면 된다
# 정렬 후 바꾸면 끄읏
# 문제 조건에 N이 100,000이하로 제한되어 있으니 이 때는
# 시간 복잡도가 O(NlogN)을 보장하는 알고리즘을 사용해야 한다!

n, k = map(int, input().split())


A = list(map(int, input().split()))

B = list(map(int, input().split()))


A.sort()
B.sort(reverse = True)

for i in range(k):
    #그냥 스왑하면 안되지! A의 값이 더 작은지 확인하고 바꿔야지!
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        #아니면 그 뒤의 반복문에서도 A가 더 클테니 반복이 무의미
        break

print(sum(A))
