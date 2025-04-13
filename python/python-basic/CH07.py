"""
2025.04.01 화
"""

print()
print()
print("------------------------")
print("--- 함수")
print("------------------------")
print()

'''
[함수(Function)]

- 특정 작업을 수행하는 코드 묶음
- 어떤 입력값을 받아서 특정 작업을 수행하고, 결과값을 반환하는 코드의 묶음이다.
- 필요할 때 마다 재사용 할 수 있고, 코드가 간결하고 구조화 된다.
- 단독으로 사용되고 def 키워드로 정의한다.

[특징]

- 단독으로 사용된다.
- 재사용이 가능해서 코드의 중복을 줄여준다.
- def 키워드로 정의한다.

[문법]

def 함수 이름() :
    코드 1
    코드 2

def  함수이름(매개변수1, 매개변수 2, ...) :
    실행할 코드
    return 반환값 (선택사항)

[콜론]

: 함수 정의 후 코드 블록의 시작을 나타낸다.
- 함수의 코드 블록은 : (콜론) 다음에 4칸(tab) 들여쓰기 해서 시작해야 한다.
- 만약에 들여쓰기 없이 def 키워드와 같은 세로줄에서 코드를 시작하면 자동으로 함수가 종료된 것으로 간주한다.
'''

'''
[메서드 (Method)]

- 객체에 종속된 함수로, 클래스 내부에 정의된 함수이다.

[특징]

- 반드시 클래스 안에서 정의된다.
- 특정 객체를 통해 호출된다
- 객체의 데이터(속성)에 접근하거나 조작할 수 있다.
'''

# EX1.
def hello() :
    print("안녕하세요")
    print("제 이름은 파이썬입니다.")

hello()
print()
hello()

print()
print()
print("------------------------")
print("--- 지역변수")
print("------------------------")
print()

'''
[지역변수(Local Variable)]

- 함수에서만 쓸 수 있다.
- 정의 : 함수 내에서 선언된 변수는 그 함수 안에서만 사용할 수 있다.
'''

# EX1.
def greet() :
    message = "hello"       # 지역변수
    print(message)
greet()

print()
print("------------------------")
print()

# EX2.
def show_score() :
    score = 95
    print(score)
show_score()

print()
print()
print("------------------------")
print("--- 전역변수")
print("------------------------")
print()

'''
[전역 변수 (Global Variable)]

- 전체적으로 쓸 수 있다.
- 정의 함수 밖에서 선언된 변수는 프로그램 전체에서 사용 가능
'''

# EX0.
score = 200  # 전역 변수

def game_round():
    score = 50  # 지역 변수
    score += 30
    print("1라운드 점수:", score)

def bonus_round():
    global score
    score += 20
    print("보너스 라운드 후 점수:", score)

game_round()
bonus_round()
print("최종 점수:", score)

print()
print("------------------------")
print()

# EX1.
score = 0
def add_score() :
    # 만약 global을 삭제한다면? : 함수 안에 있는 score를 지역변수로 생각하는데, 아직 값이 없어서 오류가 난다.
    global score    # 함수 안에서 전역변수를 사용하겠다고 선언
    score += 10
    print("함수 안 점수 : ", score)

add_score()
print("함수 밖 점수 : ", score)

print()
print("------------------------")
print()

# EX2. 게임 점수 시스템
score = 100
def play_game() :
    scoreNum = 0        # 지역 변수 
    print("게임 시작 ", scoreNum)
    scoreNum += 50
    print("게임 시작 ", scoreNum)

play_game()

print()
print("------------------------")
print()

# EX3. 게임 점수 시스템
score = 100
def playing() :
    global score
    score = 0
    print("게임 시작! ", score)
    score += 50
    print("아이템 획득! ", score)
    print("게임 시작! ", score)
    
playing()

print()
print()
print("------------------------")
print("--- 매개변수")
print("------------------------")
print()

'''
[매개변수(파라미터, parameter)]

- 함수가 호출 될 때 외부로 부터 값을 전달받기 위한 변수이다.
- 함수는 이 매개변수를 이용하여 전달받은 값을 처리한다.

[문법]

def 함수이름( 매개변수1, 매개변수2,.....) :
    코드1
    코드2.....

[함수를 호출할 때, 매개변수를 전달하는 방법]

- 함수이름(매개변수1, 매개변수2)
'''

# EX1. 매개변수
def say_hello(name) :
    print("안녕, ", name)

