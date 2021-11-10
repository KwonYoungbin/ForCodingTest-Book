import sys

n = int(sys.stdin.readline())
datas = [list(sys.stdin.readline().split()) for _ in range(n)]
datas = sorted(datas, key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for data in datas:
    print(data[0])
