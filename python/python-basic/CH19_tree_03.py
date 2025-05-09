"""
2025.05.06 화
"""

print()
print()
print("------------------------------------------------")
print("--- 트리 3. 이진 탐색 트리(Binary Search Tree)")
print("------------------------------------------------")
print()

'''
[이진 탐색 트리(Binary Search Tree, BST)]

- 이진 탐색 트리는 이진 트리의 한 종류로, 노드의 왼족 자식은 항상 자신보다 작은 값, 오른쪽 자식은 항상 자신보다 큰 값을 가지는 트리이다.
- 왼쪽 자식은 보통 부모보다 작은 값, 오른쪽 자식은 부모보다 큰 값을 가진다.

[규칙]

1. 왼쪽 서브트리의 모든 노드 < 루트 노드의 값
2. 오른쪽 서브트리의 모든 노트 > 루트 노드의 값

[장점]

- 탐색, 삽입, 삭제 연산이 평균적으로 O(logn)의 시간 복잡도를 가진다.
- 중위 순회하면 항상 오름차순 정렬된 값을 출력한다.

[삽입(insert)를 왜 해야할까?]

- 트리는 동적으로 데이터를 추가할 수 있어야 한다.

[탐색(Search)을 왜 해야할까?]

- 트리의 주 목적 중 하나는 데이터를 빠르게 찾는 것이다.
- BST에서는 값의 대소를 이용해 불필요한 탐색을 피할 수 있으므로 효율적이다.

[이진탐색트리 삭제의 정의]

- BST에서 삭제는 특정 값을 가진 노드를제거하는 연산이다.
- BST 정렬 규칙 (왼쪽 < 부모 < 오른쪽)을 유지하면서 삭제해야 한다.
'''

# 이진 탐색 트리(BST) - 삽입, 탐색, 중위 순회

# 노드 클래스 정의
class Node :
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

# 이진 팀색 트리에 값 삽입 함수
def insert(root, value) :
    if root is None :
        return Node(value)       # 트리가 비어있다면, 새 노드를 루트로 반환
    
    # 삽입할 값이 현재 노드보다 작으면 왼쪽으로 
    if value < root.value :
        root.left = insert(root.left, value)

    # 삽입할 값이 현재 노드보다 크면 오른쪽으로
    elif value > root.value :
        root.right = insert(root.right, value)

    # 변경된 루트를 반환
    return root

# 이진 탐색 트리에서 값 탐색 함수
def search(root, value) :
    # 트리가 비어있거나 못찾으면 false
    if root is None : 
        return False
    
    # 찾았을 경우 True
    if root.value == value : 
        return True
    # 왼쪽 하위 트리에서 계속 탐색
    elif value < root.value :
        return search(root.left, value)
    # 오른쪽 하위 트리에서 계속 탐색
    else :
        return search(root.right, value)

def inorder(node) :
    if node :
        inorder(node.left)
        print(node.value, end = "  ")
        inorder(node.right)

# 빈 트리 생성
root = None

# 값 삽입
values = [50, 30, 70, 20, 40, 60, 80, 35]

for value in values :
    root = insert(root, value)

# 중위 순회 출력(정렬 확인())
inorder(root)

# 탐색 예제
print("탐색 결과")
print(" 60 찾기 : ", search(root, 80))
print(" 25 찾기 : ", search(root, 25))

print()
print()
print("----------------------------------------")
print("--- BST 삭제 알고리즘 : 3가지 케이스")
print("----------------------------------------")
print()

'''
[BST 삭제 알고리즘 : 3가지 케이스]

케이스 1. 자식이 없는 노드를 삭제(리프 노드)
케이스 2. 자식이 1개인 노드 삭제
케이스 3_1. 자식이 2개인 노드 삭제
케이스 3_2. 자식이 2개인 노드 삭제 (루트 노드를 삭제 시킴)
            -> 왼쪽 서브트리의 최대값(최대 노드) 또는 오른쪽 서브트리의 최소값(최소 노드)를 가져와서 대체한 뒤, 그 노드를 삭제한다.
                   50
                /     \
             30         70
           /   \       /  \
         20    40     60   80 
'''

'''
* 자식이 2개인 노드 삭제 연습
1. 트리 구조 그리기
              60
          /       \
        40         90
      /   \      /     \
    30     50   80      100
                       /
                     95

2. 삭제 대상 : 90
              60
          /       \
        40          95
      /   \      /     \
    30     50   80      100
'''

# 노드 클래스 정의
class Node :
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

# 삽입 함수
def insert(root, value) :
    if root is None :
        return Node(value)
    
    if value < root.value :
        root.left = insert(root.left, value)

    elif value > root.value :
        root.right = insert(root.right, value)

    return root

# 중위 순회 함수
def inorder(node) :
    if node :
        inorder(node.left)
        print(node.value, end = "  ")
        inorder(node.right)

# 최소값 찾기 (오른쪽 서브트리에서 가장 작은 값 찾을 때 사용)
def find_min(node) :
    current = node
    while current.left :
        current = current.left      # 왼쪽 자식이 없을 때까지 내려감
    return current                  # 가장 왼쪽 노드(최소값) 반환

