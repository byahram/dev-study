"""
2025.03.27 목
"""

print()
print()
print("------------------------")
print("--- 딕셔너리 items()")
print("------------------------")
print()

'''
[딕셔너리의 메서드(기능)]
 
6. items()
    - 딕셔너리 안의 (키, 값) 쌍을 튜플 형태로 모두 가져올 수 있다.
    - 문법 : 딕셔너리.items()
'''

# 예제 1
abc_dic = {
    "a" : "alphabet",
    "b" : "best",
    "c" : "cheer",
}

print("1. items()")
print(abc_dic.items())
print()

print("2. for문 + items() 결합")
# for문의 반복 루프에서 매번 a 변수의 현재값, 즉 key-value 쌍을 출력
for a in abc_dic.items() :
    print(a)
print()

print("3. list() + items() 결합")
# items() 메서드를 사용해 딕셔너리의 모든 키-값을 튜플 형태로 리스트에 복사
abc_list = list(abc_dic.items())
print(abc_list)

abc_list.append(("g", "good"))
print(abc_list)

print()
print("------------------------")
print()

# 예제 2
score_dic = {
    "Korean" : 95,
    "Math" : 88,
    "English": 92,
}

print("1. items() 출력")
print(score_dic.items())
print()

print("2. for문 + items() 결합")
for subject, score in score_dic.items() :
    print(f"{subject}, {score}")
print()

print("3. list() + items() 결합")
score_list = list(score_dic.items())
print(score_list)

score_list.append(("Science", 55))
print(score_list)

print()
print()
print("------------------------")
print("--- 튜플")
print("------------------------")
print()

'''
[컬렉션 자료형 - 튜플(Tuple)]

- 여러 개의 값을 하나의 변수에 저장할 수 있는 자료형
- 리스트와 비슷하지만, 튜플은 수정할 수 없다는 큰 차이점이 있다.
- 변수명 = (요소1, 요소2, 요소3)
'''

# 1.
names = ("kim", "lee", "park")
print(names[-3])
print(names[-2])
print(names[-1])

for i in names :
    print(i)

print()
print()
print("------------------------")
print("--- 튜플 슬라이싱")
print("------------------------")
print()

# 1.
example = (3, 9, "y", 2, "k", True)
print(example[1:4])     # 4는 포함하지 않는다.
print(example[2:6])
print(example[0:5])
print()

# 범위를 벗어난 슬라이싱
print(example[4:8])
# print(example[8])     # 오류 발생

print()
print()
print("---------------------------------")
print("--- 리스트와 튜플 요소 수정하기")
print("---------------------------------")
print()

'''
[리스트와 튜플의 차이]

- 리스트(list) : [] 사용 / 수정 가능  / 크기 변경 가능  / 변수명 = [요소1, 요소2, 요소3.......]
- 튜플(tuple) : () 사용 / 수정 불가능 / 크기 고정       / 변수명 = (요소1, 요소2, 요소3......)

[튜플은 언제 사용할까?]

1. 값이 변하지 않아야 할 때
2. 리스트보다 속도가 빠르다.
3. 함수에서 여러 개의 값을 한번에 반환할 때
'''

# 1.
list3 = [3, 0, 9]
tuple3 = (3, 0, 9)

#전체 리스트, 튜플 출력
print(list3)
print(tuple3)

# 각 첫번째 요소 수정
list3[0] = 30
# tuple[0] = 30   # 오류 발생 : 튜플은 수정할 수 없다.

# 리스트 요소 추가
list3.append(7)
print(list3)

# 튜플 요소 추가
# tuple.append(7)
# print(tuple)    # 오류 발생 : 튜플은 수정할 수 없다.

print()
print()
print("------------------------")
print("--- count()")
print("------------------------")
print()

'''
[튜플의 메서드]

1. count()
    - 리스트, 튜플, 문자열 등에서 특정 값이 몇 번 나오는지 알려주는 메서드
    - 문법 : 변수명.count(찾을 값)
'''

