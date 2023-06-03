## Python으로 Tree 구현하기
# Reference : 패스트캠퍼스 강의 (개발자 취업 합격 패스 With 코딩테스트, 기술면접 초격차 패키지 Online.)
'''
트리: Node와 Branch를 이용해서 사이클을 이루지 않도록 구성한 데이터 구조
실제 트리는 이진 트리 형태의 구조로 탐색 알고리즘 구현을 위해 많이 사용이 된다.

알아둘 용어
Node : 트리에서 데이터를 저장하는 기본 요소 (Branch 정보 포함)
Root Node : 트리 맨 위에 있는 노드
Level : 최상위 노드를 level 0으로 하였을 때, 하위 branch로 연결된 노드의 깊이를 나타냄
Parent Node : 어떤 노드의 다음 레벨에 연결된 노드
Chile Node : 어떤 노드의 상위 레벨에 연결된 노드
Leaf Node : Child Node가 하나도 없는 노드
Brother Node : 동일한 Parent Node를 가진 Node
Depth : 트리에서 Node가 가질 수 있는 최대 Level
'''



## Binary Search Tree (이진 탐색 트리)

# 1. 링크드 리스트를 구현
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 2. 이진 탐색 트리에 데이터 넣기
# class BST:
#     def __init__(self, head):
#         self.head = head

#     def insert(self, data):
#         self.current_node = self.head

#         while True:
#             if data < self.current_node.value: # 넣으려는 값이 해당 노드의 값보다 작다면 왼쪽으로 
#                 if self.current_node.left != None: # 왼쪽 Branch가 있다면
#                     self.current_node = self.current_node.left # left node로 이동
#                 else:
#                     self.current_node.left = Node(data) # 없다면 left Node에 insert
            
#             else: # 넣으려는 값이 해당 노드보다 크다면 오른쪽으로
#                 if self.current_node.right != None: # 오른쪽 node에 값이 있다면
#                     self.current_node = self.current_node.rigth
#                 else:
#                     self.current_node.right = Node(data)


# 3. 이진 탐색 트리에 serch 함수 넣기

# class BST:
#     def __init__(self,head):
#         self.head = head

#     def insert(self, data):
#         self.current_node = self.head

#         while True:
#             if data < self.current_node.value:
#                 if self.current_node.left != None:
#                     self.current_node = self.current_node.left
#                 else:
#                     self.current_node.left = Node(data)
#             else:
#                 if self.current_node.right != None:
#                     self.current_node = self.current_node.rigth
#                 else:
#                     self.current_node.right = Node(data)
    
#     def serch(self, data):
#         self.current_node = self.head

#         while self.current_node:
#             if self.current_node.value == data:
#                 return True # 찾으려는 값이 존재한다
#             elif self.current_node.value < data: # 찾으려는 데이터가 현재 노드의 값보다 크다면
#                 self.current_node = self.current_node.right
#             else:
#                 self.current_node = self.current_node.left
#         # 위에서 while 문을 돌고도 없다면 해당 데이터가 없으니 Return False
#         return False
    

# 4. 이진 탐색 트리 삭제
'''
1. 이어지는 Branch가 없는 경우 (Leaf Node인 경우)
2. 이어지는 Branch가 1개인 경우 (Child Node가 1개인 경우)
3. 이어지는 Branch가 2개인 경우 (Child Node가 2개인 경우)
이렇게 3가지의 경우로 생각해 봐야함.
'''

class BST:
    def __init__(self,head):
        self.head = head

    def insert(self, data):
        self.current_node = self.head

        while True:
            if data < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(data)
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(data)
    
    def serch(self, data):
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == data:
                return True 
            elif self.current_node.value < data: 
                self.current_node = self.current_node.right
            else:
                self.current_node = self.current_node.left
        return False

    def delete(self,data):
        # 먼저 삭제할 노드 탐색
        serched = False
        self.current_node = self.head # 현재 노드
        self.parent = self.head # 현재 노드의 Parent node

        while self.current_node:
            if self.current_node.value == data:
                serched = True
                break
            elif self.current_node.value < data:
                self.parent = self.current_node
                self.current_node = self.current_node.right
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.left
        
        # 찾고자 하는 데이터가 없는 경우
        if serched == False:
            return False
        

        # case 1 Leaf Node인 경우
        if (self.current_node.left == None) and (self.current_node.right == None):
            if data < self.parent.value: 
                self.parent.left = None
            else:
                self.parent.right = None

        
        # case 2 Child Node 가 1개 있는 경우
        elif (self.current_node.left != None) and (self.current_node.right == None): # Child node가 왼쪽에 있는경우 
            if data < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left

        elif (self.current_node.left == None) and (self.current_node.right != None):  # Child Node가 오른쪽에 있는 경우
            if data > self.parent.value:
                self.parent.right = self.current_node.right
            else:
                self.parent.left = self.current_node.right


        # case 3 Child Node가 2개 있는 경우
        elif (self.current_node.left != None) and (self.current_node.right != None):
            # case 3-1 삭제할 node의 오른쪽 node 중 가장 작은 값을 삭제할 node의 parent node가 가르키도록 하는 경우
            if data < self.parent.value:
                # serch Leaf Node
                self.change_node = self.current_node.right 
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left
            # case 3-2
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

        return True


if __name__ == '__main__':
    # 0 ~ 999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제
    import random

    # 0 ~ 999 중, 100 개의 숫자 랜덤 선택
    bst_nums = set()
    while len(bst_nums) != 100:
        bst_nums.add(random.randint(0, 999))
    # print (bst_nums)

    # 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
    head = Node(500)
    binary_tree = BST(head)
    for num in bst_nums:
        binary_tree.insert(num)
        
    # 입력한 100개의 숫자 검색 (검색 기능 확인)
    for num in bst_nums:
        if binary_tree.search(num) == False:
            print ('search failed', num)

    # 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
    delete_nums = set()
    bst_nums = list(bst_nums)
    while len(delete_nums) != 10:
        delete_nums.add(bst_nums[random.randint(0, 99)])

    # 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
    for del_num in delete_nums:
        if binary_tree.delete(del_num) == False:
            print('delete failed', del_num)




                    