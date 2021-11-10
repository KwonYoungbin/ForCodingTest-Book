def solution(N, stages):
    result = {}
    remain = len(stages)

    for i in range(1, N + 1):
        if remain != 0:
            count = stages.count(i)
            result[i] = count / remain
            remain -= count
        else:
            result[i] = 0

    return sorted(result, key=lambda x: result[x], reverse=True)


# from collections import Counter
#
# def solution(N, stages):
#     dic = {}
#     remain = len(stages)
#     counter = Counter(stages)
#
#     for i in range(1, N + 1):
#         if remain != 0:
#             now = counter[i]
#             dic[i] = now / remain
#             remain -= now
#         else:
#             dic[i] = 0
#
#     return sorted(dic, key=lambda x: dic[x], reverse=True)


# def solution(N, stages):
#     dic = {}
#     remain = len(stages)

#     for i in range(1, N+1):
#         if remain != 0:
#             now = stages.count(i)
#             dic[i] = now / remain
#             remain -= stages.count(i)
#         else:
#             dic[i] = 0

#     return sorted(dic, key=lambda x:dic[x], reverse=True)