## 골드바흐의 추측

## 내가 직접 짜본 코드 (시간 초과가 난다 ! ..)
import sys
T = int(sys.stdin.readline())


a = [False,False] + [True] * (10000-1)
for i in range(2, int(10000**0.5)+1):
    if a[i]:
        for j in range(2*i, 10000+1, i):
            a[j] = False

for _ in range(T):
    n = int(sys.stdin.readline())

    primes = [x for x in range(n) if a[x] == True]
    

    list_ = []
    for index,one in enumerate(primes):
        for two in primes:
            if one + two == n:
                list_.append([one,two])
                

    list_.sort()

    other_list = []
    best_= -99999
    index_ = 0
    for index, (c,d) in enumerate(list_):
        if c-d > best_ and c-d <= 0:
            index_ = index

    print(f'{list_[index_][0]} {list_[index_][1]}')


## 찾아본 정답 
import sys
# T = int(sys.stdin.readline())
T = 3

## 제한을 미리 만들어 두면 속도가 좀 빨라질 것 같음! 
a = [False,False] + [True] * (10000)

for i in range(2, int(10000**0.5)+1):
    if a[i]:
        for j in range(2*i, 10000+1, i):
            a[j] = False

''' 여기 부분에서 복잡도를 개선한거 같은데 
먼저 input값의 중간으로 줘서 소수가 되더라도 차이가 최솟값이 되도록 줬다.
그 다음에 A는 빼는쪽으로 B는 더하는 쪽으로 줘서 시간 복잡도를 최소화 한 것 같다!.. (대단..)'''
for _ in range(T):
    n = int(sys.stdin.readline())

    A = n//2
    B = A
    for _ in range(10000):
        if a[A] and a[B]:
            print(A,B)
            break
        A -= 1
        B += 1