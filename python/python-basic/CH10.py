"""
2025.04.08 화
"""

print()
print()
print("------------------------")
print("--- 오버라이딩")
print("------------------------")
print()

'''
[오버라이딩]

- 부모 클래스에서 정의된 메서드를 자식 클래스에서 "같은 이름"으로 다시 정의하여 기능을 변경하는 것
- 즉, 상속에서 사용되는 개념, 부모 클래스의 메서드를 자식클래스에서 재정의(떺어쓰기)하는 것
- -> 부모 클래스의 메서드 대신 자식 클래스에서 새로 정의한 메서드가 호출된다.
'''

# 부모 클래스
class Animal : 
    def sound(self) :
        print("동물 소리")

# 자식 클래스
class Dog(Animal) :
    def sound(self) :       # 오버라이딩 (재정의 하는 것)
        super().sound()     # 부모의 메서드 호출
        print("멍멍")

# 자식 클래스
class Cat(Animal) :
    def sound(self) :
        print("야옹")

# 부모 메서드도 같이 쓰고 싶을때
# 객체 생성
a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()

print()
print("------------------------")
print()

# EX2
class Car : 
    def __init__(self, color):
        self.color = color
    
    def ride(self) :
        print(self.color, "차가 달립니다.")
        print("쌩쌩")

class Bus(Car) :
    def __init__(self, color, bellSound):       # 생성자 : 색상과 벨소리
        super().__init__(color)     # 부모 클래스의 생성자 호출
        self.bellSound = bellSound  #   인스턴스 변수 초기화

    def ride(self) :        # ride 메서드를 오버라이딩
        print(self.color, "버스가 달립니다.")
        print("살금살금")

    def pressBell(self) :
        print(self.bellSound)

car = Car("파랑")     # 파랑 자동차 생성
car.ride()        # 부모 클래서 ride() 생성

bus = Bus("빨간", "삑삑")
bus.ride()
bus.pressBell()

print()
print("------------------------")
print()

# EX3
class Person :
    def __init__(self, name):
        self.name = name

    def introduce(self) :
        print(f"안녕하세요. 저는 {self.name}입니다.")

class Student(Person) :
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    
    def introduce(self):        # 오버라이딩: 부모의 소개메서드를 재정의
        print(f"안녕하세요, 저는 {self.name}이고, {self.school} 학생입니다.")

class Teacher(Person) :
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"안녕하세요, 저는 {self.name} 선생님이고, {self.subject}를 가르칩니다.")

# 객체 생성 및 메서드 호출
person = Person("홍길동")
person.introduce()

p2 = Student("김민지", "해솔초등학교")
p2.introduce()

p3 = Teacher("이정훈", "수학")
p3.introduce()

print()
print()
print("------------------------")
print("--- 다중 상속")
print("------------------------")
print()

'''
[다중상속]

- 하나의 자식 클래스가 두 개 이상의 부모 클래스로부터 속성과 메서드를 모두 물려받는 것
- class 자식클래스(부모1, 부모2)
- 장점 : 여러 클래스의 기능을 한 클래스에 모을 수 있어 재사용성 증가
- 단점 : 부모 클래스에 같은 이름의 메서드가 있을 경우, 충돌이나 혼란 가능성
- pass : 아무것도 안하는 문장
- 파이썬에서는 클래스나 함수에 내용을 아직 안 쓸때 형식상 빈 블록을 만들기 위해 pass를 사용한다.
'''

# EX1
# 부모클래스 
class Fly :
    def fly(self) :
        print("날다")

# 부모 클래스
class Walk :
    def walk(self) : 
        print("걷다")

# 자식 클래스 _ 다중 상송
class Bird(Fly, Walk) :
    def sound(self) :
        print("짹짹")

# 객체 생성
b = Bird()

# 상속받은 메서드 사용
b.fly()
b.walk()
b.sound()

print()
print("------------------------")
print()

