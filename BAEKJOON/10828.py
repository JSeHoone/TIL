import sys

list_ = []
for _ in range(int(sys.stdin.readline())):
    list2 = sys.stdin.readline().rstrip().split(' ')
    action = list2[0]

    if action == 'push':
        list_.append(int(list2[1]))
    elif action == 'pop':
        if len(list_) == 0:
            print(-1)
        else:
            print(list_.pop())
    elif action == 'size':
        print(len(list_))
    elif action == 'empty':
        if len(list_) == 0:
            print(1)
        else:
            print(0)
    elif action == 'top':
        if len(list_) == 0:
            print(-1)
        else:
            print(list_[-1])