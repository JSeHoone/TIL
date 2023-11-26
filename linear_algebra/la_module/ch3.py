# ## Scalar 객체 생성 -> int object는 상속 받아서 만들순 없을까?
# class Scalar():
#     '''
#     You only use Scalar Object
#     to four basic operations.
#     '''
#     def __init__(self, scalar) -> None:
#         self.data = scalar

#     # add magic method
#     def __add__(self, other:'Scalar') -> 'Scalar':
#         return Scalar(self.data + other.data)

#     def __radd__(self, other: 'Scalar') -> 'Scalar':
#         return Scalar(self.data + other.data)
    
#     # subtraction magic method
#     def __sub__(self, other : 'Scalar') -> 'Scalar':
#         return Scalar(self.data - other.data)

#     def __rsub__(self, other : 'Scalar') -> 'Scalar':
#         return Scalar(self.data + other.data)
    
#     # multiplication magic method
#     def __mul__(self, other : 'Scalar') -> 'Scalar':
#         return Scalar(self.data * other.data)
    
#     def __rmul__(self, other : 'Scalar') -> 'Scalar':
#         return Scalar(self.data * other.data)
    
#     # division magic method 
#     def __truediv__(self, other : 'Scalar') -> 'Scalar':
#         return Scalar(self.data / other.data)
    
#     def __truerdiv__(self, other : 'Scalar') -> 'Scalar':
#         return Scalar(self.data / other.data)
    

# # Scalr object test
# a = Scalar(1)
# b = Scalar(4)
# add_ = a + b
# sub_ = a - b
# mul_ = a * b
# div_ = a / b
# print(f"result type : {type(add_)},\n result number : {add_.data}")
# print(f"result type : {type(sub_)},\n result number : {sub_.data}")
# print(f"result type : {type(mul_)},\n result number : {mul_.data}")
# print(f"result type : {type(div_)},\n result number : {div_.data}")

### Scalar처럼 만들어서 학습하는 것은 비효율적이라 생각이 들어 책 내용 그대로 고고

# Vector = Scalar의 집합 
# magnitude(크기) 와 direction(방향)을 가짐


### Vector의 사칙연산
## 1. 덧셈 : 두 Vector의 크기가 같아야 한다 (= Scalar의 갯수가 같아야 한다.)
vec_a = [1,2,3]
vec_b = [1,2,3]

# 방법 1
add_ab = []
for i in range(len(vec_a)):
    scalar = vec_a[i] + vec_b[i]
    add_ab.append(scalar)
print(add_ab) # result : [2, 4, 6]

add_ab2 = []
# 방법 2 - vector의 크기가 같아야 성립하기에 zip사용 가능
for a,b in zip(vec_a, vec_b):
    add_ab2.append(a+b)
print(add_ab2)

## 2. 뺄셈 : 덧셈과 동일함
sub_ab = []
for a,b in zip(vec_a, vec_b):
    sub_ab.append(a-b)
print(sub_ab)  # result : [0,0,0]

## 3. Scalar 곱 : 각각의 vector 원소에 scalar 값을 곱해줌
scalar_mul_a = [i*4 for i in vec_a]
print(scalar_mul_a) # result [4,8,12]

## 4. vector 원소 곱 : vector 원소에 대응하여 곱해주는 연산
vec_mul_ab = []
for a,b in zip(vec_a, vec_b):
    vec_mul_ab.append(a * b)
print(vec_mul_ab) # result : [1,4,9]


#### Matrix (행렬)

## 1. 행렬의 덧셈
def add(mat1, mat2) -> list:
    result = []
    for row_1, row_2 in zip(mat1,mat2):
        mid_save = []
        for col_1,col_2 in zip(row_1, row_2):
            mid_save.append(col_1 + col_2)
        result.append(mid_save)
    return result

## 2. 행렬의 뺄셈
def sub(mat1, mat2) -> list:
    result = []
    for row_1, row_2 in zip(mat1,mat2):
        mid_save = []
        for col_1,col_2 in zip(row_1, row_2):
            mid_save.append(col_1 - col_2)
        result.append(mid_save)
    return result

## 3. 행렬의 Scalar 곱
def mul(mat1, scalar) -> list:
    result = []
    for row in range(len(mat1)):
        middle_save = [element * scalar for element in row]
        result.append(middle_save)
    return result


## 3. 행렬의 원소 곱
def scalar_mul(mat1, mat2) -> list:
    result = []
    for row_1, row_2 in zip(mat1,mat2):
        mid_save = []
        for col_1,col_2 in zip(row_1, row_2):
            mid_save.append(col_1 * col_2)
        result.append(mid_save)
    return result

## 4. 행렬간 곱
def mat_mul(mat1, mat2):
    result = []
    for r in range(len(mat1)):
        middle_save = []
        for c in range(len(mat2[0])):
            element_mul = 0
            for c2 in range(len(mat1[0])):
                element_mul += (mat1[r][c2] * mat2[c2][c])
            middle_save.append(element_mul)
        result.append(middle_save)
    return result