import sys

n = int(sys.stdin.readline())
stuffs = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
items = list(map(int, sys.stdin.readline().split()))

# 방법 1. in 함수를 이용해서 풀기
# result = []
# for item in items:
#     if item in stuffs:
#         result.append('yes')
#     else:
#         result.append('no')
#
# print(' '.join(result))

# 방법 2. 계수 정렬을 이용해서 풀기
# chk = [0] * 1000001
# for num in stuffs:
#     chk[num] += 1
#
# for item in items:
#     if chk[item] == 0:
#         print('no', end=' ')
#     else:
#         print('yes', end=' ')

# 방법 3. 이진 탐색을 이용해서 풀기
def b_search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

stuffs.sort()

for item in items:
    print('yes', end=' ') if b_search(stuffs, item, 0, n-1) else print('no', end=' ')