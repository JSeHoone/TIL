import sys

n,m = map(int, sys.stdin.readline().rstrip().split(' '))

A = []
for _ in range(n):
    a = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    A.append(a)

B = []
for _ in range(n):
    b = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    B.append(b)

for x,y in zip(A,B):
    i = ''
    for a,b in zip(x,y):
        i += str(a+b)+str(' ')
    print(i)