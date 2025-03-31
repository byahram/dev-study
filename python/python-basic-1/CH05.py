"""
2025.03.25 화
"""

print("------------------------")
print()

# 복습: for문 예제 1
print(">> 복습: for문 예제 1")

numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers)) :
    print(numbers[i])
print()

# for문 예제 2
print(">> 복습: for문 예제 2")

fruits = ["apple", "banana", "cherry", "data"]

for i in range(len(fruits)) :
    print(fruits[i])
print()

print("------------------------")
print()

# sort() 예제 1
print(">> sort() 예제 1")

list_num = [2, 7, 3, 5]
list_num.sort()
print(list_num)

list_num.sort(reverse=True)
print(list_num)
print()

# sort() 예제 2
print(">> sort() 예제 2")

names = ["Tom", "Jerry", "Alice", "Bob"]
names.sort()
print(names)
print()

# sorted() 예제 1
print(">> sorted() 예제 1")

numbers2 = [5, 2, 3, 4, 1]
sorted_numbers = sorted(numbers2)
print(numbers2)     # 원본 바뀌지 않음
print(sorted_numbers)
print()

# 리스트 반전 예제 1
print(">> 리스트 반전 예제 1")

list_num2 = [2, 7, 3, 5]
list_num2.reverse()
print(list_num2)
print()

print("------------------------")
print()

# in, not in 예제 1
print(">> in, not in 예제 1")

list_n = [1, 2, 3, 4, 5, 6, 7]
print(3 in list_n)      # 리스트에 존재하기 때문에 True
print(10 in list_n)     # 리스트에 없기 때문에 False
print(5 not in list_n)  # 리스트에 있기 때문에 False
print()

print("------------------------")
print()

# join 예제 1
print(">> join() 예제 1")

list_abc = ["a", "b", "c"]
result = "-".join(list_abc)
print(result)

result2 = "*".join(list_abc)
print(result2)
print()

print("------------------------")
print()

# 종합 1. for문을 사용하여 리스트 출력하기
print(">> 종합 1. for문을 사용하여 리스트 출력하기")

animals = ["dog", "cat", "tiger", "lion"]
for i in range(len(animals)) :
    print(i)
print()

# 종합 2. 리스트 오름차순 정렬
print(">> 종합 2. 리스트 오름차순 정렬")

numbers3 = [15, 3, 9, 1, 7]
numbers3.sort()
print(numbers3)
print()

# 종합 3. 리스트 내림차순 정렬
print(">> 종합 3. 리스트 내림차순 정렬")

score = [88, 92, 75, 63, 99]
score.sort(reverse=True)
print(score)
print()

# 종합 4. 원본 리스트와 새 리스트 모두 출력하기
print(">> 종합 4. 원본 리스트와 새 리스트 모두 출력하기")

value = [10, 5, 8, 2, 6]
sorted_value = sorted(value)
print("원본 리스트 :", sorted_value)
print("정렬된 리스트 :", sorted)
print()

# 종합 5. 리스트 반전시키기
print(">> 종합 5. 리스트 반전시키기")

colors = ["red", "green", "blue"]
colors.reverse()
print(colors)
print()

print("------------------------")
print()

# 딕셔너리 (Dictionary)
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
print()

# 딕셔너리 예제 1
print(">> 딕셔너리 예제 1")

fruits = {
    "apple" : 3,
    "banana" : 5,
    "orange" : 2
}
print(fruits)
print()

# 딕셔너리 예제 2
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
print()

# key-value 쌍 추가 예제 1
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
print()

# key-value 쌍 추가 예제 2
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
print()

# key-value 쌍 삭제 예제 1 : del
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
print()

# key-value 쌍 삭제 예제 2 : pop()
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
print()

# 딕셔너리 전체 삭제하기 예제 1
print(">> 딕셔너리 전체 삭제하기 예제 1")

dic2.clear()
print(dic2)
print()

print("------------------------")
print()

# .get(key) 예제 1
print(">> .get(key) 예제 1")

person = {
    "name" : "Tom",
    "age" : 12
}
print(person.get("name"))
print(person.get("height"))     # None (오류가 아님)
print()

# .get(key) 예제 2
print(">> .get(key) 예제 2")

fruit_color = {
    "apple" : "red",
    "banana" : "yellow",
    "grape" : "purple"
}
print(fruit_color.get("banana"))
print(fruit_color.get("grapefruit"))
print()

# .keys() 예제 1
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
print()

# .keys() 예제 2
print(">> .keys() 예제 2")

job_dic = {
    "teacher" : "school",
    "doctor" : "hospital",
    "chef" : "restaurant"
}
print("직업 목록 :", job_dic)

for i in job_dic.keys() :
    print(i)
print()

# 리스트로 변환하기 예제 1 : keys()
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
print()

# 리스트로 변환하기 예제 2 : keys()
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
print()

# 리스트로 변환하기 예제 3 : keys()
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
print()

# 리스트로 변환하기 예제 4 : values()
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
print()

# .pop(key) 예제 1
print(">> .pop(key) 예제 1")

person = {
    "name" : "Tom",
    "age" : 12
}
age = person.pop("age")
print(age)
print(person)
print()

# .update() 예제 1
person.update({"age" : 12})
person.update({"height" : 12})
print(person)
print()

print("------------------------")
print()
