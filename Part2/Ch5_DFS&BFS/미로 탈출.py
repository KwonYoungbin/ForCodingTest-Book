import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

moves = [(-1,0), (0,1), (1,0), (0,-1)]
dq = deque([(0,0)])

# BFS 사용하는 방법, 100% 이해하지는 못함.
while dq:
    a, b = dq.popleft()
    for move in moves:
        x = a + move[0]
        y = b + move[1]

        if x < 0 or x >= n or y < 0 or y >= m:
            continue

        if map[x][y] == 1:
            map[x][y] = map[a][b] + 1
            dq.append((x,y))

print(map[-1][-1])