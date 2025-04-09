"""
2025.04.03 목
"""

print()
print()
print("------------------------")
print("--- 콜백함수")
print("------------------------")
print()

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
