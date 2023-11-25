# 2016년 
## 2016년 1월 1일은 금요일이다 . (윤달)

def solution(a, b):
    answer = ''
    
    ## 목 - 금 - 토 - 일 - 월 - 화 - 수 (순서로 설정함) => index 1번이 1월 1일로 설정 하려고
    day_of_week = ['THU','FRI','SAT','SUN','MON','TUE','WED']

    day_dict = {
        '31' : [1,3,5,7,8,10,12],
        '29' : [2],
        '30' : [4,6,9,11]
    }

    total_day = 0

    for month in range(1,a):
        if month in day_dict['31']:
            total_day +=  (31)
        elif month in day_dict['30']:
            total_day += (30)
        else:
            total_day += (29)
    print(total_day, (total_day+b) % 7)

    answer = day_of_week[(total_day+b) % 7]


    return answer


print(solution(5,24))
# print(solution(1,2))