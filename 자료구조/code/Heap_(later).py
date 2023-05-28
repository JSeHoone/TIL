## Python으로 heap 자료구조 구현하기
# Reference site: https://wikidocs.net/194445 (좌충우돌, 파이썬으로 자료구조 구현하기) code가 없당..
# New Reference site : https://ojt90902.tistory.com/572 


'''
들어가는 자료에 우선순위를 매겨서 들어간 순서와 관계없이 나갈 때는 
우선순위가 높은 자료가 먼저 나가는 자료 구조를 우선순위 큐(Pirority Queue)라고 한다.

힙(heap)은 우선순위 큐를 구현하기 위한 자료 구조다. 
Heap은 크게 배열, 링크드리스트, 트리로 구현할 수 있다. 
그렇지만 트리로 구현하는 것이 가장 좋은 것으로 알려져 있다. 

# 힙은 다음과 같은 규칙에 따라 구성한 이진 트리다.
규칙 1: 노드를 왼쪽에서 오른쪽으로 하나씩 빠짐없이 채워나간다. (Level 순서로 노드를 삽입한다.)
규칙 2: 최소 힙(MinHeap)은 부모 노드가 자식 노드의 값보다 작거나 같아야 한다. {파이썬의 heapq 모듈은 최소 힙(min heap)이다.}
    (최대 힙은 부모 노드가 자식 노드의 값보다 크거나 같다.)

'''

# 2번 Reference에 있던 코드를 Clone 해보쟝


class nheap(object):
    def __init__(self):
        self.hq = [0]

    def get_priority(self,node):
        if (len(self.hq) - 1) >= (node *2 + 1):
            if self.hq[node*2] > self.hq[self.node * 2 + 1]:
                return node * 2 + 1
            else:
                return node * 2

        elif len(self.hq) - 1 == node*2:
            return node * 2

        else:
            return -1

    def heappop(self):
        if len(self.hq) == 1:
            return 0

        return_value = self.hq[1]
        last_data = self.hq[-1]
        node = 1

        while 1:
            pri_node = self.get_priority(node)

            if pri_node == -1:
                break

            if last_data > self.hq[pri_node]:
                self.hq[node] = self.hq[pri_node]
                node = pri_node

            else:
                break

        self.hq[node] = last_data
        self.hq.pop()

        return return_value

    def heappush(self,value):
        self.hq.append(value)
        node = len(self.hq) - 1
        last_idx = node

        while node > 1:
            node //= 2

            if self.hq[node] > value:
                self.hq[last_idx] = self.hq[node]
                last_idx = node

            else:
                break

        self.hq[last_idx] = value
        # return 



## 음.. 아직 무슨 의미인지 잘 모르겠따 