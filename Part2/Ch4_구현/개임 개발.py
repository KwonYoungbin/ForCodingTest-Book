import sys

n, m = map(int, sys.stdin.readline().split())
character = list(map(int, sys.stdin.readline().split()))
map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
map[character[0]][character[1]] = 2
direction = character[2]

moves = [(0,-1), (1,0), (0,1), (-1,0)]
result = 1

startDir = direction

while True:
    direction = (direction + 3) % 4

    if map[character[0]+moves[direction][0]][character[1]+moves[direction][1]] == 0:
        map[character[0]+moves[direction][0]][character[1]+moves[direction][1]] = 2
        character[0] += moves[direction][0]
        character[1] += moves[direction][1]
        result += 1
        startDir = direction
    else:
        if startDir == direction:
            if map[character[0] - moves[direction][0]][character[1] - moves[direction][1]] == 1:
                break
            else:
                map[character[0]][character[1]] = 1
                character[0] -= moves[direction][0]
                character[1] -= moves[direction][1]
                direction += 1
print(result)