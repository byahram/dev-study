"""
2025.04.03 목
"""

print()
print()
print("------------------------")
print("--- 콜백함수")
print("------------------------")
print()

"""
[콜백함수]

- 나중에 불려지는 함수
- 다른 함수에 인자로 전달되는 함수이고, (나중에 필요할 때) 호출되는 함수를 말한다.
- 쉽게 말하자면? "나 이 함수 나중에 불러줘" 하는거고 다른 함수에게 맡겨두는 함수이다.

[콜백 함수를 사용하는 이유]

- 코드의 재사용성과 유연성이 증가한다.
- 작업이 끝난 후 실행할 동작을 지정할 수 있다. (ex: 다운로드가 끝나면 자동으로 알림을 보내는 함수 실행)
- 조건에 따라 다른 함수를 실행할 수 있다. (예시: 성공 success(), 실패 fail())
"""

# EX1.
def greet(name) :
    print(f"Hello, {name}!")

# 콜백을 받는 함수
def run_callback(callback, value) :
    callback(value)

# 실행
run_callback(greet, "Alice")

print()
print("------------------------")
print()

# EX2.
def add(a, b) :
    print("덧셈결과 :", a + b)

# 콜백을 받는 함수
def calculate(callback, num1, num2) :       # callback: 나중에 실행할 함수
    callback(num1, num2)        # num1, num2: 그 함수에 전달할 숫자 값

# 실행
calculate(add, 2, 6)

print()
print("------------------------")
print()

# EX3.
def multiply(a, b) :
    print("곱셈 결과: ", a * b)

# 콜백을 받는 함수수
def calculate2(callback, n1, n2) :
    callback(n1, n2)

# 실행
calculate2(multiply, 4, 6)

print()
print("------------------------")
print()

# EX4.
def success() :
    print("작업이 성공했습니다!")

def fail() :
    print("작업이 실패했습니다.")

def check_result(is_ok, on_success, on_fail) :
    # is_ok : 성공 여부를 판단하는 True/False 값
    # on_success : 성공했을 때 실행할 콜백 함수
    # on_fail : 실패했을 때 실행할 콜백 함수
    if is_ok :
        on_success()
    else :
        on_fail()

# 성공한 경우
check_result(True, success, fail)

# 실패한 경우
check_result(False, success, fail)

print()
print("------------------------")
print()

# EX5.
def passed() :
    print("축하합니다!")

def failed() :
    print("아쉽지만 불합격입니다!")

def check_score(score, on_success, on_fail) :
    if score >= 60 :
        on_success()
    else :
        on_fail()

check_score(55, passed, failed)
check_score(75, passed, failed) 

print()
print("------------------------")
print()

# EX6. 날씨에 따라 콜백 함수 실행
def sunny() :
    print("햇살이 좋아요!")

def rainy() :
    print("비가 와요!")

def check_weather(weather, on_sunny, on_rainy) :
    if weather == "sun" :
        on_sunny()
    elif weather == "rain" :
        on_rainy()
    else :
        print("날씨 정보를 알 수 없습니다.")

check_weather("sun", sunny, rainy)
check_weather("snow", sunny, rainy)

print()
print("------------------------")
print()

# EX7. timer
import time
def timer(second, callback) :
    print("타이머가 시작됩니다.")
    print(second, "초 뒤 요청하신 함수가 호출됩니다.")

    # 매개변수 값(초) 만큼 코드 실행이 멈춘다.
    time.sleep(second)
    callback()  # 전달받은 함수 호출
    print("타이머가 종료됩니다.")

def callback() :
    print("요청하신 함수가 호출되었습니다.")

timer(3, callback)

print()
print()
print("------------------------")
print("--- 람다함수")
print("------------------------")
print()

'''
[람다함수]

- 짧고 간단한 함수를 빠르게 만들 수 있게 해주는 익명 함수이다.

[람다함수 문법]

lambda 매개변수 : 표현식
    - 매개변수 : 함수가 받을 값들
    - 표현식 : 함수가 리턴할 값(자동으로 리던됨, return안씀)

[삼항 연산자]

- 조건에 따라 값을 선택할 수 있는 표현식이다.
- 말 그대로 3개의 항으로 이루어져 있어서 삼항 연산자라고 한다.

[삼항 연산자 문법]

<참일 때 값> if <조건> else <거짓일 때 값>
- 조건이 참이면 앞쪽 값을 반환 거짓이라면 뒤쪽 값을 반환
'''

