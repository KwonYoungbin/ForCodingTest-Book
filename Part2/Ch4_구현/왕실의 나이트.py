import sys

pos = list(sys.stdin.readline().rstrip())
row = ['1','2','3','4','5','6','7','8']
col = ['a','b','c','d','e','f','g','h']
result = 0

moves = [(-2,-1), (-2,1), (-1,-2), (1,-2), (2,-1), (2,1), (-1,2), (1,2)]

for move in moves:
    if 0 <= row.index(pos[1])-move[0] <= 7 and 0 <= col.index(pos[0])-move[1] <= 7:
        result += 1
print(result)