# 수 정렬하기 2 

import sys

T = int(sys.stdin.readline())

list_ = []
for _ in range(T):
    list_.append(int(sys.stdin.readline()))

list_.sort()

for i in list_:
    print(i)