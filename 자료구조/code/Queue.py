## Python으로 Queue 구현
# Reference site: https://www.techiedelight.com/ko/queue-implementation-python/
'''
Queue는 First In First Out (FIFO) 순서를 따르는 선형 구조이다.
먼저 삽입된 항목이 첫번째 항목이 된다.

Queue의 표준 작업
1. enqueue: Queue의 뒤쪽에서 (오른쪽) 요소를 삽입합니다.
2. dequeue: Queue의 앞쪽에서 (왼쪽) 요소를 제거하고 반환합니다.
3. peek: Queue의 맨 앞에 있는 요소를 제거하지 않고 반환합니다.
4. isEmpty: Queue가 비어있는지 확인합니다.
5. size: Queue에 있는 요소의 총 수를 반환합니다.
'''

## Stack을 공부한 이후로 Queue구현 하는 것을 보았다.
# 먼저 블로그 내 코드를 보지 않고 스스로 구현해보자 !
# 주석이 되어 있는 부분은 코드를 보고 추가한 부분이다.

class Queue:

    def __init__(self,size):
        self.capacity = size 
        self.arr = [None] * size
        self.front = 0 
        self.rear = -1 # 후면은 Queue의 마지막 요소를 카리킵니다. (내가 사용했을 떈 top을 사용)
        self.count = 0 # Queue의 현재 크기

        
    def enqueue(self,value):
        if self.size() == self.capacity: # isFull()과 동일한 코드임.
            print("The queue is Full !! Calling exit()..")
            exit()

        # self.top += 1
        # self.arr[self.top] = value
        self.rear = (self.rear + 1) % self.capacity # 여기도 왜 이런 코드를 사용햇을까?
        self.arr[self.rear] = value
        self.count += 1


    def dequeue(self):
        if self.isEmpty():
            print(f"The Queue is Empty!! Calling exit()..")
            exit(-1)

        
        data = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity ## 왜 이런 코드를 사용했을까?
        self.count -= 1
        return data
    
    def peek(self):
        if self.isEmpty():
            print(f"The Queue is Empty!! Calling exit()..")
            exit(-1)

        return self.arr[self.front]
    
    def isEmpty(self):
        return self.size() == 0
    
    ## isFull 함수가 추가 되어 있었음
    def isFull(self):
        return self.size() == self.capacity
    
    def size(self):
        return self.count # self.count를 만들어서 Queue의 크기를 반환하는 함수
    
if __name__ == '__main__':

    queue = Queue(3)

    queue.enqueue(1) # 1 넣기
    queue.enqueue(2) # 2 넣기

    print(queue.dequeue())  # 원소 하나 빼기
    print(queue.dequeue()) # 원소 하나 빼기

    print(queue.size())
 
    queue.enqueue(3) # 원소 3 넣기
    print(queue.peek())
    print(queue.arr)
    print(queue.front, queue.rear, queue.count)


'''
구현의 차이점
1. self.count를 사용하지 않았다는 점
2. self.front 와 self.rear(self.top)을 단순히 더하지 않고 나머지로 계산한 점
'''