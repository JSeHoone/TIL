'''
Stack의 표준 작업
    push: Stack의 맨 위에 있는 항목을 푸시합니다.
    pop: Stack의 맨 위에서 항목을 제거하고 반환합니다.
    peek: Stack의 맨 위에 있는 항목을 제거하지 않고 반환합니다.
    size: Stack에 있는 총 항목 수를 반환합니다.
    isEmpty: Stack이 비어 있는지 확인합니다.
    isFull: Stack이 가득 찼는지 확인합니다.
'''


class Stack:

    def __init__(self,size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1
        
    def push(self,value):
        if self.isFull():
            print("The Stack is Full Calling exit()")
            exit(-1)
        
        self.top += 1
        self.arr[self.top] = value

    def pop(self):
        if self.isEmpty():
            print("The stack is empty Calling exit()")
            exit(-1)

        data = self.arr[self.top]
        self.top -= 1
        return data

    def peek(self):
        if self.isEmpty():
            print("The stack is empty Calling exit()")
            exit(-1)

        return self.arr[self.top]

    def size(self):
        return self.top +1

    def isEmpty(self):
        return self.size() == 0
    
    def isFull(self):
        return self.top == self.capacity


if __name__ == '__main__':
    stack = Stack(3)

    stack.push(1) # Stack에 int 1 삽입
    stack.push(2) # Stack에 int 2 삽입

    stack.pop() # Stack 상단 요소 제거 (2)
    stack.pop() # Stack 상단 요소 제거 (1)

    stack.push(3) # Stack에 int 3 삽입

    print(f"Top element is {stack.peek()}")
    print(f"The stack size is {stack.size()}")

    stack.pop() # Stack 상단 요소를 제거함으로 빈공간 만들기

    # Stack이 비어있는지 확인
    if stack.isEmpty():
        print("The stack is empty")
    else:
        print('The stack is not empty')