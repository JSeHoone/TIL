## 베르트랑 공준
# 틀린 답 ㅠ.ㅠ

import sys
a = [True] * (2 * 123456 +1)
a[0] = False
a[1] = False

for i in range(2,int(len(a)**.5)+1 ):
    if a[i]:
        for j in range(2*i , len(a)+1, i):
            a[j] = False

while True:
    N = int(sys.stdin.readline())
    M = N *2

    if N == 0:
        break
    primes = [i for i in range(N,M+1) if a[i] == True]
    print( len(primes) )