# EX2
class Flyer :
    def fly(self) :
        return "Flying"

class Swimmer :
    def swim(self) :
        return "Swimming" 

# pass : 아무것도 안하는 문장
# 파이썬에서는 클래스나 함수에 내용을 아직 안 쓸때 형식상 빈 블록을 만들기 위해 pass를 사용한다.
class Duck(Flyer, Swimmer) :
    pass

f = Flyer()
f_return = f.fly()
print(f_return)

s = Swimmer()
s_return = s.swim()
print(s_return)

print()
print("------------------------")
print()

# EX3
class A :
    def show(self) :
        return "A"
    
class B :
    def show(self) :
        return "B"
    
class C(A, B) :
    pass

obj = C()
print(obj.show())       # 충돌상황이 생길 경우 왼쪽 부모인 A가 우선됨

print()
print("------------------------")
print()

# EX4. 다중 상속 + 자식이 오버라이딩
# 부모 클래스 A
class A :
    pass
    # def speak(self) :
    #     return "a"

# 부모 클래스 B
class B : 
    def speak(self) :
        return "B"

class C(A, B) :
    pass    # A가 출력됨. A가 상속 순서에서 먼저 나오기 떄문
    # def speak(self) :
    #     return "C"

# 인스턴스 생성
# c 클래스에 정의된 speak()가 있으므로 A나 B에서 상속된 speak는 사용되지 않음. 즉, 자식 클래스에서 부모 메서드를 "덮어씀"
c = C()
print(c.speak())

print()
print()
print("------------------------")
print("--- 주문 프로그램")
print("------------------------")
print()

"""
# 클래스 나눈 기준
    - 기본 원칙 : 한 클래스는 하나의 역할만!

클래스이름          나눈 이유(역할)             책임
Menu                메뉴 정보만 관리            메뉴저장, 보여주기
Order               주문 정보만 관리            항목 추가, 총합 계싼, 주문내역 출력
Customer            손님의 행동 관리            주문 수행, Order 객체 보유


* 프로그램 전체의 흐름 요약
1. 고객 이름 입력
2. 메뉴 보여줌
3. 고객이 메뉴 선택 -> 주문에 추가
4. "종료" 입력 시 주문 완료
5. 주문 내역 및 총액 출력
"""

# 메뉴 정보를 관리하는 Menu 클래스
class Menu :
    def __init__(self):
        # 메뉴 항목을 딕셔너리로 저장 (메뉴이름: 가격)
        self.items = {
            "Burger" : 5000,
            "Fries" : 2000,
            "Soda" : 1000
        }

    # 메뉴를 출력해주는 함수
    def show_menu(self) :
        print("==메뉴판==")
        for name, price in self.items.items():
            # 각 메뉴 항목 출력
            print(f"{name}: {price}원")
        # 안내 문구 출력
        print("메뉴 이름을 입력해 주세요. (입력 : '종료' 시 주문 완료) \n")

# 주문 정보를 관리하는 Order 클래스
class Order :
    def __init__(self):
        # 장바구니 역할을 할 리스트 생성
        self.cart = []
    
    # 선택한 항목을 장바구니에 추가하는 함수
    def add_item(self, name, price) :
        self.cart.append((name, price))     # 튜플로 저장

    # 장바구니에 담긴 항목을 총 가격을 계산하는 함수
    def total(self) :
        return sum([price for name, price in self.cart])
        # for in 리스트 컴프리헨션 : 파이썬 문법
        # 짧고 간단하게 리스트를 만드는 방법


    # 현재 주문 내역을 출력하는 함수
    def show_order(self) :
        print("\n주문 내역 :")
        for name, price in self.cart :
            print(f"-{name} : {price}원")

