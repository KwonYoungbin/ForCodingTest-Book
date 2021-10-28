import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)

#가장 큰 수 k번 + 두번째 큰 수 1번 이 반복되는 패턴
result = ((arr[0]*k + arr[1]) * m // (k+1)) + arr[0] * (m%(k+1))

print(result)