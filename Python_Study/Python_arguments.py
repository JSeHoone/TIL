## 일반적인 함수 사용
def func1(arg1, arg2):
    sum_ = arg1 + arg2
    return sum_


def func2(arg1 = 1, arg2 = 2):
    sum_  = arg1 + arg2
    return sum_

print(f"function1_result = {func1(1,2)} // function2_result = {func2()}")

## 위치 가변 매개변수
# -> arguments로 몇개의 값이 들어가도 상관이 없음 // *arg에서 매개변수는 튜플 형태로 들어가게 됨.
def func3(*arg):
    sum_ = 0
    print_type = type(arg)
    for i in arg:
        sum_ += i
    return sum_, print_type
print(f"function3_resunlt = {func3(1,2,3,4,5,6,7,8,9,10)[0]} // *arg type = {func3(1,2,3)[1]}")

## 위치 가변 매개변수 오류나는 방법
def func4(*arg, arg1,arg2):
    sum_ = arg1 + arg2
    return sum_
# print(f"Expectation 3 But result {func4(1,2)}") ## Error 발생 *arg로 값을 다 받기 떄문이다.
print(f"{func4(arg1 = 1,arg2 = 2)}") ## 위 함수를 사용하기 위해서는 키워드 지정방식으로 사용해야 한다.

## 키워드 가변 매개변수
# python dictionary 형태로 argument 값을 받는다
def func5(**kwargs):
    print_type = type(kwargs)
    for key, value in kwargs.items():
        print((key,value) ,end = ' ')
    print(print_type)
func5(name = 'Sayhoon', age = 26, gender = 'male')

## 키워드 가변 매개변수 오류나는 방법
# Syntax Error가 발생함 
# def func6(**kwargs, age , gender):
#     print(age,gender)
# func6(name = "Sayhoon", age = 26, gender = 'male')