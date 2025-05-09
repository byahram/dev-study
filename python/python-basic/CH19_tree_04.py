"""
2025.05.06 화
"""

print()
print()
print("----------------------------------------")
print("--- 이진 탐색 트리 + 비교 카운터 관리")
print("----------------------------------------")
print()

# 노드 클래스 정의
class Node :
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

# 이진 탐색 트리 + 비교 카운터 관리 클래스
class BSTCounter :
    def __init__(self) :
        self.root = None        # 트리의 루트 노드
        self.counter = 0        # 누적 비교 횟수를 저장하는 변수

    # 값 삽입 함수
    def insert(self, value) :
        # 트리가 비어있으면 루트로 삽입
        if self.root is None :
            self.root = Node(value)     # 루트 노드 생성
            print(0)                    # 첫 삽입은 비교 없음
            return
        
        # 현재 탐색할 노드를 루트로 시작
        current = self.root

        # 현재 삽입에 대해 비교한 횟수
        count = 0

        # 삽입할 위치를 찾을 때까지 반복
        while True :
            count += 1      # 현재 노드와 비교했으므로 +1
            
            if value < current.value :
                # 삽입할 값이 현재 노드보다 작을 경우 왼쪽
                if current.left is None :
                    current.left = Node(value)
                    print(self.counter + count)     # 누적된 count + 현재 비교수 출력
                    break

                current = current.left      # 왼쪽으로 이동

            else :
                # 삽입할 값이 현재 노드보다 크거나 같을 경우 오른쪽
                if current.right is None :
                    current.right = Node(value)
                    print(self.counter + count)     # 누적된 count + 현재 비교수 출력
                    break

                current = current.right      # 오른쪽으로 이동

        # 전체 비교 횟수 누적
        self.counter += count

# input으로 입력 받기
# 사용자로부터 숫자의 개수를 입력 받음
N = int(input("몇 개의 수를 입력하시겠습니까?"))

# 입력 받은 수를 저장할 리스트
sequence = []

print(f"{N}개의 수를 한 줄씩 입력하세요.")

for _ in range(N) :
    num = int(input())      # 사용자에게 정수를 하나씩 입력 받음
    sequence.append(num)

# BSTCounter 인스턴스를 생성하고 수열을 삽입
bst = BSTCounter()
for num in sequence :
    bst.insert(num)

print()
print("------------------------ 끝")
print()
