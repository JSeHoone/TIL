def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(x ** 0.5) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아니다.
    return True
    

def solution(n):
    answer = 0
    for num in range(2,n+1):
        if is_prime_number(num):
            answer += 1
    return answer

print(solution(10))