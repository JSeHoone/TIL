## 10814
import sys

T = int(sys.stdin.readline())

list_ = []
for index, _ in enumerate(range(T)):
    data = [index]
    data.extend(list(sys.stdin.readline().split()))
    list_.append(data)

a = sorted(list_, key = lambda x : int(x[1]) )
for i in a:
    print(f"{i[1]} {i[2]}")