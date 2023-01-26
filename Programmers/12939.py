def solution(s):
    
    list_ = list(map(int, s.split()))
    answer = str(min(list_)) + ' ' + str(max(list_))
    
    return answer