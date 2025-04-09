"""
2025.03.27 목
"""

print()
print()
print("------------------------")
print("--- 딕셔너리 items()")
print("------------------------")
print()

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
print("--- 튜플 음수 인덱스")
print("------------------------")
print()

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
print("---------------------------------")
print()

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
