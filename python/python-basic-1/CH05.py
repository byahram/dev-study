"""
2025.03.25 화
"""

print("------------------------")

# 복습: for문 예제 1
print()
print(">> 복습: for문 예제 1")

numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers)) :
    print(numbers[i])

# for문 예제 2
print()
print(">> 복습: for문 예제 2")

fruits = ["apple", "banana", "cherry", "data"]

for i in range(len(fruits)) :
    print(fruits[i])

print()
print("------------------------")


"""
* sort() 메서드
    - 리스트를 자동으로(오름차순) 정렬하여 다시 저장한다.
    - 즉, 원본 리스트가 변경된다.
    - 문법 : 리스트.sort()
    
* sort(reverse = True) 메서드
    - 리스트를 자동으로(내림차순) 정렬하여 다시 저장한다.
    
* sorted() 함수
    - 새롭게 정렬된 리스트를 반환한다.
    - sort() 메서드와 달리 원본 리스트는 변경되지 않는다.
    
* 리스트 반전
    - 리스트의 맨 앞 요소가 맨 뒤로, 맨 뒤 요소가 맨 앞으로 이동한다.
    - 리스트 원본이 변경된다.
    - 리스트.reverse() 
"""

# sort() 예제 1
print()
print(">> sort() 예제 1")

list_num = [2, 7, 3, 5]
list_num.sort()
print(list_num)

list_num.sort(reverse=True)
print(list_num)

# sort() 예제 2
print()
print(">> sort() 예제 2")

names = ["Tom", "Jerry", "Alice", "Bob"]
names.sort()
print(names)

# sorted() 예제 1
print()
print(">> sorted() 예제 1")

numbers2 = [5, 2, 3, 4, 1]
sorted_numbers = sorted(numbers2)
print(numbers2)     # 원본 바뀌지 않음
print(sorted_numbers)

# 리스트 반전 예제 1
print()
print(">> 리스트 반전 예제 1")

list_num2 = [2, 7, 3, 5]
list_num2.reverse()
print(list_num2)

print()
print("------------------------")


"""
* 리스트 내부에 요소가 있는지 확인하는 키워드 : in
    - 파이썬에서 in 키워드는 리스트에 특정 값이 존재하는지 확인하는데 사용
    - 문법: 특정값 in 리스트
    
* 리스트 내부에 요소가 없는지 확인하는 키워드 : not in
    - 존재하지 않는 지 확인하는 데 사용
"""

# in, not in 예제 1
print()
print(">> in, not in 예제 1")

list_n = [1, 2, 3, 4, 5, 6, 7]
print(3 in list_n)      # 리스트에 존재하기 때문에 True
print(10 in list_n)     # 리스트에 없기 때문에 False
print(5 not in list_n)  # 리스트에 있기 때문에 False

print()
print("------------------------")


"""
* 리스트 요소를 문자열로 만들기 : join()
    - 리스트의 요소들을 하나하나 엮어서 새로운 문자열을 만들기 위해 파이썬은 join() 메소드 제공
    - 문법 : 요소 사이에 들어갈 문자.join(리스트)
"""

# join 예제 1
print()
print(">> join() 예제 1")

list_abc = ["a", "b", "c"]
result = "-".join(list_abc)
print(result)

result2 = "*".join(list_abc)
print(result2)

print()
print("------------------------")

# 종합 1. for문을 사용하여 리스트 출력하기
print()
print(">> 종합 1. for문을 사용하여 리스트 출력하기")

animals = ["dog", "cat", "tiger", "lion"]
for i in range(len(animals)) :
    print(i)

# 종합 2. 리스트 오름차순 정렬
print()
print(">> 종합 2. 리스트 오름차순 정렬")

numbers3 = [15, 3, 9, 1, 7]
numbers3.sort()
print(numbers3)

# 종합 3. 리스트 내림차순 정렬
print()
print(">> 종합 3. 리스트 내림차순 정렬")

score = [88, 92, 75, 63, 99]
score.sort(reverse=True)
print(score)

# 종합 4. 원본 리스트와 새 리스트 모두 출력하기
print()
print(">> 종합 4. 원본 리스트와 새 리스트 모두 출력하기")

value = [10, 5, 8, 2, 6]
sorted_value = sorted(value)
print("원본 리스트 :", sorted_value)
print("정렬된 리스트 :", sorted)

# 종합 5. 리스트 반전시키기
print()
print(">> 종합 5. 리스트 반전시키기")

colors = ["red", "green", "blue"]
colors.reverse()
print(colors)

