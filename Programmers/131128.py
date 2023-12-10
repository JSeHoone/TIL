## 숫자 짝꿍 
# 내가 시도한 코드 -- 시간 초과로 틀림
def solution(X, Y):
    answer = ''
    X = list(X)
    Y = list(Y)
    
    pair = []
    if len(X) <= len(Y):
        for num in X:
            if num in Y:
                pair.append(num)
                Y.remove(num)
    else:
        for num in Y:
            if num in X:
                pair.append(num)
                X.remove(num)
    
    if len(pair) == 0 :
        answer = '-1'
    else:
        pair.sort(reverse = True)
        for num in pair:
            answer += num
    
    return str(int(answer))

## 알아본 코드 - 대박
# def solution(X, Y):
#     answer = ''

#     for i in range(9,-1,-1) :
#         answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
#     if answer == '' :
#         return '-1'
#     elif len(answer) == answer.count('0'):
#         return '0'
#     else :
#         return answer
# 출처: https://chan-lab.tistory.com/36 [은공지능 공작소:티스토리]