print()

#################################
# 4. print() 함수 - 기본적인 입출력
#################################
print("입력해주세요")
print('hello')
print()

print(123)
print(1+1)
print(3.14)
print(1+3j)
print()

###################
# 6. 문자열과 따옴표
###################
print("what's your name")
print('what\'s your name')
print()

##########################################
# 7. print() 함수에서 이스케이프 코드 활용하기
##########################################
print("이스케이프 코드 1. \n 문자열 줄바꿈")
print("이스케이프 코드 2. \t 문자열 탭 간격")
print("이스케이프 코드 3. \\ 역슬러쉬를 그대로 표현")
print("이스케이프 코드 4. \' 작은따옴표 그대로 표현")
print("이스케이프 코드 5. \" 큰 따옴표 그대로 표현")
print("이스케이프 코드 6. \r 캐리지 반환(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)")
print("이스케이프 코드 7. \f 폼 피드(줄 바꿈, 현재 커서에서 다음 줄로 이동)")
print("이스케이프 코드 8. \a 벨 소리")
print("이스케이프 코드 9. \b 백 스페이스")
print("이스케이프 코드 10. \000 Null")
print()

###################
# 8. 문자열 연산하기
###################
print("더하면" + "붙어요")
print("안녕하세요" * 10)
print()

print("=" * 50)
print("내손으로" + "배우는" + "파이썬")
print("=" * 50)
print()

###############################
# 9. print() 함수의 옵션 사용하기
###############################

# sep
print("you know what I mean?")                      # 1개의 문자
print("you" + "know" + "what" + "I" + "mean?")      # 1개의 문자
print("you", "know", "what", "I", "mean?")          # 5개의 문자
print()

print("you", "know", "what", "I", "mean?", sep="...")
print("개미는", "오늘도", "열심히 일을하네", sep="뚠뚠")
print("010", "000", "0000", sep="-")
print()

# end
print("hello", end="\n")        # default
print("hello", end="python")
print("0과 1로만 구성된 열차는? ", end="정답은 ")
print("남행열차")
print()

# 이스케이프 코드 비활성화
print(r"안녕하세요 \n 반갑습니다")
print()

print("제가 1994년에 la에 있었을때.... " \
"la 다저스 시절이 가장 먼저 생각")
print("제가 1994년에 la에 있었을때....  \
la 다저스 시절이 가장 먼저 생각")
print()

###############
# 11. 산술연산자
###############

# ** 거듭제곱 | // 나눈 몫 | % 나눈 나머지
# 괄호 > 나눗셈 및 곱셈 > 덧셈 및 뺄셈