print()
print("------------------------")


"""
* 자료형 1: < 딕셔너리 (Dictionary) >
    - 키(key)와 값(value)의 쌍으로 이루어진 자료형으로 정보를 효율적으로 관리하는데 유용하다.
    - key : 데이터를 식별하는 고유한 값. key는 중복될 수 없다. 만약, 같은 key가 여러 번 쓰이면, 마지막에 입력된 값으로 덮어쓰기 된다.
    - value : key에 대응되는 데이터 값. value는 중복 가능하다.
        ex) 키(key) - 값(value)
             apple  -   사과
    - 문법 = {
                key1: value1
                key2: value2
            }
        ex) {
                "name" : "kim",
                "age" : 30,
                "phone: " "01024562345"
            }
    - 이처럼 딕셔너리는 상품 정보처럼 여러가지 정보를 한꺼번에 저장하고 관리하는데 유용하다
    
* 딕셔너리 (Dictionary) 요소
    - 딕셔너리에 포함된 항목들을 하나의 쌍 또는 페어(pair)라고 한다.
"""

# 딕셔너리 (Dictionary)
print()
print(">> 딕셔너리 (Dictionary)")

dic = {
    "a" : "abc",
    "b" : 3,
    4 : [1, 2, 3],
}
print(dic)

# 딕셔너리에 저장된 데이터를 한쌍씩 출력하고 싶으면 : 변수명[key값]
print(dic["a"])
print(dic[4])

# 딕셔너리 예제 1
print()
print(">> 딕셔너리 예제 1")

fruits = {
    "apple" : 3,
    "banana" : 5,
    "orange" : 2
}
print(fruits)

# 딕셔너리 예제 2
print()
print(">> 딕셔너리 예제 2")

person = {
    "name" : "kim",
    "age" : 30,
    "phone" : "010-1234-5667",
    "subject" : ["python", "java"]
}
print("1. 딕셔너리 전체 출력 :", person)
print("2. kim 출력 :", person["name"])
print("3. subject 출력 :", person["subject"])
# print(person["face"])     # KeyError: "face" -> key 값이 없을 때 나타나는 에러

print()
print("------------------------")


"""
* 딕셔너리 (Dictionary) 연산
    - 연산을 지원하며, 이를 통해 딕셔너리를 자유롭게 조작하고 데이터를 활용할 수 있다.
    - 가장 기본적인 딕셔너리 연산은 빈 딕셔너리를 생성하는 것이다.
    - 빈 딕셔너리는 아직 어떤 데이터도 저장하지 않은 상태다.
    - dic = {}
    
* key-value 쌍 추가
    - 문법 : 딕셔너리 변수명[새로운 key값] = 새로운 value값
    
* key-value 쌍 삭제
    - 문법 : del 딕셔너리 변수명[삭제하고 싶은 key값]

* pop을 사용하여 삭제하기
    - pop은 삭제하면서 값을 반환해준다. 그래서 나중에 그 값을 활용할 수 있다.
    - 문법 : value = 딕셔너리 변수명.pop(삭제하고 싶은 key값)
    
* 딕셔너리 전체 삭제
    - 문법 : 딕셔너리 변수명.clear()
"""

# key-value 쌍 추가 예제 1
print()
print(">> key-value 쌍 추가 예제 1")

dic_color = {
    "red" : "apple",
    "yellow" : "banana",
    "purple" : "grape"
}
print(dic_color)

# dic_color["Orange"] = "orange"
dic_color["red"] = "orange"
print(dic_color)

# key-value 쌍 추가 예제 2
print()
print(">> key-value 쌍 추가 예제 2")

dic_animal = {
    "dog" : "멍멍",
    "cat" : "야옹",
    "cow" : "음메"
}
print(dic_animal)

dic_animal["bird"] = "짹짹"
print(dic_animal)

dic_animal["cat"] = "냐옹"
print(dic_animal)

# key-value 쌍 삭제 예제 1 : del
print()
print(">> key-value 쌍 삭제 예제 1 : del")

sports_star = {
    "축구" : "손흥민",
    "야구" : "이정후",
    "피겨스케이팅" : "김연아",
    "수영" : "박태환",
}
print(sports_star)

del sports_star["야구"]
print(sports_star)

# key-value 쌍 삭제 예제 2 : pop()
print()
print(">> key-value 쌍 삭제 예제 2 : pop()")

dic2 = {
    1 : "java",
    2 : "python",
    3 : "C++"
}
print(dic2)

