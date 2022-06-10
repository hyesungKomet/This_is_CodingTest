#BFS(Breadth First Search): 너비 우선 탐색
# 큐 자료구조에 기초하여 구현
# deque 라이브러리 사용하기
# 시간복잡도는 O(N)이며, 일반적으로 실제 수행 시간은 DFS보다 좋은 편!
# -> DFS는 컴퓨터 시스템의 동작 특성상 실제 프로그램 수행 시간이 느려질 수 있기 때문\

# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리한다
# 2. 큐에서 노드를 꺼내고 해당 노드의 인접노드 중 방문하지 않은 노드를 모두 큐에 삽입한다
# 3. 더 이상 수행할 수 없을 때까지 2번을 반복한다

#deque 라이브러리 사용
from collections import deque

#BFS method 정의
def bfs(graph, start, visited):
    queue = deque([start])
    #현재 노드 방문처리  
    visited[start] = 1
    #큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나 dequeue해서 출력
        v = queue.popleft()
        print(v, end=' ')
        #해당 원소의 인접노드 중 방문하지 않은 노드 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)
