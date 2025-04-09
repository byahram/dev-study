"""
2025.04.04 금
"""

print()
print()
print("------------------------")
print("--- 생성자")
print("------------------------")
print()

# EX1.
class Dog :
    # 클래스가 호출될 때 자동으로 실행된다.
    def __init__(self, name, age) :
        self.name = name
        self.age = age

myDog = Dog("Buddy", 3)
print(myDog.name)
print(myDog.age)

print()
print("------------------------")
print()

# EX2. 메서드로 변경
class Dog2 :
    def setInfo(self, name, age) :
        self.name = name
        self.age = age
        print(f"{self.name} / {self.age}")

myDog2 = Dog2()
myDog2.setInfo("Buddy", 3)

print()
print("------------------------")
print()

# EX3.
class Animal :
    # 생성자 생성. 매개변수는 sound
    def __init__(self, sound) :
        self.sound = sound

    # 메서드 cry
    def cry(self) :
        print(self.sound * 2)

cat = Animal("야옹")
cat.cry()
dog = Animal("멍멍")
dog.cry()

print()
print("------------------------")
print()

# EX4.
class Person :
    def __init__(self, name):
        self.name = name

    def introduce(self) :
        print(f"안녕하세요 저는 {self.name}입니다")

p1 = Person("민수")
p2 = Person("환희")
p3 = Person("아현")
p1.introduce()
p2.introduce()
p3.introduce()

print()
print("------------------------")
print()

# EX5.
class Rectangle :
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self) :
        return self.width * self.height
    
    def perimeter(self) :
        return (self.width + self.height) * 2
    
r = Rectangle(4, 5)
print("area :", r.area())
print("perimeter :", r.perimeter())

print()
print("------------------------")
print()

# EX6. 영화 정보 클래스 만들기
class Movie :
    def __init__(self, title, director, star = 0.0):
        # 이렇게 하면 필요할 떄만 넣고 안넣으면 자동 기본값으로 설정되니까 편하고 안전할 수 있다.
        self.title = title
        self.director = director
        self.star = star

    def showInfo(self) :
        print("제목 :", self.title)
        print("감독 :", self.director)
        print("평점 :", self.star)

    def isGood(self) :
        if self.star > 8.0 :
            print("추천 영화입니다!")
        else :
            print("그냥 그래요")

movie = Movie("인터스텔라", "크리스토퍼놀란", 9.5)
movie.showInfo()
movie.isGood()

movie2 = Movie("무제", "미상")
movie2.showInfo()
movie2.isGood()

print()
print()
print("------------------------")
print("--- 소멸자")
print("------------------------")
print()

# EX1.
class FileManager :
    def __init__(self):
        # 변수초기화, 호출될 때 가장 먼저 호출될 기능을 적어줌
        print("파일 열기 완료")

    def readFile(self) :
        print("파일 읽는 중")
    
    def __del__(self) :
        print("파일 닫기 완료")

# 객체 생성 (클래스를 변수에 할당)
file = FileManager()
file.readFile()

# 객체 삭제 -> 소멸자 자동 호출됨 -> 가비지 컬렉션 삭제
# 가비지 컬렉션 : 더이상 쓰이지 않는 개체를 자동으로 메모리에서 정리해주는 기능이다.
# 주기적으로 또는 조건에 따라 객체를 감시하다가 "이 객체 이제 안쓰네?" 하면서 메모리에서 제거한다.
del file

print()
print("------------------------")
print()

# EX2.
class UserSession :
    def __init__(self, name):
        self.name = name
        print(f"{self.name}님이 로그인 하셨습니다.")
    
    def showUser(self) :
        print(f"현재 사용자 : [{self.name}]")

    # 소멸자는 언제 생성(정의 되는가)?
    # 자동으로 만들어지지 않고, 필요할 때 우리가 정의하는 것것
    def __del__(self) :
        print(f"{self.name}님이 로그아웃 하셨습니다.")

    # 소멸자는 언제 실행이 되는가?
    # 소멸자는 객체가 더 이상 필요없어서 메모리에서 삭제될 때 자동으로 실행된다.

user1 = UserSession("지민")
user1.showUser()

del user1

print()
print()
print("------------------------")
print("--- 클래스 변수")
print("------------------------")
print()

# EX1.
class Student :
    count = 0       # 클래스 변수
    def __init__(self, name):
        self.name = name        # 인스턴스 변수
        # 클래스명.클래스변수 
        Student.count += 1

print()
print("------------------------")
print()

# EX2.
class Cup :
    total_cups = 0

    def __init__(self, color):
        self.color = color
        print(self.color)
        Cup.total_cups += 1

cup1 = Cup("빨강")
cup2 = Cup("파랑")
cup3 = Cup("초록")
print("총 만든 컵의 수 :", Cup.total_cups)

print()
print("------------------------")
print()

# EX3.
# 클래스 변수와 인스턴스 변수를 모두 사용하는 예제
class Student :
    total_students = 0      # 클래스변수 : 전체 학생 수 (모든 객체가 공유)

    def __init__(self, name, classNum):
        self.name = name        # 인스턴스 변수 : 학생 이름
        self.classNum = classNum        # 인스턴스 변수 : 반 번호
        Student.total_students += 1     # 학생이 생성될 때마다 클래스 변수 증가

    def introduce(self) :
        print(f"안녕하세요. 저는 {self.classNum}반의 {self.name}입니다.")

# 학생 객체 생성(클래스를 변수에 저장)
std1 = Student("영준", 1)
std2 = Student("대연", 2)
std3 = Student("서진", 3)
std1.introduce()
std2.introduce()
std3.introduce()

print()
print()
print("------------------------")
print("--- 클래스 상속")
print("------------------------")
print()

# EX1.
# 부모 클래스
class Animal :
    # 메서드 정의
    def speak(self) :
        print("동물이 소리를 냅니다.")

# 자식 클래스
class Dog(Animal) :
    # 메서드 정의
    def bark(self) :
        print("멍멍!")

# 객체 생성
dog = Dog()

# 자식 클래스에서 부모 클래스의 메서드 사용 가능!
# 부모 클래스에서 자식 클래스는 직접 쓸 수 없다.
dog.speak()
dog.bark()

print()
print("------------------------")
print()

# EX2.
class Device :
    def __init__(self, brand):
        self.brand = brand

    def turn_on(self) :
        print(f"{self.brand} 기기를 켭니다")

class Phone(Device) :
    def call(self) :
        print("전화 거는 중 ...")

phone = Phone("삼성")
phone.turn_on()
phone.call()

print()
print()
print("------------------------")
print("--- super()")
print("------------------------")
print()

# EX1.
# 부모 생성자 재사용
class Animal :
    # 생성자
    def __init__(self, name):
        self.name = name        # 인스턴스 변수
        print(f"{self.name}가 태어났어요")

# 자식 클래스
class Cat(Animal) :
    def __init__(self, name, breed):
        super().__init__(name)      # 부모의 생성자 호출
        self.breed = breed
        print(f"품종은 {self.breed} 입니다")

cat = Cat("초코", "푸들")

print()
print("------------------------")
print()

# EX2.
# 부모
class Employee :
    def __init__(self, name, department):
        self.name = name
        self.department = department
        print(f"{self.name}님은 {self.department} 부서에 배정되었습니다")

# 자식
class Developer(Employee) :
    def __init__(self, name, department, language):
        super().__init__(name, department)
        self.language = language
        print(f"사용 언어는 {self.language}입니다.")

dev = Developer("하은", "개발", "python")

print()
print()
print("------------------------ 끝")
print()
