## 실패율
# 실패율 계산 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

def solution(N, stages):
    

    stage_dict = dict()
    for stage in range(1,N+1):
        not_clear = stages.count(stage) # yet, stage clear
        current_user = 0
        for i in stages:
            if i >= stage:
                current_user += 1
        
        if not_clear == 0:
            stage_dict[stage] = 0
        else:
            stage_dict[stage] = not_clear / current_user

    data = sorted( stage_dict, reverse=True, key= lambda x : stage_dict[x])
    
    return data

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))