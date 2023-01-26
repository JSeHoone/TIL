## 1427
import sys
data = sys.stdin.readline().rstrip()
a = ""
for i in sorted(data, reverse = True):
    a += i
print(a)