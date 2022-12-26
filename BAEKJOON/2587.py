import sys

list_ = list(map(int, sys.stdin.readlines()))

print(sum(list_) // len(list_))
print(sorted(list_)[2])