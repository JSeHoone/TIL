## Python으로 Hash Table 구현하기
# Reference: 패스트캠퍼스 강의 (개발자 취업 합격 패스 With 코딩테스트, 기술면접 초격차 패키지 Online.)

'''
Hash 구조
- Hash Table: 키(Key)에 데이터(Value)를 저장하는 데이터 구조
- Key를 통해서 데이터를 바로 받아올 수 있으므로, 속도가 빨라짐
- 파이썬의 Dict가 Hash Table의 예시
- 보통 배열로 미리 Hash Table 사이즈 만큼 생성 후에 사용
  (공간과 탐색시간을 맞바꾸는 기법)

알아둘 용어
- Hash : 임의 값을 고정 길이로 변환하는 것
- Hash Table : 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
- Hashing Function : Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
- Hash Value or Hash Address : Key를 해싱함수로 연산해서, Hash 값을 알아내고
                               이를 기반으로 Hash Table에서 해당 Key에 대한 데이터 위치를 일관성 있게 찾을 수 있음
- Slot : 한 개의 데이터를 저장할 수 있는 공간

저장할 데이터에 대해 Key를 추출할 수 있는 병도 함수도 존재할 수 있음
 
'''

## 1. 간단한 Hash Table 만들기
hash_table = [i for i in range(10)]
print(hash_table)

# 초간단 Hash Function 만들기 (가장 간단한 방법이 나머지 값을 사용하는 기법)
def hash_func(key):
    return key % 5 

# Hash Table에 저장해보기
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'
''' 데이터에 따라 필요시 Key 생성 방법 정의가 필요합니다
여기서는 문자열 데이터가 들어왔기 때문에 ord()함수를 사용하여 ASCII(아스키)코드로 리턴하여
문자열을 숫자로 표현 후 hash function에 넣어 Hash value를 만들어줍니다'''
print (ord(data1[0]), ord(data2[0]), ord(data3[0]))
print (ord(data1[0]), hash_func(ord(data1[0])))
print (ord(data1[0]), ord(data4[0]))
# 이렇게 만들면 중복되는 아스키 코드가 있을 것 같음

def storage_data(data, value):
    key = ord(data[0]) # 문자열 데이터의 앞 부분을 아스키코드로 변환하여 key를 만듬
    hash_address = hash_func(key) # 위에서 만든 해쉬 함수를 통해 hash adress생성
    hash_table[hash_address] = value

storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01022223333')
print(hash_table)

# 저장한 데이터를 읽어오는 함수
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]
print(get_data('Andy'))