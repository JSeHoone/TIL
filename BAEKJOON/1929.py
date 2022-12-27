## 3~ 16 사이의 소수 구하기 (정답은 3,5,7,11,13)

import sys
N,M = map(int, sys.stdin.readline().rstrip().split())

a = [False,False] + [True]*(M-1)

for i in range(2,int(M**.5)+1):
    if a[i]:
        for j in range(2*i, M+1, i):
            a[j] = False
            
primes = [i for i in range(N,M+1) if a[i] == True]
for i in primes:
    print(i)