# 예제 1
# list
numbers = [1, 2, 3, 2, 4, 2]
print("1) list의 count() :", numbers.count(2))

# tuple
colors = ("red", "blue", "red", "green", "red")
print("2) tuple의 count() :", colors.count("red"))

# text
text = "banana"
print("3) text의 count() :", text.count("b"))

print()
print("------------------------")
print()

# 예제 2
tuple_alphabet = ("a", "a", "b", "c", "c", "a")
print("a의 개수 :", tuple_alphabet.count("a"))
print("b의 개수 :", tuple_alphabet.count("b"))
print("c의 개수 :", tuple_alphabet.count("c"))

print()
print()
print("------------------------")
print("--- index()")
print("------------------------")
print()

'''
[튜플의 메서드]

2. index() 
    - 리스트, 튜플, 문자열 등에서 특정 값의 위치(어디에 있는지)를 알려주는 메서드 (첫 등장 위치 or 인덱스)
    - 문법 : 변수명.index(찾을 값)
'''

# 예제 1
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.index("banana"))

print()
print("------------------------")
print()

# 예제 2
nums = (3, 5, 7, 9, 2, 7, 1)
print(nums.index(7))

print()
print()
print("------------------------")
print("--- 데이터 교환")
print("------------------------")
print()

'''
[튜플의 활용 - 데이터 교환]

- 튜플은 각 요소를 직접 수정할 수 없지만, 두 튜플을 활용하여 간접적으로 튜플 요소의 값을 교환할 수 있다.
- '=' 연산자를 사용하여 새로운 튜플의 값을 기존 튜플 변수에 할당한다
'''

# 예제 1
x = 10
y = 20
print("교환 전 출력 : x = ", x, ", y = ", y)

(x, y) = (y, x)
print("교환 후 출력 : x = ", x, ", y = ", y)

print()
print("------------------------")
print()

# 예제 2
name = "Alice"
nickName = "Ace"
print("교환 전 출력 : name = ", name, ", nickName = ", nickName)

(name, nickName) = (nickName, name)
print("교환 후 출력 : name = ", name, ", nickName = ", nickName)

print()
print()
print("---------------------------------")
print("--- 각자의 형태를 가진 자료형들")
print("--- 세트(Set)")
print("---------------------------------")
print()

'''
[컬렉션 자료형 - 세트(Set)]

- 중복을 허용하지 않고, 순서가 없는 자료형이다
- 세트란?
    - 수학에서 말하는 집합과 비슷하다.(합집합, 교집합, 차집합)
    - 중복된 값을 자동으로 제거한다.
    - 값들의 순서가 없어서 인덱스로는 접근이 불가능하다.

[세트의 기본 형태]

- 변수명 = {요소1, 요소2, 요소3 ... }
- 세트의 표현 방법은 {}
- 다른 자료형을 세트로 변환하고자 할 때, 문법 : set(세트로 바꾸고 싶은 다른 자료형)

[참고]
Q : 문자열을  set으로 변환했을 대 순서가 매번 달라지는데, 숫자 리스트나 튜플은 set으로 바꾸면 숫자가 거의 고정되어 있는지?
A : 해시값이란 데이터(문자, 숫자등)를 일정한 규칙에 따라 고정된 크기의 숫자로 바꾼 값이다.
        = 데이터를 빠르게 찾기 위한 고유 식별 숫자(바뀔 수있다.)

* 숫자는 해시값이 안정적이다
    - 문자열 : set()으로 변환시 매번 달라짐
    - 숫자 : 변환을 해도 대부분 비슷한 순서이다. 
'''

str2 = "apple"
list2 = [1, 2, 3]
tuple2 = (1, 2, 3)

print("str : ", str2)
print("list : ", list2)
print("tuple : ", tuple2)

print()
print()
print("----------------------------")
print("--- set로 변환한 자료형들")
print("----------------------------")
print()

# 1.
# 변수 str의 문자열 "apple"을 set 자료형으로 변환하여 set_str에 할당한다.
set_str = set(str2)
set_list = set(list2)
set_tuple = set(tuple2)

