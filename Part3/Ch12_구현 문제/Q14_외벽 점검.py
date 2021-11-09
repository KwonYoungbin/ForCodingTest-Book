from itertools import permutations

# 아직 이해 못함, 미완성 미구현 상태.
def solution(n, weak, dist):
    answer = len(dist) + 1
    origin_length = len(weak)

    for i in range(len(weak)):
        weak.append(weak[i] + n)

    for i in range(origin_length):
        for per in list(permutations(dist, len(dist))):
            count = 1
            max_pos = weak[i] + per[count - 1]
            for idx in range(i, i + origin_length):
                if max_pos < weak[idx]:
                    count += 1
                    if count >= len(dist):
                        break
                    max_pos = weak[idx] + per[count - 1]
            answer = min(answer, count)

    return answer if answer <= len(dist) else -1