# 인자 : 함수를 호출할 때 전달하는 실제 값
say_hello("민지야")         # 매개변수에는 name = "민지"
say_hello("민주")           # 매개변수에는 name = "민주"

print()
print("------------------------")
print()

# EX2. 두 수 더하기
def add(a, b) :
    print("두수의 합 = ", a + b)

add(10, 15)

print()
print("------------------------")
print()

# EX3. 매개변수
def hello(name) :
    print("안녕하세요!")
    print("제 이름은 " + name + "입니다")
    print("만나서 반갑습니다.")

hello("김송아")

print()
print("------------------------")
print()

# EX4.
def multiply(num1, num2) :      # 매개변수(=parameter)
    print(num1 * num2)

multiply(3, 4)      # 인자

print()
print("------------------------")
print()

# EX5.
def introduce(name, age) :
    print("안녕하세요, 제 이름은 ", name, "입니다")
    print("제 나이는 ",  age, "입니다")
    print("잘 부탁드립니다.")

introduce("제니", 20)

print()
print()
print("------------------------")
print("--- return")
print("------------------------")
print()

'''
[return]

- 함수의 결과값을 함수 바깥으로 돌려주는 역할을 한다.
- 함수 안에서 어떤 값을 계산하고, 그 값을 밖에서 쓰고 싶을 때 꼭 필요하다.

    기능			특징
  print()       값을 화면에 보여줌      : 결과를 "출력"만 한다. 
  return        값을 함수 밖으로 전달   : 결과를 변수에 저장하거나, 다른 계산에 사용 가능

[문법]

def 함수이름 (매개변수) :
    코드1
    return 함수 밖으로 전달하고 싶은 값

* return은 함수 내에 있어야 한다.
'''

# EX1.
def add2(a, b) :
    print(a + b)
add2(3, 5)

# return을 쓰는 경우
def add3(a, b) :
    return a + b            # 함수 밖으로 더한 값을 내보내고 싶다.

result = add3(3, 5)
print(result) 

print()
print("------------------------")
print()

# EX2.
def multiply2(x, y) :
    return x * y

result = multiply2(4, 6)
print(result)

print()
print()
print("---------------------------")
print("--- 매개변수의 경우의 수")
print("---------------------------")
print()

'''
[매개변수의 경우의 수]

1. 경우의 수 : 매개변수 x, return x
    - 특징 : 외부에서 값도 안받고, 값을 돌려주지도 않는다. 그냥 실행만 하는 함수다.

            def hello() :
                print("안녕하세요")
            hello() 

2. 경우의 수 : 매개변수 o,  return x
    - 특징 : 외부에서 값을 받기만 한다.  계산 결과는 print()로 출력만 한다.

            def greet(name)
                print(name)
            greet("슬")

3. 경우의 수 : 매개변수 x, return o
    - 특징 : 외부 값을 받지 않고, 내부에서 계산한 결과를 돌려줌

            def get_number() :
                return 42
            num = get_number()
            print(num)

4. 경우의 수 : 매개변수 o, return o
    - 특징 : 외부값을 받고 게산한 결과를 함수 밖으로 돌려줌. 실무에서 자주 쓰는 형태

            def add(a, b)
                return a + b

            result = add(3,5)
            print(result)
'''

# EX1.
def get_number() :
    return 42

num = get_number()
print(num)

print()
print("------------------------")
print()

# EX2.
def add5(a, b) :
    return a + b

result = add5(3,5)
print(result)

print()
print("------------------------")
print()

# EX3.
def plus(a, b) :
    return a + b

sum = plus(5, 10)
print(sum)

print()
print("------------------------")
print()

# EX4.
def plus_add(a, b) :
    sum = a + b
    if sum % 2 == 0 :
        return sum
    else :
        return sum + 1

print(plus_add(5, 10))
print(plus_add(6, 10))   

print()
print("------------------------")
print()

# EX5. 세 수 중 가장 큰 수를 반환하기
# max() 함수는 여러 값 중에서 가장 큰 값을 찾아서 돌려주는 함수이다.
# min() 함수는 가장 작은 값을 돌려주는 함수이다.

def find_max(a, b, c) :
    # max = a
    # if b > max :
    #     return b
    # elif c > max :
    #     return c
    # else :
    #     return a
    return max(a, b, c)

print(find_max(3, 7, 5))
print(find_max(10, 2, 8))

print()
print("------------------------")
print()

