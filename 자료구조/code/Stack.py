## Python으로 Stack 구현
# Reference site : https://www.techiedelight.com/ko/stack-implementation-python/
"""
Stack은 Last in First Out(LIFO) 순서를 따르는 선형 데이터 구조이다.
한 쪽 끝에서만 삽입되거나 제거 될 수 있다 !

Stack의 표준 작업
    push: Stack의 맨 위에 있는 항목을 푸시합니다.
    pop: Stack의 맨 위에서 항목을 제거하고 반환합니다.
    peek: Stack의 맨 위에 있는 항목을 제거하지 않고 반환합니다.
    size: Stack에 있는 총 항목 수를 반환합니다.
    isEmpty: Stack이 비어 있는지 확인합니다.
    isFull: Stack이 가득 찼는지 확인합니다.
"""

# List를 사용한 Stack 구현

class Stack:

    # Stack을 초기화하는 생성자
    def __init__(self, size :int ):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1

    # Stack에 'val' 요소를 추가하는 함수
    def push(self, val):
        if self.isFull():
            print('Stack OverFlow!! Calling exit()')
            exit(-1)
        
        print(f"Inserting {val} into the Stack...")
        self.top = self.top + 1
        self.arr[self.top] = val

    # Stack에서 최상위 요소를 pop하는 함수
    def pop(self):
        # Stack의 UnderFlow 검사
        if self.isEmpty():
            print('Stack Underflow!! Calling exit()...')
            exit(-1)

        print(f"Removing {self.peek()} from the stack")
        top =self.arr[self.top]
        self.top = self.top -1
        return top
    
    # Stack의 최상위 요소를 반환하는 함수
    def peek(self):
        if self.isEmpty():
            exit(-1)
        
        return self.arr[self.top]
    
    # Stack의 크기를 반환하는 함수
    def size(self):
        return self.top + 1
    
    # Stack이 비어있는지 확인하는 함수
    def isEmpty(self):
        return self.size() == 0
    
    # Stack이 가득 찼는지 확인하는 함수
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


## Python 에서는 collections라는 라이브러리 내 deque를 사용해서 구현도 가능하다 !