# EX1.
# 일반함수
def add(a, b) :
    return a + b
print(add(3, 5))

# 람다함수 정의
add_lambda = lambda a, b : a + b
print(add_lambda(1, 4))

# EX2. 문자열 길이 구하기
length = lambda str : len(str)
print(length("hello"))

print()
print("------------------------")
print()

# EX3. 짝수 홀수 판별하기
check_c = lambda x : "짝수" if x % 2 == 0 else "홀수"
print(check_c(8))

print()
print("------------------------")
print()

# EX4.
score = 85

# 삼항 연산자
result = "합격" if score >= 60 else "불합격"
print(result)

# 람다 함수
result_l = lambda score : "합격" if score >= 60 else "불합격"
print(result_l(85))

print()
print("------------------------")
print()

# EX5. 점수 기준으로 리스트 정렬
# 튜플(이름, 점수) 형태의 데이터가 들어 있다.
students = [("민수", 90), ("영희", 85), ("철수", 95)]
# key = 리스트 안의 값들을 어떤 기준으로 정렬할 지 알려주는 옵션이다.
# x[1] = 튜플의 두번째 값(점수)를 기준으로 정렬을 해준다.
students.sort(key = lambda x : x[1])
print(students)

print()
print("------------------------")
print()

# EX6. 나이를 기준으로 내림차순 정렬하기
people = [("지훈", 25), ("수민", 20), ("현우", 30)]
people.sort(key = lambda age : age[1], reverse=True)
print(people)

print()
print("------------------------")
print()

# EX7.
print("# EX7. 단어의 길이를 기준으로 정렬")

words = ["banana", "apple", "kiwi"]
words.sort(key = len)
print(words)

print()
print()
print("------------------------")
print("--- 사용자 입력")
print("------------------------")
print()

'''
* 사용자에게 입력을 받는 방법 input()함수를 사용한다.

[문법]

변수 = input("값을 넣어주세요")
    - 값을 넣어주세요 = 입력 안내 문구
    - 사용자로부터 문자열 형태의 입력을 받는다.

[주의]

- int(input()).split() ->  사용 불가능하다.
- int()는 숫자 하나만 받을 수 있기 때문이다.
'''

# EX1.
# 문자열 입력받기, string
name = input("이름을 입력해주세요 : ")
print("안녕하세요, ", name, "님")

# 정수 입력받기, int
age = int(input("나이를 입력하세요 : "))
print("내년에는", age + 1, "살이 됩니다")

# 실수 입력받기, float
num = float(input("실수를 입력하세요 : "))
print(num)

print()
print("------------------------")
print()

# EX2.
# .split() : 여러 개의 값을 나눠서 입력받을 때 사용
x, y = input("두 수를 입력하세요. (띄어쓰기로 구분) : ").split()
x = int(x)
y = int(y)
print("합 = ", x + y)

print()
print("------------------------")
print()

# EX3.
a, b = input("두 수를 입력하세요. (띄어쓰기로 구분) : ").split()
a = int(a)
b = int(b)
print("합 = ", a + b)

print()
print("------------------------")
print()

# EX4.
a, b = input("두 수를 입력하세요. (띄어쓰기로 구분) : ").split()
a = int(a)
b = int(b)
    
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

print()
print("------------------------")
print()

# EX5.
a, b = map(int, input("두 정수를 입력하세요 : ").split())
print("합 : ", a + b)

print()
print("------------------------")
print()

# EX6.
n1, n2 = map(float, input("두 실수를 입력하세요 : ").split())
print("합 : ", n1 + n2)

print()
print()
print("------------------------")
print("--- 클래스")
print("------------------------")
print()

