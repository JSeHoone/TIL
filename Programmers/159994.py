# 카드 뭉치
def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    for word in goal:

        if (len(cards2) == 0) & (len(cards1) != 0): # cards2번 리스트가 빈값이 된 경우
            if word == cards1[0]:
                del cards1[0]
            else:
                answer = 'No'
                break
        elif (len(cards1) == 0) & (len(cards2) != 0): # cards1번 리스트가 빈 값이 된 경우
            if word == cards2[0]:
                del cards2[0]
            else:
                answer = 'No'
                break
        else: # 모든 카드 뭉치에 word가 있는 경우
            if word == cards1[0]:
                del cards1[0]
            elif word == cards2[0]:
                del cards2[0]
            else:
                break
        
    return answer 


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print("="*100)
print(solution(["i", "water", "drink"] , ["want", "to"],["i", "want", "to", "drink", "water"] ))
