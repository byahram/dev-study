"""
2025.04.29 화
"""

print()
print()
print("------------------------------")
print("--- 연결리스트(LinkedList)")
print("------------------------------")
print()

'''
[연결리스트(LinkedList)란?]

- 데이터를 일렬로 저장하지만, 연속된 메모리 공간이 아니다.
- 각 데이터(노드)가 다음 데이터의 위치(주소)를 기억하는 방식으로 연결되어 있는 자료구조이다.

[연결리스트 시각화]

Head -> [데이터 | 다음 노드의 주소] -> [데이터 | 다음 노드의 주소] -> [데이터 | NONE] 
Head -> [체리] -> [수박] -> [블루베리]

[연결리스트 특징]

- 각 노드는 두가지 정보를 가진다.
    - 데이터 : 저장할 데이터
    - 주소 : 다음 노드를 가리키는 포인터(주소)
- 맨 앞 노드(Head)에서 시작해서 다음 노드를 따라가며 전체를 순회함.
- 데이터를 중간에 넣거나 삭제하기가 쉬움.

[한 줄 요약]

- 연결리스트는 순서를 유지하여, "자주 추가/삭제가 필요한 상황"에 유리한 자료구조이다.
'''

'''
[리스트 vs 연결리스트의 차이]

항목                        리스트(배열 기반)                       연결리스트
저장방식            연속된 메모리에 저장 : arr[0]           노드들이 포인터로 연결된다.
접근 속도           인덱스로 빠르게 접근                    순차적으로 탐색해야함
삽입/삭제           중간 삽입/삭제 시 느림                  중간 삽입/삭제가 빠르다.
크기               처음부터 크기를 정하거나 자동 증가        노드 추가할 때마다 크기가 유동적임
구현 난이도         파이썬에서는 매우 쉽다                  직접 클래스를 만들어야 한다.
예시               학생 이름 목록, 상품 리스트 등           브라우저 뒤로가기, 큐, 힙, 그래프등

[리스트 삽입/삭제 예시]

- [1,2,3,4,5,7,8,9,10] 중간에 삭제를 할 경우 한 칸씩 다 앞으로 와야해서 느림
'''

# 하나의 노드를 나타내는 클래스 정의
class Node :
    def __init__(self, data) :
        self.data = data        # 노드가 담고 있는 데이터
        self.next = None        # 다음 노드의 주소를 저장할 변수

# 연결 리스트 전체를 관리할 클래스 정의
class LinkedList :
    def __init__(self) :
        self.head = None        # 연결리스트의 시작점(처음엔 비어있음)

    # 리스트에 새 노드를 추가하는 메서드
    def append(self, data) :
        new_node = Node(data)   # 새 노드 생성

        # 리스트가 비어있다면
        if self.head is None :
            self.head = new_node        # head가 새 노드를 가리키게 함
            return
        
        # 리스트가 이미 있으면 -> 맨 끝까지 가야한다.
        current = self.head
        while current.next :            # current.next가 None이 아닐 동안 반복
            current = current.next      # 다음 노드로 이동
        current.next = new_node         # 마지막 노드의 next를 새 노드로 연결
                                        # [체리] -> [수박]
                                        # 지금 있는 노드가 새 노드한테 이어주는 것
    
    # 리스트에서 노드를 삭제하는 메서드
    def delete(self, data) :
        current = self.head         # 현재 노드를 head부터 시작
        prev = None                 # 이전 노드는 처음엔 없음

        while current :                     # 노드가 있는 동안 계속 반복
            if current.data == data :       # 찾는 데이터라면
                if prev is None :
                    # 첫 번째 노드를 삭제하는 경우
                    self.head = current.next
                else :
                    # 중간 또는 마지막 노드 삭제
                    prev.next = current.next
                print(f"`{data}`를 삭제했습니다.")
                return
            
            # 이전 노드를 현재로 저장하고
            prev = current
            # 다음 노드로 이동
            current = current.next

    # 리스트 전체 내용을 출력하는 메서드
    def print_all(self) :
        current = self.head             # 맨 처음 노드부터 시작

        while current :                 # current가 None이 아닐 때까지 반복
            print(current.data, end = ' -> ')       # 데이터 출력(줄바꿈 없이)
            current = current.next                  # 다음 노드로 이동
            
        print("None")           # 마지막 표시


# 빈 연결 리스트 생성
li = LinkedList()
li.append("체리")
li.append("바나나")
li.append("수박")
li.print_all()

li.delete("체리")
li.print_all()

print()
print("------------------------")
print()

'''
['라면'을 삭제하는 과정]

1. 처음부터 노드를 하나씩 살펴보기
      head -> [] -> [] ->
      current = self.head # 현재 노드를 head 부터 시작
      previous = None # 이전 노드는 처음엔 없음
2. current의 menu가 '라면'인지 확인
    previous = current
    current = current.next      # 다음 노드로 이동
3. current가 '라면'을 찾으면
    # 다음 노드로 이동
4. 이전 노드의 next 를 현재 노드의 다음 노드로 연결
    [김밥 | 라면의 주소] -> [라면 | 샐러드의 주소] -> [샐러드 | 돈까스 주소]
    [김밥 | 샐러드의 주소] -> [샐러드 | 돈까스주소]
    previous.next = current.next
'''

class Menu :
    def __init__(self, menu) :
        self.menu = menu
        self.next = None

class LunchList :
    def __init__(self) :
        self.head = None
    
    def add_menu(self, menu) :
        new_menu = Menu(menu)
        
        if self.head is None :
            self.head = new_menu
            return 
        
        current = self.head

        while current.next :
            current = current.next

        current.next = new_menu

    def delete_menu(self, menu) :
        current = self.head
        prev = None

        while current :
            if current.menu == menu :
                if prev is None :
                    self.head = current.next
                else :
                    prev.next = current.next
                print(f"`{menu}`를 삭제했습니다.")
                return
        
        prev = current
        current = current.next

    def print_menu(self) :
        current = self.head
        
        if current : 
            print("오늘 먹은 점심 메뉴 :")

            while current :
                print(current.menu)
                current = current.next
            print("끝.")

lunch_menu = LunchList()
lunch_menu.add_menu("김밥")
lunch_menu.add_menu("라면")
lunch_menu.add_menu("샐러드")
lunch_menu.add_menu("돈까스")
lunch_menu.print_menu()