# 고객을 나타내는 Customer 클래스
class Customer :
    def __init__(self, name):
        self.name = name        # 고객 이름 저장
        self.order = Order()    # 고객당 하나의 주문 객체 생성

    # 고객이 실제로 주문하는 함수
    def make_order(self, menu) :
        while True :
            # 메뉴판 보여주기
            menu.show_menu()
            # 사용자로부터 주문할 메뉴 입력 받기
            choice = input("주문할 메뉴 입력 : ")

            # '종료' 입력 시 반복 종료 -> 종료 끝
            if choice == "종료" :
                break

            # 올바른 메뉴를 입력했는지 확인
            if choice in menu.items : 
                # 주문 항목 추가
                self.order.add_item(choice, menu.items[choice])
                print(f"{self.name}님이 {choice}를 주문했습니다.\n")
            else :
                # 메뉴에 없는 항목 입력 시 안내
                print("메뉴에 없는 항목입니다. 다시 입력해주세요. \n")

# 프로그램 실행 부분

# Menu 객체 생성
menu = Menu()

# 사용자에게 이름을 입력받기
customer_name = input("고객의 이름을 입력하세요 >> ")

# Customer 객체 생성
customer = Customer(customer_name)

# 주문 시작 (메뉴 선택 반복)
customer.make_order(menu)

# 주문 내역 출력
customer.order.show_order()

# 총액 출력
print(f"총액: {customer.order.total()}원")

print()
print()
print("------------------------")
print("--- 프로그램 개발하기")
print("------------------------")
print()

"""
# 프로그램 개발하기

# 1. 프로그램 이름
    : 투두리스트 애플리케이션

# 2. 프로그램의 목적
    : 투두리스트를 목록 보기 및 투두 추가

# 4. 기능 설명 및 예시 흐름
    1. 사용자 이름 입력
    2. 할 일 추가
    3. 할 일 목록 보기
    4. 프로그램 종료

# 5. 클래스 설계
- Todo      :   투두에 대한 정보 저장     :   투두 완료처리, title 출력
- TodoList  :   투두리스트를 관리   :   할일 추가, 목록 출력
- TodoApp   :   앱 실행을 담당 : 사용자 이름 입력, 메뉴 인터페이스 출력
"""

class Todo :
    def __init__(self, title):
        self.title = title
        self.isCompleted = False

    def markDone(self) :
        self.isCompleted = True

    def __str__(self):
        status = "[✔️]" if self.isCompleted else "[ ]"
        return f"{status} {self.title}"

class TodoList :
    def __init__(self):
        self.todos = []

    def addTodo(self, title):
        self.todos.append(Todo(title))

    def showTodos(self) :
        if len(self.todos) == 0:
            print("할 일이 없습니다. 할 일을 추가해주세요.\n")
        else:
            print("== 할 일 목록 ==")
            for index, todo in enumerate(self.todos):
                print(f"{index + 1}. {todo}")
            print()

    def completeTask(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index].markDone()
            print(f"'{self.todos[index].title}' 완료 처리되었습니다.\n")
        else:
            print("유효하지 않은 번호입니다.\n")

class TodoApp : 
    def __init__(self):
        self.user = ""
        self.todoList = TodoList()

    def getUsername(self):
        while not len(self.user) > 0:
            self.user = input("이름을 입력하세요 : ")

    def showMenu(self):
        print()
        print(f"=== {self.user}'s 투두리스트 ===")
        print("1. 할 일 추가")
        print("2. 할 일 목록 보기")
        print("3. 종료")
        print()

    def run(self):
        self.getUsername()
    
        while len(self.user) > 0:
            self.showMenu()
            choice = input("메뉴를 선택하세요: ")
            print()

            if choice == "1":
                title = input("할 일을 입력하세요: ")
                self.todoList.addTodo(title)
                print("할 일이 추가되었습니다.\n")
            elif choice == "2":
                self.todoList.showTodos()
            elif choice == "3":
                print("프로그램을 종료합니다.")
                break
            else:
                print("올바른 메뉴 번호를 입력해주세요.\n")

app = TodoApp()
app.run()

print()
print()
print("------------------------ 끝")
print()
