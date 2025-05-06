"""
2025.05.02 금
"""

print()
print()
print("------------------------")
print("--- 트리 1. 일반 트리")
print("------------------------")
print()

'''
[자료구조]

- 리스트(list), 스택, 큐 : 일렬로 데이터를 처리할 때 유용 (선형처리)
- 트리(tree) : 선형구조로 나타내기 어려운 상황이 있을때 (비선형구조)

[트리(tree)의 실제 예시]

1. 폴더 구조 : 내 컴퓨터 ->문서 -> 과제 자료 -> 업무자료
    -> 한 폴더 안에 여러 하위 폴더가 있고, 또 그 하위 폴더 안에 더 많은 폴더가 있는 구조는 전형적인 트리(tree)구조이다.
    -> 폴더는 ' 부모' 가 있고, 그 안에 '자식'폴더가 존재한다.

2. 게임 캐릭터 계층 구조
    -> rpg 게임에서 캐릭터라는 클래스 아래에 전사, 마법사, 궁수 같은 하위 직업이 존재하고, 그 안에는 더 세부적인 작업이 있을 수 있다.
'''

'''
[트리의 정의]

- 트리는 데이터를 "계층 구조"로 저장하는 자료구조이다.
- 하나의 시작점(루트)에서 여러 방향으로 까지가 뻗어 나가는 형태를 가지고 있어, 한 부모가 여러 자식을 가질 수 있는 구조이다.

[트리의 기본 용어]

- 노드 (node)       : 트리의 각 요소(데이터 하나)
- 루트 노드(root)    : 트리의 가장 위에 있는 노드(시작점)
- 부모 노드(parent)	 : 자식 노드를 가지는 노드
- 자식 노드(child) 	 : 부모 아래에 연결된 노드
- 형제 노드		     : 같은 부모를 가진 노드
- 리프 노드		     : 자식이 없는 노드(끝 노드)
- 서브 트리		     : 하나의 노드와 그 자식들을 포함한 작은 트리
- 깊이		        : 루트에서 해당 노드까지의 거리(몇 단계 아래인지)
- 높이		        : 해당 노드에서 가장 깊은 리프까지의 거리

[트리의 종류]

1. 일반 트리 - 자식 노드 수에 제한 없음
2. 이진 트리 - 하나의 노드가 최대 2개의 자식만 가질 수 있는 트리 : 왼쪽 자식, 오른쪽 자식 나뉨
3. 이진 탐색 트리 - 왼쪽 자식 < 부모 < 오른쪽 자식 : 탐색, 삽입, 삭제에 효율적
'''

# 일반 트리 구현
class TreeNode :
    def __init__(self, data) :
        self.data = data        # 노드에 저장할 값
        self.children = []      # 자식 노드를 저장하는 리스트

    def add_child(self, child_node) :
        # 현재 노드에 자식 노드를 추가한다.
        self.children.append(child_node)

    def print_tree(self, level = 0) :
        # 트리 구조를 들여쓰기로 출력
        print("  " * level + str(self.data))
        for child in self.children :
            child.print_tree(level + 1)

# 트리 생성
def build_tree() :
    root = TreeNode("한국")

    # 1단계 자식 노드
    seoul = TreeNode("서울")
    busan = TreeNode("부산")
    incheon = TreeNode("인천")

    # 2단계 자식 노드
    gangnam = TreeNode("강남구")
    seocho = TreeNode("서초구")
    haeundae = TreeNode("해운대")

    # 트리 구조 연결
    root.add_child(seoul)
    root.add_child(busan)
    root.add_child(incheon)

    seoul.add_child(gangnam)
    seoul.add_child(seocho)
    busan.add_child(haeundae)

    return root

# 트리 출력
# 여기에 있는 코드는 '직접 실행할 때만' 실행된다.
# 이 코드를 모듈로 사용할 경우, 테스트 코드가 실행되지 않도록 하기 위함.
if __name__ == "__main__" :
    korea_tree = build_tree()
    korea_tree.print_tree()

print()
print("------------------------")
print()

class FoodTreeNode :
    def __init__(self, data) :
        self.data = data
        self.children = []

    def add_child(self, child_node) :
        self.children.append(child_node)

    def food_tree(self, level = 0) :
        print("  " * level + str(self.data))
        for child in self.children :
            child.food_tree(level + 1)

def build_food_tree() :
    root = FoodTreeNode("음식")

    k = FoodTreeNode("한식")
    c = FoodTreeNode("중식")
    w = FoodTreeNode("양식")

    k.add_child(FoodTreeNode("비빔밥"))
    k.add_child(FoodTreeNode("김치찌개"))

    c.add_child(FoodTreeNode("짜장면"))
    c.add_child(FoodTreeNode("마라탕"))

    w.add_child(FoodTreeNode("파스타"))
    w.add_child(FoodTreeNode("스테이크"))

    root.add_child(k)
    root.add_child(c)
    root.add_child(w)

    return root

if __name__ == "__main__" :
    korea_tree = build_food_tree()
    korea_tree.food_tree()

print()
print("------------------------ 끝")
print()
