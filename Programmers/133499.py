def solution(babbling):
    answer = 0
    speak_word = ['aya', 'ye','woo','ma']
    
    count = 0
    for word in babbling:
        pre_speak_word = '' # 연속 된 단어를 방지 하기 위함
        target_word = "" # 현재 말하는 단어를 저장
        
        for alpha in word:
            target_word += alpha
            
            if target_word in speak_word: # target_word가 speak_word에 있는지?
                if pre_speak_word == target_word: # 이전에 말한 단어랑 같은지 ?
                    break # count 할 수 없음 !
                    
                else: # 다르다면 target_word를 초기화 
                    pre_speak_word = target_word
                    target_word = ''
    
        if target_word == '':
            answer += 1
                
                
    return answer