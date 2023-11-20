# # 부모 Class 생성
# class Parents():
#     parants_num = 0 # Class 변수
#     def __init__(self, arg1, arg2, arg3): # 생성자
#         self.arg1 = arg1 # instance 변수 (인스턴스 변수)
#         self.arg2 = arg2
#         self.arg3 = arg3
#         Parents.parants_num += 1 # Class 변수에 1을 넣어주어서 Parents Class가 몇개 생성 되었는지 확인

#     def talk(self,text): # Class 내 함수 
#         self.text = text

# # 상속 (자식 Class 생성)
# class Children(Parents):
#     children_num = 0
#     def __init__(self,arg1,arg2,arg3):
#         super().__init__(1,2,3) ## 생성자 오버라이딩
#         ## super()를 통해서 생성자 오버라이딩 할 때, 인자(Arguments)값을 넣어주어야 함.
#         ## 안 넣어주면 안되더라구 
#         Children.children_num += 1
    
# mother = Parents(1,2,3)
# father = Parents(2,3,4)
# print(f"Parants Class number : {mother.parants_num}")

# son1 = Children(1,2,3)
# son2 = Children(2,3,4)

# print(f"Children Class number : {son2.children_num}")

# print("=" * 100)
##################################################################################
# 부모 Class에서 인자값들은 Default 해주면 super().__init__()으로 사용가능 ~! 

# 부모 Class 생성
class Parents():
    parants_num = 0 # Class 변수
    def __init__(self, arg1=None, arg2=None, arg3=None ): # 생성자
        self.arg1 = arg1 # instance 변수 (인스턴스 변수)
        self.arg2 = arg2
        self.arg3 = arg3
        Parents.parants_num += 1 # Class 변수에 1을 넣어주어서 Parents Class가 몇개 생성 되었는지 확인

    def talk(self,text): # Class 내 함수 
        self.text = text

# 상속 (자식 Class 생성)
class Children(Parents):
    children_num = 0
    def __init__(self,arg1,arg2,arg3):
        super().__init__() ## 생성자 오버라이딩
        Children.children_num += 1
    
mother = Parents(1,2,3)
father = Parents(2,3,4)
print(f"Parants Class number : {mother.parants_num}")

son1 = Children(1,2,3)
son2 = Children(2,3,4)

print(f"Children Class number : {son2.children_num}")
