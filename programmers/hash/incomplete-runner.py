# 완주하지 못한 선수

# dictionary를 활용한 풀이
def solution(participant, completion):
    bucket = {}
    for p in participant:
        if p in bucket:
            bucket[p] += 1
        else:
            bucket[p] = 1
    for c in completion:
        if bucket[c] == 1:
            del(bucket[c])
        else:
            bucket[c] -= 1
    answer = list(bucket.keys())[0]

    return answer

# sorting을 활용한 풀이
def solution(participant, completion):
    bucket = {}
    for p in participant:
        if p in bucket:
            bucket[p] += + 1
        else:
            bucket[p] = 1
    for c in completion:
        if bucket[c] == 1:
            del(bucket[c])
        else:
            bucket[c] -= - 1
    answer = list(bucket.keys())[0]
        
    return answer

# collections.Counter를 활용한 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]