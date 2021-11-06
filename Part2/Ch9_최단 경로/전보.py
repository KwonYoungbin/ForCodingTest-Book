import sys
import heapq

# 문제를 이해하고 원리는 알겠으나, 직접 구현하는 것이 아직 어려움.

INF = int(1e9)

n, m, c = map(int, sys.stdin.readline().split())

distance = [INF] * (n+1)
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, start = map(int, sys.stdin.readline().split())
    graph[a].append((b,start))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
for d in distance:
    if d != INF and d != 0:
        count += 1

max_val = 0
for val in graph[c]:
    if max_val < val[1]:
        max_val = val[1]

print(count, max_val)