print(3+1)
print(10-1)
print(-12-1)
print(2*4)
print(15/2)
print(15//2)
print(15%2)
print()

print(3.5+1.3)
print(1.4-0.1)
print()

print(3.7 / 1.547)
print(1.64 // 0.54)
print()

###############
# 12. 변수 개요
###############

# 변수 : 값이 변하지 않은 임의의 값, 여러 데이터를 담을 컨테이너

age = 29
name = "홍길동"
print(age, name)

age = 29 + 1
name = "홍길동 2"
print(age, name)
print()

#################
# 13. 변수명명규칙
#################

'''
1. 변수의 이름은 알파벳 또는 언더바 "_"로 시작할 수 있다.
2. 소문자, 대문자를 서로 다른 문자로 인식한다.
3. 숫자 사용이 가능하다. (하지만 첫번째로 올 수 없다.)
4. 공백, 특수문, 키워드(예약어)는 변수명으로 사용할 수 없다.
'''

'''
1. 카멜 표기법 : camelCase, variableN, thisIsCamelCase
2. 스네이크 표기법 : snake_case, variable_n, this_is_camel_case
2. 파스칼 표기법 : PascalCase, VariableN, ThisIsPascalCase
'''

####################################
# 14. 변수에 들어가는 다양한 데이터 타입
####################################

'''
1. integer : 정수형
2. float : 실수형
3. string : 문자형
4. boolean : 논리형
'''

age = 32
name = "헨리"
height = 185.4
marital_status = False

print(age, name, height, marital_status)
print(type(age), type(name), type(height), type(marital_status))
print()

variable = 100
print(variable)
print(id(variable))     # 메모리에 저장되어 있는 변수의 물리적인 위치
print()

# int() float() str() bool()
age = 29
height = 185.8
marital_status = False
print(int(height))
print(int(marital_status))
print(float(age))
print()

##################
# 15. 기본적인 입력
##################

'''
input()
변수명 = input(출력 유도 문구)
input으로 입력되는 모든 것은 문자열
'''

name = input("이름을 입력해주세요 >> \n")
print(name)

num = int(input("숫자를 입력해주세요 >> \n"))
print(num)

num = input("숫자를 입력해주세요 >> \n")
print(int(num))

##########################
# 16. 숫자 데이터 들여다보기
##########################

num = 1_000_000
num2 = 0.5
num3 = 1000000
print(num + num2)
print(num == num3)
print()

num4 = 4
fnum = 4.2
result = num4 + fnum
print(result)
print(type(result))
print()

############################
# 17. 문자열 데이터 들여다보기
############################

str = "hello, python"

print(str[0])
print(str[4])
print()

print(len(str))         # 길이
print(str.find(","))    # 인덱스
print()

print('h' in str)
print('h' not in str)
print()

print(str.upper())
print(str.lower())
print()

# 문자열 슬라이싱
print(str[2:5])         # [x:y] x 인덱스부터 y 인덱스 직전까지
print()

# 문자열 바꾸기
print(str.replace("hello", "bye"))
print(str.replace("python", "java"))
print()

# 문자열 쪼개기
str = "hello, python"
print(str.split())

text = "h.e.l.l.o.p.y.t.h.o.n"
print(text.split("."))
print(text.split(".", 4))
print()

##########################
# 18. 논리 데이터 들여다보기
##########################
print(1 == 1)
print(1 != 2)
print(1 <= 1)
print()

num = 200
print(isinstance(num, int))

num = "200"
print(isinstance(num, int))
print()

print(True and True)
print(True and False)
print(False and False)
print()

print(True or True)
print(True or False)
print(False or False)
print()

print(not True)
print(not False)
print()

###########################################
# 19. 문자열에 변수 삽입 방법 1 - 문자열 포맷팅
###########################################

# format() 

age = 20
intro = "제 이름은 서재필입니다. 나이는 {}살입니다."
print(intro.format(age))
print()

wage2020 = 8590
wage2021 = 8720
result = wage2021 - wage2020
print("2020년 최저임금은 {}원입니다.".format(wage2020))
print("2021년 최저임금은 {}원입니다.".format(wage2021))
print("두 해의 차이는 총 {}원입니다.".format(result))
print()

print("""2020년 최저임금은 {}원입니다.
2021년 최저임금은 {}원입니다.
2021년 최저임금은 2020년보다 {}원 상승했습니다.""".format(wage2020, wage2021, result))
print()

print("""2020년 최저임금은 {2}원입니다.
2021년 최저임금은 {1}원입니다.
2021년 최저임금은 2020년보다 {0}원 상승했습니다.""".format(result, wage2021, wage2020))
print()

item = "마우스"
quantity = 12
item_price = 59_000
total_price = quantity * item_price
myorder = "{2}원인 {0}을 {1}개에 대한 총 금액은 {3}원입니다."
print(myorder.format(item, quantity, item_price, total_price))
print()

name = "산악회"
age = 57
print("그의 이름은 {0}입니다. {0}의 나이는 {1}세 입니다.".format(name, age))
print()

my_car = "제 차는 {car}이고 색은 {color}입니다."
print(my_car.format(car = "트럭", color = "노란색"))
print()

pi = 3.141592653589793
txt = "원주율은 원 둘레와 지름이 비이고 값은 {}입니다."
print(txt.format(pi))
print()

pi = 3.141592653589793
txt = "원주율은 원 둘레와 지름이 비이고 값은 {:.2f}입니다."
print(txt.format(pi))
print()

print("hello {:<10} world".format(23))      # 공백
print("text:{0:>20}".format("샘플"))
print("{0:<10}".format("LEFT"))
print("{0:_^10}".format("CENTER"))
print()

#######################################################
# 20. 문자열에 변수 삽입 방법 2 - 문자열 포맷팅 서식 지정자 %
#######################################################
height = 185
print("제 키는 %d입니다." % height)
print("제 키는 %f입니다." % height)
print()

print("정수형 데이터는 %d, 문자형 데이터는 %s, 실수형 데이터는 %f" % (100, "문자열", 0.54))
print("score: %10d" % 100)
print("score: %010d" % 100)
print()

a = 0.43
print("%f입니다." % a)
print("%.3f입니다." % a)
print("%.1f입니다." % a)
print()

####################################
# 21. 자료구조형 데이터 타입 1 - 리스트
####################################

'''
* 여러 개의 값을 저장하는 데이터 타입
1. list [] : 리스트는 순서가 있고 / 수정 가능한 컬렉션이고 / 중복을 허용한다.
2. tuple () : 튜플은 순서가 있고 / 수정 불가능한 컬렉션이고 / 중복을 허용한다.
3. dictionary {} : 순서가 없고 / 수정 가능한 컬렉션이고 / 중복을 허용하지 않는다.
4. set {} : 순서가 없고 / 인덱스를 사용하지 않는다 / 중복을 허용하지 않는다.
'''

attendance = ["성화섭", "송유한", "문수민"]
print(attendance)
print(attendance[2])
print(attendance[-3])
print()

name_list = ["성화섭", "송유한", "문수민", "임병직"]
print(len(name_list))
print(type(name_list))
print(name_list[1:3])
print()

food_list = ["피자", "치킨", "깐풍기", "삼겹살", "항정살"]
food_list[1] = "치킨22"         # 리스트 값 변경하기  
print(food_list)
food_list.insert(0, "밥")       # 리스트 값 해당 인덱스에 추가하기     
print(food_list)
food_list.append("갈비")        # 리스트 값 해당 인덱스에 추가하기   
print(food_list)    
food_list.pop(2)                # 리스트 값 삭제하기
print(food_list)                
food_list.pop(2)                # 리스트 값 삭제하기
print(food_list)          
del food_list    
print()

animal = ["토끼", "호랑이", "개", "고양이"]
bird = ["독수리", "부엉이", "참새"]
animal.extend(bird)
print(animal)
print(animal + bird)
animal.append(bird)
print(animal[7])
print()

eng = ["b", "a", "d", "c"]
num = [4, 5, 600, -4, 0]
eng.sort()
num.sort()
eng.sort()
num.sort()
print()

####################################
# 22. 자료구조형 데이터 타입 2 - 튜플
####################################

name_tuple = ("홍길동", "이순신", "세종대왕", "유관순")
print(name_tuple)
print(type(name_tuple))
print()

num_tuple =  (1, 2, 3, 4, 5)
name_tuple = ("홍길동", "이순신", "세종대왕", "유관순")
mix_tuple = (1, "text", 3.14, True)

print(num_tuple)
print(name_tuple)
print(mix_tuple)
print()

num_tuple = (5, 4, 3, 2, 1)
# num_tuple.sort()           # 사용 불가
# num_tuple.append(6)       # 사용 불가
print(num_tuple)
print()

import sys

num_tuple = (1, 2, 3, 4, 5)
num_list = [1, 2, 3, 4, 5]
print(len(num_tuple), len(num_list))
print("튜플 용량", sys.getsizeof(num_tuple))
print("리스트 용량", sys.getsizeof(num_list))
print()

rainbow = ("빨", "주", "노", "초", "파", "남", "보")
print(rainbow[0])
print(rainbow[2:])
print(rainbow[-3])
print("빨" in rainbow)
print(type("빨" in rainbow))
print()

rainbow2 = ("빨", "주", "검")
print(rainbow2)

list_rainbow = list(rainbow2)
print(list_rainbow)

list_rainbow[2] = "노"
list_rainbow = tuple(rainbow2)
print(list_rainbow)
print()

t1 = (1, 2, 3)
t2 = ("하나", "둘", "셋")
print(t1 + t2)
print(t1 * 3)
print()

####################################
# 23. 자료구조형 데이터 타입 3 - 집합
####################################

set1 = {1, 2, 3, 4}
print(set1)
print(1 in set1)
print(type(set1))
print()

set2 = {1, 2, 3}
set2.add(4)
print(set2)
set2.update([4, 5, 6, 7, 8])
print(set2)
print()

s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = s1.union(s2)
print(s3)
print()

s11 = {1, 2, 3, 4}
s11.discard(3)
print(s11)
s11.discard(5)
print(s11)
print()

s22 = {1, 2, 3, 4}
print(s22)
s22.remove(3)
print(s22)
# s22.remove(5)       # 에러
# print(s22)
print()

x = {1, 2, 4, 8}
y = {1, 2, 4, 8, 16}
z = x.intersection(y)
print(z)
print()

######################################
# 24. 자료구조형 데이터 타입 4 - 딕셔너리
######################################

sd = {
    "name" : "윤태훈", 
    "직업" : "편집자",
    "나이" : 32,
}
print(sd)
print(type(sd))
print()

person = {
    "이름" : "노동혁",
    "나이" : 17,
    "결혼" : False,
    "취미" : {"탁구", "음악감상", "게임"}
}
print(person)

person["신장"] = 175.8
person["주소"] = "서울 강남구"
print(person)
print()

print(person.keys())
print(person.values())
print(person.items())
print()

person = {
    "김주환" : {"결혼" : False, "나이": 29},
    "김민수" : {"결혼" : True, "나이": 34},
    "김은수" : {"결혼" : True, "나이": 37},
}
print(person)
print()

p1 = {"이름" : "김주환", "나이" : 29}
p2 = {"이름" : "김민수", "나이" : 34}
p3 = {"이름" : "김은수", "나이" : 37}
pp = {
    "첫째" : p1,
    "둘째" : p2,
    "셋째" : p3
}
print(pp)
print()

###################
# 25. 제어문 - 조건
###################
my_age = 7
if my_age < 20 :
    print("미성년자 입니다.")
    if my_age < 8 :
        print("8세 이하입니다.")
print()

height = 175
if height <= height <= 165 :
    print("s사이즈를 입으세요.")
elif 166 <= height <= 175 :
    print("m사이즈를 입으세요.")
else :
    print("l사이즈를 입으세요.")
print()

lens = True
glasses = False

if lens or glasses :
    print("시력이 좋지 않습니다.")
else :
    print("시력이 좋습니다")
print()

animal_list = ["개", "고양이", "토끼", "돼지", "하마"]
animal = "독수리"
if animal in animal_list :
    print("{}는 리스트에 있습니다.".format(animal))
else :
    print("{}는 리스트에 없습니다.".format(animal))
print()

###################
# 26. 제어문 - 반복
###################

i = 1
while i < 10 :
    print("{}X{}={}".format(2, i, 2*i))
    i += 1
print()

i = 0
while i < 10 :
    i += 1
    if i == 3 :
        continue
    print(i,"번째 출력")
print()

attend = ["김순희" , "김영철", "최민규", "조현호", "민지수"]
index = 0
while index < len(attend) :
    print(attend[index])
    index += 1
print()

for name in attend :
    print(name)
print()

for x in "python" :
    print(x)
print()


attend = ["김순희" , "김영철", "최민규", "조현호", "민지수"]
for name in attend :
    print(name)
    if name == "최민규" :
        break
print()

for x in range(6) :
    print(x)
print()

for x in range(1, 15, 2) :
    print(x)
print()

for x in range(6) :
    print(x)
else :
    print("반복문종료")
print()

for x in range(1, 10) :
    print("{}X{}={}".format(2, x, 2*x))
print()

for x in range(2, 10) :
    print()
    print("%d단" % x)
    for y in range(1, 10) :
        print("{}X{}={}".format(x, y, x*y))
print()

###########################
# 27. 함수 - 사용자 정의 함수
###########################

'''
- 내장함수에 대한 이해, 함수 사용하기 
- 필요에 따라 import, 외장함수 사용하기
- 자주 사용하는 함수 만들어서 사용하기 = 사용자 정의 함수
'''

def magician_hat(a) :
    if a == "동전" :
        return "토끼"
    elif a == "손수건" :
        return "비둘기"
print(magician_hat("동전"))
print(magician_hat("손수건"))
print()

def hello(a) :
    while a > 0 :
        print("안녕하세요, 반갑습니다.")
        a -= 1
hello(3)
print()

def add(a, b) :
    return a + b
print(add(150, 180))
print()

def add_all(*args) :
    total = 0
    for i in args :
        total = total + i
    return total
print(add_all(1, 6, 7, 20, 23, 14, 100))
print()

def phone(*args) :
    print("회원님의 전화번호는 " + args[2] + "입니다.")
phone("양나래", "서울 강남구", "010-1234-4567")
print()

def cheerup(name) :
    """
    이 함수는 응원의 메시지를 출력하는 함수.
    인수로는 응원할 사람의 이름을 입력.
    """
    print("{}님 힘내세요, 화이팅".format(name))
cheerup("김건모")
print()

age = 29
def birthday() :
    global age
    print(age, "번째 생일을 축하합니다.")
birthday()
print()

age2 = 29

def birthday() :
    global age2
    age2 = 30
    print(age2, "번째 생일을 축하합니다.")
birthday()
print(age2, "번째 생일을 축하합니다.")
print()

def menu(beverage="coke", food="burger") :
    print("주문한 음식은 {}과 {}입니다.".format(beverage, food))
menu()
print()

def my_family(**child) :
    print("우리집 막내는 ", child["c1"], "입니다.")
my_family(c1="황찬희", c2="황인우", c3="황혜원")
print()

num = int(input())
print("선착순", num,"명")

def first_come(num) :
    person = ["구준표", "금잔디", "송우빈", "윤지후", "강희수", "나공주"]
    if num == 0 :
        print("끝.")
    else :
        print(person[num - 1])
        first_come(num - 1)
first_come(num)
print()

# 람다 함수
print((lambda a, b : a + b) (4, 5))
print()

#####################
# 28. 함수 - 내장 함수
#####################

# 절대값
num = 999
pnum = abs(num)
mnum = abs(-num)
print(pnum == mnum)
print()

# 두수를 나눈 몫과 나머지
print(type(divmod(9, 2)))
print(divmod(9, 2))
print()

# 순서가 있는 컬렉션을 인덱스 포함해서 출력 : enumerate
topten = ["애플", "구글", "마이크로소프트", "아마존", "페이스북", "코카콜라", "디즈니"]

for i, enterprice in enumerate(topten) :
    print(i, enterprice)
print()

# map
name = ["김광일", "김광이", "김광삼", "김광사", "김광오", "김광육"]
def student(x) :  return x+" 학생"

mapresult = list(map(student, name))
print(mapresult)
print()

######################
# 29. 모듈과 라이브러리
######################

# 모듈: 함수나 변수 또는 클래스를 모아 놓은 파일

# math
import math 
# from math import factorial

num = math.factorial(5)
# num = factorial(5)
print(num)
print()

print(math.pi)
print(math.e)
print(math.pow(3, 3))           # 제곱
print(math.sqrt(4))             # 제곱근
print(math.log(4, 2))           # 로그
print()

# random
from random import *
a = random()
print(a)

a = uniform(0.1, 9.99)
print(a)

a = randrange(1, 101, 2)
print(a)

a = randrange(10)
print(a)
