import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
# 0 값을 갖는 한 좌표와 인접한 모든 0 값을 1로 만들기 때문에, 인접한 다른 노드들에 대해서는 False값을 가짐.
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result += 1

print(result)