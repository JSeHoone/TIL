## 색종이
import sys

# T = int(sys.stdin.readline())
T = 3

paper = [[0]*101 for i in range(101)]

for _ in range(T):
    # a,b = map(int,sys.stdin.readline().split())
    a,b = map(int,input().split())
    for i in range(10):
        for j in range(10):
            paper[a+i][b+i] = 1


answer = 0
for x in paper:
    answer += sum(x)
print(answer)