'''
Queue는 First In First Out (FIFO) 순서를 따르는 선형 구조이다.
먼저 삽입된 항목이 첫번째 항목이 된다.

Queue의 표준 작업
1. enqueue: Queue의 뒤쪽에서 (오른쪽) 요소를 삽입합니다.
2. dequeue: Queue의 앞쪽에서 (왼쪽) 요소를 제거하고 반환합니다.
3. peek: Queue의 맨 앞에 있는 요소를 제거하지 않고 반환합니다.
4. isEmpty: Queue가 비어있는지 확인합니다.
5. isFull : Qeueu가 가득 찼는지 확인합니다.
6. size: Queue에 있는 요소의 총 수를 반환합니다.
'''

class Queue:

    def __init__(self,size):
        self.q = [None] * size
        self.capacity = size
        self.front = 0
        self.tail = -1
        self.count = 0


    def enqueue(self, value):
        if self.isFull():
            print("The Queue is Full ! Calling exit()")
            exit()

        self.tail  = (self.tail + 1) % self.capacity
        self.q[self.tail] = value
        self.count += 1

    
    def dequeue(self):
        if self.isEmpty():
            print("The Queue is empty! Calling exit()")
            exit()
        
        data = self.q[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return data

    def peek(self):
        if self.isEmpty():
            print("The Queue is Empty! Calling exit()")
            exit(-1)

        return self.q[self.front]

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity

    def size(self):
        return self.count


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
self.tail이랑 self.front에서 +1을 해주고 capacity로 나눈 나머지로 더해주는 이유
FIFO 순서로 인해  

[1 None None] 일 때 
self.front의 index = 0
self.tail의 index = 0

요소 2추가

[1 2 None]
self.front 의 index = 0
self.tail의 index = 1

요소 3 추가
[1 2 3]
self.front의 index = 0
self.tail의 index = 2

만약에 front로 요소를 다 빼게 된다면
[None 2 3]
self.front index = 1
self.tail index = 2

[None None 3]
self.front index = 2
self.tail index = 2

[None None None]
self.front index = 3 % (self.capacity ==3) 이러면 나머지가 0이 되니 나중에 pop시 0번 인덱스부터
다시 빼올 수 있따 !

'''