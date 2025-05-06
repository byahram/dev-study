"""
2025.05.02 금
"""

print()
print()
print("------------------------------------")
print("--- 트리 2. 이진 트리(Binary Tree)")
print("------------------------------------")
print()

'''
[이진트리 규칙]

- 모든 노드의 자식은 최대 2개다.
- 루트 노드는 트리의 시작점이다.

[노드 클래스 설계하기]

- 이진 트리를 만들기 위해 먼저 노드클래스를 정의해야한다.

class Node :
 	def __init__(self, value) :
		self.value = value      # 노드에 저장할 값
		self.left = None        # 왼쪽 자식 노드
		self.right = None

        1
      /    \
    2       3   
'''

# 노드 클래스 정의
class Node :
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

# 노드 생성
root = Node(1)
root.left = Node(2)
root.right = Node(3)

# 노드 값 출력
print("루트 노드 :", root.value)
print("왼쪽 자식 :", root.left.value)
print("오른쪽 자식 :", root.right.value)

print()
print("------------------------")
print()

class Node2 :
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

# 노드 생성
root = Node2(10)
root.left = Node2(5)
root.right = Node2(15)

root.left.left = Node2(2)
root.left.right = Node2(7)

# 트리 출력 함수
# node부터 시작해서 트리를 출력하는 함수. level은 들여쓰기 (깊이)
def print_tree(node, level = 0) :
    # 현재 노드가 존재할 때만 실행
    if node is not None :
        # 현재 노드의 값이 출력하되, 들여쓰기를 통해 트리 구조를 시각화
        print("  " * level + f"노드 값 : {node.value}")
        # 왼쪽 자식 노드를 재귀 호출(깊이 1 증가)
        print_tree(node.left, level + 1)
        # 오른쪽 자식 노드로 재귀 호출(깊이 1 증가)
        print_tree(node.right, level + 1)

print("트리 구조 출력")
print_tree(root)

print()
print("------------------------ 끝")
print()
