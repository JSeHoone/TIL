## 과일 장수
# 예를 들어, k = 3, m = 4, 사과 7개의 점수가 [1, 2, 3, 1, 2, 3, 1]이라면,
# 다음과 같이 [2, 3, 2, 3]으로 구성된 사과 상자 1개를 만들어 판매하여 최대 이익을 얻을 수 있습니다.

## 이익 계산식 : (최저 사과 점수) x (한 상자에 담긴 사과 개수) x (상자의 개수) = 2 x 4 x 1 = 8

def solution(k, m, score):
    answer = 0
    # 만들 수 있는 상자의 수 계산 
    max_box = len(score) // m

    # 정렬해서 m만큼 나눠주면 되지 않을까?
    score.sort(reverse = True)

    s_idx = 0
    for _ in range(max_box):
        # 최대이익 계산식 넣음
        cal_score = min(score[s_idx:s_idx + m]) * m
        # 더해줌
        answer += cal_score
        # slicing하기 위해서 시작 index를 지정해줌
        s_idx += m
    
    return answer

print(solution(3,4,[1,2,3,1,2,3,]))
print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))

