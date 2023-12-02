def solution(dartResult):
    
    score_list = []
    # 10을 구별하기 위한 변수
    num = ''
    for dart in dartResult:
        # 점수 데이터 넣기 
        if (num != '') and (not dart.isdigit()):
            score_list.append(int(num))
            num = ''
            
        # 점수 데이터 뽑기
        if dart.isdigit():
            num += dart
            
        # S, D, T 구분하여 점수 추가
        elif dart in ['S','D','T']:
            if dart == 'D':
                score_list[-1] = score_list[-1] ** 2
            elif dart == 'T':
                score_list[-1] = score_list[-1] ** 3
        # 옵션에 따른 점수 부여
        elif dart in ['*', '#']:
            if dart == '*':
                if len(score_list) == 1:
                    score_list[0] = score_list[0] * 2
                else:
                    for index in range(1,3):
                        score_list[-index] = score_list[-index] * 2
            elif dart == '#':
                score_list[-1] = score_list[-1] * -1
            
    return sum(score_list)

print(solution("1S2D*3T"))
print(solution("1D#2S*3S"))
print(solution("1D2S#10S"))
print(solution("1T2D3D#"))
