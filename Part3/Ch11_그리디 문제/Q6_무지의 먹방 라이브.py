import heapq

# heap을 사용하는 원리는 잘 이해했으나, 세부적으로 알고리즘을 생각하는 것이 어려웠음.
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for x, y in enumerate(food_times):
        heapq.heappush(q, (y, x + 1))

    food_count = len(food_times)
    prev = 0
    while True:
        num, idx = heapq.heappop(q)
        if (num - prev) * food_count <= k:
            k -= ((num - prev) * food_count)
            food_count -= 1
            prev = num
        else:
            heapq.heappush(q, (num, idx))
            break
    q = sorted(q, key=lambda x: x[1])
    return q[k % food_count][1]