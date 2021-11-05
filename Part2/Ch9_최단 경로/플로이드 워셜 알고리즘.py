import sys

n, m = map(int,sys.stdin.readline().split())
INF = int(1e9)

# 무한의 값을 갖는 2차원 리스트 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# i = j 인 위치의 값을 0으로 초기화
for i in range(1,n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0

# 입력받은 간선 정보 추가
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())    # a -> b로 가는 비용 c
    graph[a][b] = c

# 플로이드 워셜 알고리즘 적용
for x in range(1, n+1):
    for y in range(1, n+1):
        for z in range(1, n+1):
            graph[y][z] = min(graph[y][z], graph[y][x]+graph[x][z])     # 점화식

for i in range(n+1):
    print(graph[i], end='\n')