# EX6. 리스트에서 최댓값 찾기
scores = [82, 91, 77, 88]
print(max(scores))
print(max("a", "z", "c"))       # 아스키코드표에 의해서 결과가 나온다. a:97, z: 122

print()
print("------------------------")
print()

# EX7.
def check_seven(num) :
    if num % 7 == 0 :
        return True
    else :
        return False
    
print(check_seven(3))

print()
print()
print("------------------------")
print("--- 팩토리얼")
print("------------------------")
print()

'''
[팩토리얼]

- 어떤 자연수 n이 있을 때, 그 수부터 1까지 모든 자연수를 곱한 값을 팩토리얼 이라고 한다.
- 기호는 !를 사용하여 표현한다.

[예시]

3! = 3*2*1 
4! = 4*3*2*1
0! = 1 (정의)

[공식]

n! = n * (n-1) * (n-2)* ... * 2 *1
'''

# EX1.
def factorial(num) :
    sum = 1     # 지역 변수

    # range(5)는 [0, 1, 2, 3, 4]
    for n in range(num) :
        sum = sum * (n+1)       # [1, 2, 3, 4, 5]
        # sum = sum * (0 + 1) = 1
        # sum = sum * (1 + 1) = 1 * 2 = 2
        # sum = sum * (2 + 1) = 2 * 3 = 6
        # sum = sum * (3 + 1) = 6 * 4 = 24
        # sum = sum * (4 + 1) = 24 * 5 = 120
    return sum

print(factorial(5))

print()
print()
print("------------------------")
print("--- 심화 예제")
print("------------------------")
print()

# EX1. 리스트로 평균 반환하기
def cal_average(scores) :
    sum = 0

    for score in scores :
        sum += score

    average = sum / len(scores)
    return average

average1 = cal_average([55, 70, 100])
print(average1)

print()
print("------------------------")
print()

# EX2. 리스트 숫자 두 배로 출력하기
def double_numbers(numbers) :
    new_list = []
    for num in numbers :
        new_list.append(num * 2)
    return new_list

list = double_numbers([3, 5, 7])
print(list)

print()
print("------------------------")
print()

# EX3. 리스트에서 최댓값 반환하기
def find_max(numbers) :
    max_value = numbers[0]

    for n in numbers :
        if n > max_value :
            max_value = n

    return max_value

max1 = find_max([45, 89, 72, 33, 100])
print(max1)

print()
print()
print("------------------------")
print("--- 파일 관련 함수")
print("------------------------")
print()

'''
[파일 입출력]

1. 파일 열기
    - 파이썬에서 파일을 열기 위해서는  open()이라는 함수를 사용한다.
    - 문법 : open(파일명, 모드)

    모드  |		기능		 |        설명
    r	 |	읽기기능(기본값)  |	  파일을 읽기 전용으로 연다.
    w	 |	쓰기 모드		 |   파일에 새로운 내요을 쓰기 위해 연다. 기존 파일의 내용은 덮어쓰여 진다.
    a 	 |	추가 모드		 |   파일에 새로운 내용을 추가하기 위해 연다. 기존 파일의 내용은  유지

2. 파일 읽기
    - 변수명.read() : 파일 ㅣ전체 내용 읽기
    - 변수명.readline() : 파일 한 줄씩 읽기
    - 변수명.readlines() : 파일의 모든 줄을 읽어 리스트로 반환한다.

3. 파일 쓰기 : write()

4. 파일 닫기 : 변수명.close()
'''

import os
print(os.getcwd())

# 파일 읽기
file = open("./python/python-basic-1/ch07.txt", "r", encoding="utf-8")
all = file.read()
print(all)

# 파일 쓰기
file = open("./python/python-basic-1/ch07.txt", "w")
file.write("ABABCABC")

# 파일 닫기
file = open("./python/python-basic-1/ch07.txt", "r")
all = file.read()
print(all)
file.close()        # 운영체제에서 파일을 닫는다(시각적으로 변화하는 것은 아님)

print()
print()
print("------------------------")
print("--- 콜백함수")
print("------------------------")
print()

"""
- 나중에 불려지는 함수
- 다른 함수에 인자로 전달되는 함수이고, (나중에 필요할 때) 호출되는 함수를 말한다.
- 쉽게 말하자면? "나 이 함수 나중에 불러줘" 하는거고 다른 함수에게 맡겨두는 함수이다.
"""

print()
print()
print("------------------------ 끝")
print()
