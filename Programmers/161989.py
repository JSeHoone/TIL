# def solution(n, m, section):
#     answer = 0
#     width = ((max(section) - min(section))+1)
    
#     if width <= m:
#         answer += 1
    
#     elif (width % m) == 0:
#         answer += width // m
        
#     else:
#         answer += width // m
#         answer += 1
    
#     return answer

def solution(n, m, section):
    answer = 1 # 칠하는 횟수
    paint = section[0] # 덧칠 시작점
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]
            
    return answer