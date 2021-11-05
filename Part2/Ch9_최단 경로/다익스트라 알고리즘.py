#-------------------- 구현은 간단하지만, 동작 속도 느린 Ver. -------------------- 시간복잡도 O(V**2) / V:노드의 개수
# n : 노드의 개수 / m : 간선의 개수
# import sys
#
# n, m = map(int,sys.stdin.readline().split())
# INF = int(1e9)
#
# # 시작 노드
# start = int(sys.stdin.readline())
#
# # 각 노드와 연결된 노드에 대한 정보를 위한 리스트
# graph = [[] for _ in range(n+1)]
#
# # 방문 여부 확인 리스트
# visited = [False] * (n+1)
#
# # 최단 거리 테이블 초기화
# distance = [INF] * (n+1)
#
# # 간선 정보 입력 받기
# for _ in range(m):
#     a, b, c = map(int, sys.stdin.readline().split())    # a -> b 의 비용이 c
#     graph[a].append((b, c))
#
# # 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드 반환
# def get_smallest_node():
#     min_val = INF
#     idx = 0
#     for i in range(1, n+1):
#         if distance[i] < min_val and not visited[i]:
#             min_val = distance[i]
#             idx = i
#     return idx
#
# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     # 시작 노드와 직접 연결된 노드들의 거리 입력
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#
#     # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             distance[j[0]] = min(distance[j[0]], cost)
#
# dijkstra(start)
#
# print(*distance, sep='\n')
#--------------------------------------------------------------------------

#------------------------- 개선된 다익스트라 알고리즘 -------------------------- 시간복잡도 O(ElogV) / E:간선의 개수, V:노드의 개수
import heapq
import sys

n, m = map(int,sys.stdin.readline().split())
INF = int(1e9)

# 시작 노드
start = int(sys.stdin.readline())

# 각 노드와 연결된 노드에 대한 정보를 위한 리스트
graph = [[] for _ in range(n+1)]

# 최단 거리 테이블 초기화
distance = [INF] * (n+1)

# 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())    # a -> b 의 비용이 c
    graph[a].append((b, c))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)

print(*distance, sep='\n')