print("set_str : ", set_str)    # 출력값이 계속 변하는 이유는 set은 순서 유지를 하지 않기 때문이다. 중복 허용하지 않기에 a가 하나가 사라짐
print("set_list : ", set_list)
print("set_tuple : ", set_tuple)

print()
print("------------------------")
print()

# 2. (중복 포함)
num_list = [1, 2, 2, 3, 3, 3, 4]
num_tuple = (5, 5, 6, 7, 6, 7, 7)

print("list 원본 :", num_list)
print("tuple 원본 :", num_tuple)
print()

print("list > set :", set(num_list))
print("tuple > set :",set(num_tuple))

print()
print()
print("-----------------------------")
print("--- set 요소 접근 시도하기")
print("-----------------------------")
print()

# str_banana = "banana"
# set_banana = set(str_banana)
#print(set_banana[0])    # set는 인덱싱이 불가능

# 예제 1. 리스트와 튜플로 변환하여 세트 요소에 접근하기 
str_banana = "banana"
set_banana = set(str_banana)
print(set_banana)

list_banana = list(set_banana)
tuple_banana = tuple(set_banana)
print(list_banana[0])
print(tuple_banana[1])

print()
print("------------------------")
print()

# 예제 2. 리스트와 튜플로 변환하여 세트 요소에 접근하기
str_apple = "apple"

set_apple = set(str_apple)
print(set_apple)

list_apple = list(set_apple)
tuple_apple = tuple(set_apple)

print("list_apple :", list_apple[0])
print("tuple_apple :", tuple_apple[1])

print()
print()
print("-----------------------------------")
print("--- n번째로 작은 알파벳 출력하기")
print("-----------------------------------")
print()

str_random = "apbdhwoernzhd"

# 문자열을 set으로 변경
str_random = set(str_random)
print(str_random)
list_str = list(str_random)
print(list_str)

# 오름차순 정렬
list_str.sort()
print(list_str)
print()

# 특정 순서의 알파벳 출력
print("3번째로 작은 알파벳 :", list_str[3])
print("7번째로 작은 알파벳 :", list_str[7])
print("5번째로 작은 알파벳 :", list_str[5])

print()
print()
print("------------------------")
print("--- .add()")
print("------------------------")
print()

'''
[세트의 메서드]

1. .add()
    - '하나'의 요소를 추가할 때 사용하는 메서드
    - 문법 : 세트.add(요소)

2. .update()
    - set에 여러 개의 요소를 한꺼번에 추가할 때 사용한다
    - 문법 : 세트.update(반복가능한\_자료형)
    - 예시 : s.update([1, 2, 3])
    
* 중복된 값은 자동으로 걸러진다.
'''

# 예제 1: 세트 요소 추가하기
set = {1, 2, 3}
set.add(4)
print(set)

set.update({5, 6, 7})
print(set)
print()

# 예제 2: 알파벳 세트 생성
alphabet_set = {"a", "b", "c"}
alphabet_set.add("d")
print(alphabet_set)

alphabet_set.update({"e", "f", "g"})
print(alphabet_set)

print()
print()
print("------------------------")
print("--- .remove() 삭제")
print("------------------------")
print()

'''
[세트의 메서드]

3. .remove(값)
    - 지정한 값을 제거, 그 값이 없으면 error가 발생(KeyError)
'''

# 예제 1
s = {1, 2, 3}
s.remove(2)
print(s)
#s.remove(5) # 없는 값 삭제 에러 발생

print()
print()
print("------------------------")
print("--- .discard() 삭제")
print("------------------------")
print()

'''
[세트의 메서드]

4. .discard(값)
    - 지정한 값을 제거, 그 값이 없어도 조용히 넘어감 (error 발생 X)
'''

# 예제 1
dis = {5, 6, 7}
dis.discard(6)
print(dis)
dis.discard(10)     # 없는 값 삭제 에러 발생 X

print()
print()
print("------------------------")
print("--- .pop() 삭제")
print("------------------------")
print()

