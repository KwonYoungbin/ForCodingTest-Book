import sys

n = int(sys.stdin.readline())
dic = {}

for _ in range(n):
    name, score = sys.stdin.readline().split()
    dic[name] = int(score)

print(*sorted(dic, key=lambda x:dic[x]), sep=' ')
