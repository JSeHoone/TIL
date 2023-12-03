def solution(lottos, win_nums):
    
    zero_count = 0
    answer_count = 0
    for mine in lottos:
        if mine == 0:
            zero_count += 1
        else:
            if mine in win_nums:
                answer_count += 1
    max_min = [6 if (6 - (zero_count + answer_count) + 1) > 6 else (6 - (zero_count + answer_count) + 1), 
               6 if (6 - (answer_count) + 1) > 6 else (6 - (answer_count) + 1) ]
    
    
    
                
                
    return max_min