# 이진 탐색 트리에서 값을 삭제하는 함수
def delete(root, value) :
    # 트리가 비어있으면 아무 작업도 하지 않음
    if root is None :
        print(f"값 {value}를 찾을 수 없습니다.")
        return None
    
    # 삭제할 값이 현재 노드보다 작으면 왼쪽으로
    if value < root.value :
        print(f"{value} < {root.value} --> 왼쪽으로 이동")
        root.left = delete(root.left, value)

    # 삭제할 값이 현재 노드보다 크면 오른쪽으로
    elif value > root.value :
        print(f"{value} > {root.value} --> 오른쪽으로 이동")
        root.right = delete(root.right, value)

    else :
        # 삭제할 노드를 찾은 경우(로그 찍기)
        print(f"삭제할 노드 {value}를 찾았습니다.")

        # 1. 자식이 없는 경우(리프 노드)
        if root.left is None and root.right is None :
            print(f"{value}는 리프노드입니다. 삭제합니다.")
            return None
        
        # 2. 왼쪽 자식이 없는 경우 -> 오른쪽 자식을 올림
        elif root.left is None :
            print(f"{value}는 오른쪽 자식만 있습니다. 오른쪽 자식을 올립니다.")
            return root.right
        
        # 3. 오른쪽 자식이 없는 경우 -> 왼쪽 자식을 올림
        elif root.right is None :
            print(f"{value}는 왼쪽 자식만 있습니다. 왼쪽 자식을 올립니다.")
            return root.left
        
        # 4. 자식이 둘 다 있는 경우
        else :
            # 오른쪽 서브트리에서 가장 작은 값을 찾아 현재 노드 값과 교체
            min_node = find_min(root.right)
            print(f"{value}는 자식이 2개입니다. {min_node.value}로 교체한 후, {min_node.value}값을 삭제합니다.")

            root.value = min_node.value

            # 그 최소값을 오른쪽 서브트리에서 제거
            root.right = delete(root.right, min_node.value)

    # 삭제 후 현재 루트 반환
    return root

# 트리 생성에 사용할 값들
values = [50, 30, 70, 20, 40, 60, 80, 35]

# 트리 초기화
root = None

# 주어진 값들을 순서대로 삽입하여 이진 탐색 트리 구성
for value in values :
    root = insert(root, value)

# 삭제 전 트리 상태 출력(중위 순회)
print("삭제 전 (중위 순회)")
inorder(root)
print('\n')

# 값 90을 삭제
root = delete(root, 90)

# 삭제 후 트리 상태 
print('\n')
print("삭제 후 (중위 순회)")
inorder(root)

print()
print("------------------------")
print()

# 예제 2. 자식이 2개인 노드 삭제

# 노드 클래스 정의
class Node :
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

# 값 삽입 함수
def insert(root, value) :
    if root is None :
        return Node(value)
    
    if value < root.value :
        root.left = insert(root.left, value)

    elif value > root.value :
        root.right = insert(root.right, value)

    return root

# 중위 순회 함수
def inorder(node) :
    if node :
        inorder(node.left)
        print(node.value, end = "  ")
        inorder(node.right)

# 최소값 찾기
def find_min(node) :
    current = node
    while current.left :
        current = current.left
    return current

# 값 삭제 함수
def delete(root, value) :
    if root is None :
        print(f"값 {value}를 찾을 수 없습니다.")
        return None
    
    elif value > root.value :
        print(f"{value} > {root.value} --> 오른쪽으로 이동")
        root.right = delete(root.right, value)

    else :
        # 삭제할 노드를 찾은 경우(로그 찍기)
        print(f"삭제할 노드 {value}를 찾았습니다.")

        # 1. 자식이 없는 경우(리프 노드)
        if root.left is None and root.right is None :
            print(f"{value}는 리프노드입니다. 삭제합니다.")
            return None
        
        # 2. 왼쪽 자식이 없는 경우 -> 오른쪽 자식을 올림
        elif root.left is None :
            print(f"{value}는 오른쪽 자식만 있습니다. 오른쪽 자식을 올립니다.")
            return root.right
        
        # 3. 오른쪽 자식이 없는 경우 -> 왼쪽 자식을 올림
        elif root.right is None :
            print(f"{value}는 왼쪽 자식만 있습니다. 왼쪽 자식을 올립니다.")
            return root.left
        
        # 4. 자식이 둘 다 있는 경우
        else :
            min_node = find_min(root.right)
            print(f"{value}는 자식이 2개입니다. {min_node.value}로 교체한 후, {min_node.value}값을 삭제합니다.")
            root.value = min_node.value
            root.right = delete(root.right, min_node.value)

    return root

# 트리 생성에 사용할 값들
values = [50, 30, 70, 20, 40, 35, 45]

# 트리 초기화
root = None

for value in values :
    root = insert(root, value)

print("삭제 전 (중위 순회)")
inorder(root)
print()

root = delete(root, 45)

print("삭제 전 (중위 순회)")
inorder(root)

print('\n')
print()
print("------------------------ 끝")
print()
