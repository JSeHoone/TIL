### 금과은 운반하기 >> parametric serch 공부하고 다시 접근해보기

# def solution(a, b, g, s, w, t):
#     answer = -1
#     city_list = {}
    
#     # create city_info
#     for index,(gold,silver,weight,time) in enumerate(zip(g,s,w,t)):
#         city_list[f"{index}"] = [gold,silver,weight,time]
    
#     # 도시가 하나인 경우
#     if len(city_list) == 1:
#         # remain weight
#         remain_w = (a%city_list["0"][2]) + (b%city_list["0"][2])
#         loop_cnt = ((a // city_list["0"][2]) + (b // city_list["0"][2])) * 2
#         # print(loop_cnt, remain_w)
        
#         if remain_w <= city_list["0"][2]:
#             loop_cnt += 1
#         elif (remain_w % city_list["0"][2]) != 0:
#             loop_cnt += ((remain_w // city_list["0"][2]) + 1) + 1

#         answer = loop_cnt * city_list["0"][-1]
    
#     # 도시가 2개 이상인 경우
#     else:
#         # gold 운반이 가능한 도시 찾기
#         gold_possible_city = [i for i in range(len(city_list)) if (city_list[f"{i}"][0] != 0) ]
#         print(gold_possible_city)
#         # 무게 배분하기
#         # 트럭이 옮길 수 있는 무게에 따라서 다르게 배분해야 하나?




#     return answer

# print(solution(10,10,[100],[100],[7],[10]))
# print(solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]))