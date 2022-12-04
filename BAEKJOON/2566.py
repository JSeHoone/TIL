import sys

max_row = 0
max_col = 0

max_num = 0
for row in range(9):
    list_ = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    if max_num <= max(list_):
        max_num = max(list_)
        max_row = row
        max_col = list_.index(max(list_))
        
print(max_num)
print(max_row+1, max_col+1)