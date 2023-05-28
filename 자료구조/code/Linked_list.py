## Pytho으로 링크드리스트 구현하기
# Reference : 패스트캠퍼스 강의 (개발자 취업 합격 패스 With 코딩테스트, 기술면접 초격차 패키지 Online.)

'''
링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조

링크드 리스트 기본 구조와 용어
- Node : 데이터 저장 단위 (데이터값, 포인터)로 구성
- Pinter : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간


Python에서는 list가 링크드 리스트의 기능을 모두 지원한다.
'''


## 간단한 링크드 리스트 예

# 1. Node 구현
from re import search


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# Node 와 Node 연결하기 (Pointer 활용)

node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1
# head노드는 node1이 되고 node1이랑 연결 되어 있는 node가 node2 가 된다.



# 2. 링크드 리스트로 데이터 추가하기
class Node:
    def __init__(self,data, next= None):
        self.data = data
        self.next = next

def add(data):
    node = head # 전역변수에 있는 head를 node로 설정 (맨 앞에 있는 데이터)
    while node.next: # node.next 가 None이 되면 해당 while문은 벗어남
        node = node.next # node.next가 None이 아니라면 node는 head가 아닌 node.next가 된다
    node.next = Node(data) # node.next 에 data를 넣어준다.

node1 = Node(1)
head = node1
for index in range(2,10):
    add(index) # 2부터 9까지의 데이터가 연결되어 진다. 
print(node1.data) # 맨 처음 데이터 (head)
print(node1.next.data) # head 데이터랑 연결된 2번 데이터
print(node1.next.next.data) # 2번 데이터랑 연결된 데이터


## 링크드 리스트의 장단점 
'''
장점
1 . 미리 데이터 공간을 할당하지 않아도 된다.

단점
1. 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
2. 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림
3. 중간 데이터 삭제시, 앞 뒤 데이터의 연결을 재구성해야 하는 부가적인 작업 필요
'''

# 3. 링크드 리스트의 복잡한 기능 1 ( 데이터 사이에 데이터 추가)

# 데이터 Serch
node = head
while node.next:
    print(node.data) # 마지막 노드 전까지 출력
    node = node.next
print(node.data) # 마지막 노트의 data 출력

# 새로운 데이터를 데이터 사이에 넣기 (1과 2사이)
node3  = Node(1.5) # 1과 2사이에 있는 데이터 값

node = head
serch = True
while search: # 1과 2사이를 찾기 위해서 node.data값이 1인 node를 찾기 위해 serch
    if node.data == 1:
        serch = False
    else:
        node = node.next
    
node_next = node.next # 기존에 연결 되어 있던 데이터 값은 새로운 값을 연결하고 다시 연결해줘야 하기 떄문에
node_next = node3 # node.data ==1 인 node의 node.next를 node3으로 연결
node3.next = node_next # node3.next를 기존에 연결되어있던 next로 연결



## 파이썬 OOP로 링크드 리스트 구현하기

class Node():
    def __init__(self,data, next = node):
        self.data = data
        self.next = next


class NodeMgmt:
    # 초기 node를 성정하기 위한 __init__ 함수
    def __init__(self,data):
        self.head = Node(data)

    # data 를 추가 하기 위한 함수
    def add(self,data):
        if self.head == '': # 만약에 head가 비어있다면
            self.head(data) # 추가해준 데이터로 head를 채우기
        else:
            node = self.head # head가 있다면 해당 data를 node로 세우고
            while node.next: # 해당 Node에 next가 있다면
                node = node.next # Node는 node.next로 node를 설정해준다. 
            node.next = Node(data) # 새로 들어온 데이터로 node.next를 채워준다

    # 링크드 리스트의 연결을 출력해주는 함수
    def dsec(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # 응용2. 특정 노드를 삭제하는 방법
    def delete(self,data):
        if self.head == '':
            print('해당 값을 가진 노드가 없습니다')
        
        if self.head.data == data: # 삭제하려는 데이터가 같다면
            temp = self.head # 해당 값을 temp에 저장해주고
            self.head = self.head.next # head를 head의 next값으로 지정해준다.
            del temp # 이후 해당 node를 삭제해준다

        else: # 삭제하려는 값이랑 다를 때 (찾아줘야한다)
            node = self.head # self.head의 값을 node에 저장
            while node.next: # 마지막 노드의 next 는 None이니까 
                if node.next.data == data: # node의 next 데이터가 삭제하려는 데이터라면
                    temp = node.next # 해당(node의 next node) node를 저장하고
                    node.next = node.next.next # 그 다음 next node를 현재 node의 next node로 지정
                    del temp # 노드 삭제
                    return 
                else:
                    node = node.next # 그렇지 않으면 다음 노드로 node를 변경


