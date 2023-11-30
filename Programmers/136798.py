def solution(number, limit, power):
    answer = 0
    
    for knight in range(1,number+1):
        count = 0
        for i in range(1, int(knight**0.5)+1):
            if knight % i == 0:
                count += 1
                if ((i**2) != knight) :
                    count += 1
        
        if count > limit:
            answer += power 
        else:
            answer += count 
            
    return answer