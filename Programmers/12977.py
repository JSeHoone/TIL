# 소수 만들기
## 주어진 리스트에서 3개의 숫자를 뽑아서 만들 수 있는 소수의 갯수 구하기

from itertools import combinations



# 소수 판별 함수 - 에라토스테네스의 체
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(x ** 0.5) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아니다.
    return True


def solution(nums):
    answer = 0
        
    # comb_sum = []
    for list_ in combinations(nums, 3):
        if is_prime_number( sum(list_) ) :
            answer += 1
    
    return answer

print(solution([1,2,7,6,4]))