'''
[세트의 메서드]

5. pop()
    - 임의의 요소 하나 제거 + 그 값을 반환
    - 순서가 없으므로 어떤 값이 제거 될 지 모름
    - 비어 있으면 error 발생 (KeyError)
'''

# 예제 1
set_d = {"b", "l", "u", "e"}

# pop메서드를 사용하여 요소를 랜덤으로 제거
print(set_d)
# pop은 삭제 요소를 반환한다.
print(set_d.pop())    

print()
print()
print("------------------------")
print("--- .clear() 삭제")
print("------------------------")
print()

'''
[세트의 메서드]

6. clear()
    - 모든 요소 삭제 (세트 초기화)
'''

# 예제 1
set_last = {1, 2, 3, 4}
set_last.clear()
print(set_last)

print()
print()
print("------------------------")
print("--- 세트의 교집합")
print("------------------------")
print()

'''
[세트의 연산 종류]

| 연산 종류 | 기호 또는 메서드           | 의미                         |
| -------- | ----------------------- | ---------------------------- |
| 합집합    | \| 또는 union()          | 모든 요소                     |
| 교집합    | `&` 또는 .intersection() | 공통된 값들만 추출              |
| 차집합    | `-` 또는 .difference()   | 앞 세트에는 있고 뒤에는 없는 값  |
'''

# 예제 1
set_a = {2, 4, 6}
set_b = {3, 6, 9}

# intersection() 메서드를 사용하여 두 세트의 교집합을 찾는다.
intersection_AandB = set_a.intersection(set_b)
print(intersection_AandB)

# & 연산자를 사용하여 두 세트의 교집합을 찾는다.
intersection_AandB = set_a & set_b
print(intersection_AandB)

print()
print("------------------------")
print()

# 예제 2
set_c = {"apple", "banana", "cherry"}
set_d = {"apple", "banana", "orange"}

# 메서드를 이용하여 교집합
print(set_c.intersection(set_d))

# 연산자를 이용하여 교집합
print(set_c & set_d)

print()
print()
print("------------------------")
print("--- 세트의 합집합")
print("------------------------")
print()

# 예제 1
setA = {2, 4, 6}
setB = {3, 6, 9}

# union() 메서드를 사용하여 두 세트의 합집합 찾기
union_AandB = setA.union(setB)
print(union_AandB)

# 연산자 사용
union_AandB = setA | setB
print(union_AandB)

print()
print()
print("------------------------")
print("--- 세트의 차집합")
print("------------------------")
print()

setA = {2, 4, 6}
setB = {3, 6, 9}

# 메서드
diff_AandB = setA.difference(setB)
print(diff_AandB)

# 연산자
diff_AandB = setA - setB
print(diff_AandB)

print()
print()
print("------------------------")
print("--- 함수")
print("------------------------")
print()

'''
[메모리 구조]

1. 스택 영역 
    - 함수가 호출 될 때 생기는 공간
    - 지역 변수나 매개변수가 저장된다.
    - 함수가 끝나면 이 영역의 값도 사라진다.

2. 힙 영역
    - 객체나 리스트 같이 동적으로 생성되는 데이터가 저장된다. 
    - 함수가 끝나도 참조가 남아있으면 계속 존재한다.

3. Global/ Static영역
    - 프로그램이 시작될 때부터 끝날 때까지 유지
    - 전역 변수, 모듈, 클래스, 함수 정의등 저장된다.
'''

# 예제 1
def my_func() :         # my_func 이라는 함수 선언
    x = 10
    print(x)

my_func()

print()
print("------------------------")
print()

# 예제 2
def say_hello() :
    message = "안녕 반가워!"
    print(message)

say_hello()

print()
print("------------------------")
print()

# 예제 3
def cal() :
    num = 4
    result = num * num
    print(result)
cal()

print()
print("------------------------")
print()

# 예제 4. 리스트 출력하기
def print_fruits() :
    fruits = ["사과", "바나나", "포도"]
    print(fruits)

print_fruits()

print()
print()
print("------------------------ 끝")
print()
