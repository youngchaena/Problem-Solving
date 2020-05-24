# hash 문제
# dictionary를 활용해서 cnt가능
# 각 카테고리별 cnt + 1(미착용)의 곱 - 1 (아무것도 미착용)

def solution(clothes):
    cats = {}
    for _, cat in clothes:
        if cat in cats:
            cats[cat] += 1
        else:
            cats[cat] = 1
    comb = 1
    for n in cats.values():
        comb *= (n + 1)
    return comb - 1