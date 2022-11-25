# 프로그래머스 Level_1 모의고사 (42840)
'''
수포자 1번: 1,2,3,4,5 순으로 찍는다.
수포자 2번: 2,1,2,3,2,4,2,5,2,1 순으로 찍는다.
수포자 3번: 3,3,1,1,2,2,4,4,5,5 순으로 찍는다.
가장 많이 맞춘 사람이 누군지 맞추자 !
'''
def solution(answers):
    result = []

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    for i, answer in enumerate(answers):
        if one[i%5] == answer:
            score[0] += 1
        if two[i%8] == answer:
            score[1] += 1
        if three[i%10] == answer:
            score[2] += 1

    for i in range(len(score)):
        if max(score) == score[i]:
            result.append(i+1)

    return result