'''
[객체 지향 프로그래밍]
- 사람, 강아지, 자동차, 게임 캐릭터등 현실의 모든것을 "객체"라고 한다.
- 그 객체들이 가진 속성(변수)와 행동(함수)을 정의해서 코드를 짜는 방식이다.

[속성 (Attribute)]
- 객체가 가지고 있는 데이터(정보)를 의미한다.
- 즉, 객체의 특징이나 상태를 나타내는 변수이다.

[메서드 (Method)]
- 객체가 할 수 잇는 동작(기능)을 의미한다.
- 즉, 클래스 안에 정의된 함수를 의미한다.

[클래스]
- 실제 동작하는 객체를 만들기 전에 어떤 속성과 행동을 가질지 미리 정의해 두는 것이다.

[비교]
- 클래스 : 객체를 만들기 위한 설계도
- 객체 : 클래스를 바탕으로 만들어진 실제 사용 가능한 존재
- 속성 : 객체가 가지고 있는 정보/데이터
- 메서드 : 객체가 할 수 있는 행동/기능

[실생활 예제]
- 클래스 : 레고 설계도 
- 객체 : 실제 조립된 레고
- 속성 : 색상, 무기, 모델
- 메서드 : 공격하기, 날기, 변신하기

[객체 지향 프로그래밍의 4가지 특징]
1. 캡슐화 : 속성과 메서드를 하나로 묶고, 외부에서 직접 접근하지 못하게 보호하는 것
2. 상속 : 기존 클래스의 속성과 메서드를 물려받아 새로운 클래스를 만드는것
3. 다(多)형(形)성 : 같은 이름의 메서드가 상황에 따라 다르게 동작할 수 있는 성질
4. 추상화 : 복잡한 내부 동작은 숨기고, 필요한 기능만 보여주는 것

[클래스 문법]
class 클래스명 :
    클래스 변수	
    생성자
    메서드

* 클래스 외부에 있으면 함수 : 독립적으로 정의된 동작을 수행하는 코드 블록 
* 클래스 내부에 있으면 메서드 : 클래스에 소속된 함수. 객체와 함께 동작한다.

[메서드 문법]
class 클래스 이름 : 
    def 메서드이름(self, 매개벼수1, 매갠변수) :
    실행할 코드

* self 
    - 항상 첫 번째 매개변수로 들어가야만 한다.
    - 메서드가 호출된 그 객체 자신을 가리킨다.
    - 객체의 속성이나 다른 메서드에 접근할 수 있다.
'''

# EX1.
# Person 클래스 정의
class Person :
    # 메서드 정의 
    def introduce(self) :
        print("안녕하세요!")

minsu = Person()
minsu.introduce()

print()
print("------------------------")
print()

# EX2.
class Animal :
    # 메서드 정의
    def sound(self) :
        print("동물이 소리를 냅니다.")

cat = Animal()
cat.sound()

print()
print("------------------------")
print()

# EX3. 메서드에 매개변수 추가
class Person2 :
    def introduce(self, name) :
        print(f"안녕하세요 {name}입니다.")

jihoon = Person2()
jihoon.introduce("민수")

print()
print("------------------------")
print()

# EX4.
class Animal2 : 
    def cry(self, sound) :
        print(f"저의 울음 소리는 {sound}입니다")

cat = Animal2().cry("야옹")
dog = Animal2().cry("멍멍")

print()
print("------------------------")
print()

# EX5.
class Book :
    def show_title(self, title) :
        self.title = title
        print(f"책 제목은 {self.title}입니다")

book = Book()
book.show_title("파이썬 입문")

# 클래스 안의 메서드가 자기 객체의 데이터를 사용할 때 쓰는 말이다.

print()
print("------------------------")
print()

# EX6.
class Lamp :
    def turn_on(self, color) :
        self.color = color          # self.속성 = "그 객체의 정보를 담고 있는 변수(상자)"
        print(f"{self.color} 램프가 켜졌습니다.")
lamp = Lamp()
lamp.turn_on("노란색")

print()
print("------------------------")
print()

# EX7.
class Student :
    def introduce(self, name, age) :
        self.name = name
        self.age = age
        print(f"저는 {self.name}이고, {self.age}살 입니다.")

me = Student()
me.introduce("지훈", 15)

print()
print("------------------------")
print()

# EX8.
class Box :
    def show_items(self, items) :
        self.items = items
        print("상자 안에 있는 물건 : ")
        for item in self.items :
            print("-", item)

box = Box()
box.show_items(["연필", "지우개", "자"])

print()
print()
print("------------------------ 끝")
print()
