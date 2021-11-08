# 방법을 더 생각해보면 효율적인 방법을 떠올려 볼 수 있을 것 같음.

def rotate90(arr):
    return [row[::-1] for row in zip(*arr)]

def check_center(arr):
    start = len(arr) // 3
    for i in range(start, start * 2):
        for j in range(start, start * 2):
            if arr[i][j] != 1:
                return False
    return True

def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    expand_map = [[0] * (n * 3) for _ in range(n * 3)]

    # 자물쇠 확장(3배) 후 가운데 셋팅
    for row in range(n):
        for col in range(n):
            expand_map[row + n][col + n] = lock[row][col]

    for _ in range(4):
        key = rotate90(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        expand_map[x + i][y + j] += key[i][j]
                if check_center(expand_map):
                    return True
                for i in range(m):
                    for j in range(m):
                        expand_map[x + i][y + j] -= key[i][j]

    return answer