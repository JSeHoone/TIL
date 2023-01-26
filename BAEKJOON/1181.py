## 1181 -> 속도 3452
import sys

T = int(sys.stdin.readline())

list_ = []
for _ in range(T):
    data = sys.stdin.readline().rstrip()
    if data not in list_:
        list_.append(data)

a = sorted(list_, key = lambda x : (len(x) , x))
for i in a:
    print(i)


""" 속도 60인 코드
import sys

n = int(input())
string_set = set()
for _ in range(n):
    string_set.add(sys.stdin.readline().rstrip())
string_list = list(string_set)
string_list.sort()
string_list.sort(key=len)
print("\n".join(string_list))
"""