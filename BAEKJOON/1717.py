import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b

# node 갯수와 간선 의 개수 입력 받기
v,e = map(int,input().split())
parent = [0] * (v+1)

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    command,a,b = map(int,input().split())

    if command == 0:
        union(a,b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
