import sys
# 구현 미완료 상태. 추가 해야 함
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
board = [[-1]*(n+2) for _ in range(n+2)]

apples = [tuple(map(int,sys.stdin.readline().split())) for _ in range(k)]
l = int(sys.stdin.readline())
moves = [tuple(sys.stdin.readline().split()) for _ in range(l)]
result = 0

direction = [(0,1),(1,0),(0,-1),(-1,0)]
start_dir = 0
head = (1,1)

# 맵과 벽 지정
for i in range(1, n+1):
    for j in range(1, n+1):
        board[i][j] = 0
board[1][1] = 1
