import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
moves = [[] for _ in range(n+1)]
result = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    moves[a].append(b)

distance = [0] * (n+1)
q = deque([x])

while q:
    now = q.popleft()
    for node in moves[now]:
        if distance[node] == 0:
            distance[node] = distance[now] + 1
            q.append(node)

if k not in distance:
    print(-1)
else:
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)