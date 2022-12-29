import time

## 제곱근을 취하여 연산 속도를 더 빠르게 해주었다.
start_1 = time.time()
n=16
a = [False,False] + [True]*(n-1)

for i in range(2, int(n**.5)+1):
  if a[i]:
    for j in range(2*i, n+1 , i):
        a[j] = False

primes=[i for i in range(n+1) if a[i]==True]
print(f"제곱근 취할시 : {time.time() - start_1 : 0.8f}")



### 제곱근은 취하지 않음!
start_2 = time.time()
n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(f"제곱근 안 취할시 : {time.time() - start_2 : 0.8f}")

''' Result 
제곱근 취할시   :  0.00000811
제곱근 안 취할시 :  0.00018787
'''