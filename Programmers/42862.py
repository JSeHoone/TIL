## 체육복 문제
def solution(n, lost, reserve):
    lost.sort() # 정렬해서 최대한 많은 옷 찾기
    a = set(lost) & set(reserve)
    
    for i in a:
        reserve.remove(i)
        lost.remove(i)

    for sweatsuit in lost:
        if sweatsuit in reserve:
            reserve.remove(sweatsuit)
        elif ((sweatsuit - 1) in reserve) :
            reserve.remove((sweatsuit - 1))
        elif ((sweatsuit + 1) in reserve) :
            reserve.remove((sweatsuit + 1))
            
        else:
            n -= 1
            
    return n