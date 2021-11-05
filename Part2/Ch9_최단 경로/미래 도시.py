import sys

# N의 범위가 좁기 때문에 플로이드 워셜 알고리즘 사용
INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())
arr = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            arr[i][j] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

x, k = map(int, sys.stdin.readline().split())

for w in range(1, n+1):
    for y in range(1, n+1):
        for z in range(1, n+1):
            arr[y][z] = min(arr[y][z], arr[y][w]+arr[w][z])

print(arr)
print(arr[1][k]+arr[k][x]) if arr[1][k] != INF and arr[k][x] != INF else print(-1)