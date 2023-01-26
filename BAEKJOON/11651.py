## 11651 
import sys
T = int(sys.stdin.readline())

list_ = []
for _ in range(T):
    data = list(map(int, sys.stdin.readline().split()))
    list_.append(data)

a = sorted(list_ , key = lambda x : (x[1], x[0]) )

for x,y in a:
    print(f"{x} {y}")