value = dic2.pop(1)
print("삭제된 값 :", value)
print("삭제 후 딕셔너리 :", dic2)

# 딕셔너리 전체 삭제하기 예제 1
print()
print(">> 딕셔너리 전체 삭제하기 예제 1")

dic2.clear()
print(dic2)

print()
print("------------------------")


"""
* 딕셔너리의 메서드(기능)
    - .get(key) : 해당 key의 값을 가져옴 (key가 없으면 None 반환)
    - .keys() : 딕셔너리의 모든 key 값을 반환
    - .values() : 딕셔너리의 모든 value 값을 반환
    - .pop(key) : key에 해당하는 항목을 삭제하고, 그 value를 반환
    - .update() : 다른 딕셔너리를 추가하거나 기존 값을 수정
    
* 딕셔너리의 키 값들을 리스트로 변환하기
    - 문법 : list(딕셔너리.keys())
    
* 딕셔너리의 Value 값들을 리스트로 변환하기
    - 문법 : list(딕셔너리.values())
"""

# .get(key) 예제 1
print()
print(">> .get(key) 예제 1")

person = {
    "name" : "Tom",
    "age" : 12
}
print(person.get("name"))
print(person.get("height"))     # None (오류가 아님)

# .get(key) 예제 2
print()
print(">> .get(key) 예제 2")

fruit_color = {
    "apple" : "red",
    "banana" : "yellow",
    "grape" : "purple"
}
print(fruit_color.get("banana"))
print(fruit_color.get("grapefruit"))

# .keys() 예제 1
print()
print(">> .keys() 예제 1")

fruit_color2 = {
    "red" : "apple",
    "yellow" : "banana",
    "purple" : "blueberry"
}
print("1. keys() 출력 : ", fruit_color2.keys())
# fruit_color2.keys().append("test")      # append는 리스트에서만 사용할 수 있다.

print()
print("2. for문 + keys() 결합")
for i in fruit_color2.keys() :
    print(i)

# .keys() 예제 2
print()
print(">> .keys() 예제 2")

job_dic = {
    "teacher" : "school",
    "doctor" : "hospital",
    "chef" : "restaurant"
}
print("직업 목록 :", job_dic)

for i in job_dic.keys() :
    print(i)

# 리스트로 변환하기 예제 1 : keys()
print()
print(">> 리스트로 변환하기 예제 1 : keys()")

fruit_colors = {
    "red" : "apple",
    "yellow" : "banana",
    "purple" : "blueberry",
}
print("1. keys()")
print(fruit_colors.keys())

print()
print("2. 리스트로 변환하기 : list() + keys()의 결합")
# keys() 메서드를 호출하여 반환된 객체를 list 메서드에 인자로 전달
color_list = list(fruit_colors.keys())
print(color_list)
color_list.append("blue")
print(list(color_list))

# 리스트로 변환하기 예제 2 : keys()
print()
print(">> 리스트로 변환하기 예제 2 : keys()")

animal_sounds = {
    "dog" : 1,
    "cat" : 2,
    "cow" : 3
}
animal_list = list(animal_sounds.keys())
print(animal_list)

animal_list.pop(1)
print(animal_list)

animal_list.remove("dog")
print(animal_list)

# 리스트로 변환하기 예제 3 : keys()
print()
print(">> 리스트로 변환하기 예제 3 : keys()")

t_sound = {
    "car" : 10,
    "train" : 20,
    "bike" : 30
}

t_list = list(t_sound.keys())
print("1. 리스트 변환 :",t_list)

t_list.append("airplane")
print("2. 값 추가 후 : ", t_list)

t_list.remove("bike")
print("3. 값 삭제 후 :", t_list)

# 리스트로 변환하기 예제 4 : values()
print()
print(">> 리스트로 변환하기 예제 4 : values()")

abc_div = {
    "a" : "alphabet",
    "b" : "best",
    "c" : "cheer"
}

print("1. values() 출력")
print(abc_div.values())

print()
print("2. for문과 values()의 결합")
for i in abc_div.values() :
    print(i)

print()
print("3. list()와 values()의 결합")
abc_list = list(abc_div.values())
abc_list.remove("alphabet")
print(abc_list)

# .pop(key) 예제 1
print()
print(">> .pop(key) 예제 1")

person = {
    "name" : "Tom",
    "age" : 12
}
age = person.pop("age")
print(age)
print(person)

# .update() 예제 1
person.update({"age" : 12})
person.update({"height" : 12})
print(person)

print()
print("------------------------")