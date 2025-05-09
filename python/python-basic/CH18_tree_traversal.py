"""
2025.05.02 금
"""

print()
print()
print("-----------------------------")
print("--- 트리 순회 1. 전위 순회")
print("-----------------------------")
print()

'''
[트리 순회]

- 트리의 모든 노드를 일정한 규칙에 따라 한 번씩 방문하는 과정을 말한다.
- 트리 구조는 계층적이기 때문에 순회 방법에 따라 노드를 방문하는 순서가 달라지며, 대표적인 순회방식은 다음과 같다.

1. 전위 순회
    순서 : 루트 -> 왼쪽 서브트리 -> 오른쪽 서브트리 방문
'''

class Node3 :
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

# 트리 구조 생성
root = Node3("A")
root.left = Node3("B")
root.right = Node3("C")
root.left.left = Node3("D")
root.left.right = Node3("E")

# 전위 순회 함수 정의 : 루트 -> 왼쪽 -> 오른쪽
def preorder(node) :
    if node :
        # 전위 순회에서는 루트 노드를 먼저 방문하니까 현재 노드를 먼저 출력하는 것이다.
        print(node.value, end = '  ')        # 1단계 : 현재 노드 출력

        # 현재 노드의 왼쪽 자식 노드를 재귀적으로 전위 순회 한다.
        # 즉, 왼쪽 서브 트리부터 다시 전위 순회를 시작하는 것이다.
        preorder(node.left)                 # 2단계 : 왼쪽 자식 방문

        # 왼쪽 다 끝났으면 오른쪽으로 넘어가서 또 순회한다.
        preorder(node.right)                # 3단계 : 오른쪽 자식 방문

# 함수 실행
print("1. 전위 순회 결과")
preorder(root)

print('\n')
print("------------------------")
print()

class Node4 :
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

# 트리 구조 생성
root = Node4("M")
root.left = Node4("N")
root.right = Node4("O")
root.left.left = Node4("P")
root.right.left = Node4("Q")
root.right.right = Node4("R")

def preorder2(node) :
    if node :
        print(node.value, end = "  ")
        preorder2(node.left)
        preorder2(node.right)

print("2. 전위 순회 결과")
preorder2(root)

print('\n')
print()
print("------------------------")
print("--- 재귀 함수")
print("------------------------")
print()

'''
[재귀 호출]

- 함수가 자기 자신을 다시 부르는 프로그래밍 기법
'''

# 간단한 재귀 함수 (숫자 출력) 예시
print(">> 재귀 함수")

def countdown(n) :
    # 기저 조건 : if n > 0 이 업승면 무한 반복돼서 오류 발생
    if n > 0 :
        print(n)
        countdown(n - 1)

    else :
        print("끝")

# 함수 실행
countdown(5)

print()
print()
print("-----------------------------")
print("--- 트리 순회 2. 중위 순회")
print("-----------------------------")
print()

'''
[중위 순회]

- 순서 : 왼쪽 -> 루트 -> 오른쪽 
- 트리의 왼쪽 서브트리를 먼저 순회하고, 그 다음 루트 노드를 처리한 후, 오른쪽 서브트리르 순회한다.
'''

# 중위 순회 예제 : DBEAC
class Node5 :
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

# 트리 구조 생성
root = Node5("A")
root.left = Node5("B")
root.right = Node5("C")
root.left.left = Node5("D")
root.left.right = Node5("E")

# 중위 순회 함수 : 왼쪽 -> 루트 -> 오른쪽
def inorder(node) :
    if node :
        inorder(node.left)
        print(node.value, end = '  ')
        inorder(node.right)

# 순회 실행
print("2. 중위 순회 결과")
inorder(root)

'''
- 트리는 계층 구조이다.
- 전위 순회 순서 : 루트 -> 왼쪽 -> 오른쪽
- 중위 순회 순서 : 왼쪽 -> 루트 -> 오른쪽
'''

print()
print()
print("-----------------------------")
print("--- 트리 순회 3. 후위 순회")
print("-----------------------------")
print()

'''
2025.05.06 화

[후위 순위]

- 트리의 노드를 왼쪽 오른쪽 루트 순서로 방문한다.
- 즉, 자식 노드를 모두 방문한 후, 가장 마지막에 부모 노드를 처리하는 방식이다.

4-5-2-6-7-3-1
D  B  E  G  F  C  A
'''

# 노드 클래스 정의
class Node : 
    def __init__(self, value) :
        self.value = value
        self.left = None        # 왼쪽 자식 노드
        self.right = None       # 오른쪽 자식 노드

# 트리 생성
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

# 후위 순회 함수
def postorder(node) :
    if node :
        postorder(node.left)        # 왼쪽 자식 방문
        postorder(node.right)       # 오른쪽 자식 방문
        print(node.value, end = '  ')       # 현재 노드 출력

# 후위 순회 실행
print("후위 순회 실행")
postorder(root)

print('\n')
print("------------------------")
print()

# 노드 클래스 정의
class Node : 
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

root = Node("1")
root.left = Node("2")
root.right = Node("3")
root.left.left = Node("4")
root.left.right = Node("5")
root.right.left = Node("6")
root.right.right = Node("7")

def postorder(node) :
    if node :
        postorder(node.left)
        postorder(node.right)
        print(node.value, end = '  ')

print("후위 순회 실행")
postorder(root)

print('\n')
print("------------------------ 끝")
print()
