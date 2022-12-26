import sys

a = list(map(int,sys.stdin.readline().rstrip().split()))
b = list(map(int,sys.stdin.readline().rstrip().split()))
b.sort(reverse = True)

print(b[a[1]-1])