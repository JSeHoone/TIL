## 베르트랑 공준

import sys
a = [True] * (2 * 123456 +1)
a[0] = False
a[1] = False

for i in range(2,int(len(a)**.5) ):
    if a[i]:
        for j in range(2*i , len(a)+1, i):
            a[j] = False

while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break
    else:
        print( sum(a[N+1 : (2*N+1)]) )