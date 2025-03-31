# [Python1] 컬렉션 자료형

<br>

## 리스트 (list)

### 리스트란?

- 일상 생활에서 사용하는 목록과 비슷한 개념을 가진 자료구조
- 여러 개의 데이터를 하나의 변수에 한 번에 저장하고 관리할 수 있다.
- - 하나의 데이터만 담은 변수
  - age = 20
- 여러 개의 데이터를 묶은 리스트를 담은 변수
  - nums = [0, 1, 2, 3] 데이터들을 쉼표로 구분하여 나열한다.

```python
numbers = [0, 1, 2, 3, 4]       # 숫자 리스트
alphabets = ['a', 'b', 'c']     # 문자 리스트
bools = [True, True, False]     # 논리값 리스트
greetings = ["hi", "hello"]     # 문자열 리스트

# 파이썬에서만 가능 (다른 언어에서는 사용 불가)
example = [3, 9, "y", 2, "k", True]     # 숫자, 문자, 논리값 혼합하여 담은 리스트

# 리스트 슬라이싱
리스트[start : stop : step]

# IndexError
nums = [1, 2, 3, 4, 5]      # 인덱스는 5까지 있다
print(nums[7])              # IndexError: list index out of range
```

```python
# EX1
nums = [6, 1, 3]
print(nums)       # [6, 1, 3]

# EX2. 인덱스를 사용하여 요소 접근하기
names = ["kim", "lee", "park"]
print(names[0])         # kim
print(names[1])         # lee
print(names[2])         # park
print(names[-1])        # park
print(names[-2])        # lee
print(names[-3])        # kim

# EX3
nums = [10, 20, 30, 40, 50]
print(nums[0])          # 10
print(nums[2])          # 30
print(nums[4])          # 50
print(nums[2])          # 30

# EX4. 리스트 슬라이싱
example = [3, 9, "y", 2, "k", True]
print(example[1:4])           # [9, 'y', 2]
print(example[2:])            # ['y', 2, 'k', True]
print(example[0:-1])          # [3, 9, 'y', 2, 'k']
```

### 리스트 결합

- 리스트에서 자주 사용하는 연산 중 하나는 결합이다.
- 리스트 결합은 여러 개의 리스트를 하나의 리스트로 합쳐 새로운 리스트를 만들 수 있는 연산이다.
- '+' 연산자 - 두개 이상의 리스트를 직접 연결하여 새로운 리스트를 만든다.

  - 기존 리스트를 수정하지 않는다.

  ```python
  list1 = ["A", "B", "C"]
  list2 = ["D", "E"]

  list3 = list1 + list2
  print(list3)            # ['A', 'B', 'C', 'D', 'E']

  list3 = list2 + list1
  print(list3)            # ['D', 'E', 'A', 'B', 'C']
  ```

- extend()메서드 - 기존 리스트의 끝에 다른 리스트의 모든 요소를 추가한다.

  - 기존 리스트를 수정한다.
  - 메모리에 효율적이다
  - 문법 : 리스트.extend(연결할 리스트)

  ```python
  # EX1
  list11 = ["A", "B", "C"]
  list22 = ["D", "E"]
  list11.extend(list22)

  print(list11)           # ['A', 'B', 'C', 'D', 'E']
  print(list22)           # ['D', 'E']

  # EX2
  nums1 = [1, 2, 3]
  nums2 = [4, 5]
  nums1.extend(nums2)
  print(nums1)            # [1, 2, 3, 4, 5]

  # EX3. 리스트 반복 예제
  nums1 = [1, 9, 3, 0]
  print(nums1 * 3)        # [1, 9, 3, 0, 1, 9, 3, 0, 1, 9, 3, 0]
  ```

### 리스트 메서드(기능)

- append()

  - 리스트에 요소를 추가하고 싶을 때 간단하게 쓰는 메서드.
  - 리스트의 마지막에 새로운 요소를 추가하는 역할.
  - 문법 : 리스트변수.append(추가할 값(요소))

  ```python
  # EX1
  nums4 = [1, 2, 3]
  nums4.append(4)
  print("추가 후 : ", nums4)          # 추가 후 :  [1, 2, 3, 4]

  # EX2
  fruits = ["apples", "bananas"]
  fruits.append("cherry")
  print("추가 후 : ", fruits)         # 추가 후 :  ['apples', 'bananas', 'cherry']
  ```

- insert()

  - 파이썬에서는 리스트의 중간에 요소를 삽입할 수 있는 insert() 메서드를 제공
  - 문법 : 리스트변수.insert(위치(인덱스 번호), 추가할 값(요소))

  ```python
  # EX1
  nums5 = [4, 5, 6]
  print("추가 전 : ", nums5)        # 추가 전 :  [4, 5, 6]
  nums5.insert(1, 8)
  print("추가 후 : ", nums5)        # 추가 후 :  [4, 8, 5, 6]

  # EX2. append, insert
  animals = ["monkey", "dog"]
  print("추가 후 :", animals)       # 추가 후 : ['monkey', 'dog']

  animals.append("cat")
  animals.append("lion")
  print("결과 1 :", animals)        # 결과 1 : ['monkey', 'dog', 'cat', 'lion']

  animals.insert(2, "horse")
  print("결과 2 :", animals)        # 결과 2 : ['monkey', 'dog', 'horse', 'cat', 'lion']

  animals.insert(4, "cow")
  print("결과 3 :", animals)        # 결과 3 : ['monkey', 'dog', 'horse', 'cat', 'cow', 'lion']
  ```

- remove()

  - 특정 값을 가진 요소를 삭제
  - 문법 : 리스트변수.remove(요소)

  ```python
  # EX1
  nums6 = [1, 2, 3, 4, 5]
  print("추가 전 : ", nums6)        # 추가 전 :  [1, 2, 3, 4, 5]
  nums6.remove(2)
  print("추가 후 : ", nums6)        # 추가 후 :  [1, 3, 4, 5]

  # EX2. 여러 개의 요소가 있을 때
  color = ["black", "yellow", "red", "black"]
  color.remove("black")
  print(color)              # ['yellow', 'red', 'black']

  while "black" in color :
      color.remove("black")
  print(color)              # ['yellow', 'red']
  ```

- pop()

  - 특정 위치에 있는 요소를 삭제
  - 문법 : 리스트변수.pop(인덱스 번호)

  ```python
  # EX1
  nums7 = [1, 2, 3, 4, 5]
  print("삭제 전 : ", nums7)      # 삭제 전 :  [1, 2, 3, 4, 5]

  nums7.pop(4)
  print("삭제 후 : ", nums7)      # 삭제 후 :  [1, 2, 3, 4]

  # EX2
  colors = ["black", "yellow", "red", "black"]
  colors.pop(3)
  print(colors)         # ['black', 'yellow', 'red']

  # EX3
  numbers = [10, 20, 30, 40, 50]
  numbers.pop(2)
  print(numbers)        # [10, 20, 40, 50]
  ```

- len()

  - 리스트 길이
  - 문법 : len(리스트)

  ```python
  # EX1
  computer_science = ["data structure", "algorithms", "python"]
  subject_num = len(computer_science)
  print(subject_num)          # 3
  ```

- sort()

  - 리스트를 자동으로(오름차순) 정렬하여 다시 저장한다.
  - 즉, 원본 리스트가 변경된다.
  - 문법 : 리스트.sort()

  ```python
  # EX
  names = ["Tom", "Jerry", "Alice", "Bob"]
  names.sort()
  print(names)            # ['Alice', 'Bob', 'Jerry', 'Tom']
  ```

- sort(reverse = True)

  - 리스트를 자동으로(내림차순) 정렬하여 다시 저장한다.
  - 문법 : 리스트.sort(reverse = True)

  ```python
   # EX
  list_num = [2, 7, 3, 5]
  list_num.sort()
  print(list_num)         # [2, 3, 5, 7]

  list_num.sort(reverse=True)
  print(list_num)         # [7, 5, 3, 2]
  ```

- sorted()

  - 새롭게 정렬된 리스트를 반환한다.
  - sort() 메서드와 달리 원본 리스트는 변경되지 않는다.

  ```python
  # EX1
  numbers2 = [5, 2, 3, 4, 1]
  sorted_numbers = sorted(numbers2)

  print(numbers2)             # [5, 2, 3, 4, 1]
  print(sorted_numbers)       # [1, 2, 3, 4, 5]
  ```

- reverse()

  - 리스트의 맨 앞 요소가 맨 뒤로, 맨 뒤 요소가 맨 앞으로 이동한다.
  - 리스트 원본이 변경된다.
  - 문법 : 리스트.reverse()

  ```python
  # EX1
  list_num2 = [2, 7, 3, 5]
  list_num2.reverse()
  print(list_num2)          # [5, 3, 7, 2]
  ```

- in

  - 리스트 내부에 요소가 있는지 확인하는 키워드
  - 파이썬에서 in 키워드는 리스트에 특정 값이 존재하는지 확인하는데 사용
  - 문법: 특정값 in 리스트

- not in

  - 리스트 내부에 요소가 없는지 확인하는 키워드
  - 존재하지 않는 지 확인하는 데 사용

  ```python
  # EX1
  list_n = [1, 2, 3, 4, 5, 6, 7]
  print(3 in list_n)          # 리스트에 존재하기 때문에 True
  print(10 in list_n)         # 리스트에 없기 때문에 False
  print(5 not in list_n)      # 리스트에 있기 때문에 False
  ```

- join()

  - 리스트 요소를 문자열로 만들기
  - 리스트의 요소들을 하나하나 엮어서 새로운 문자열을 만들기 위해 파이썬은 join() 메소드 제공
  - 문법 : 요소 사이에 들어갈 문자.join(리스트)

  ```python
  # EX1
  list_abc = ["a", "b", "c"]
  result = "-".join(list_abc)
  print(result)                 # a-b-c

  result2 = "*".join(list_abc)
  print(result2)                # a*b*c
  ```

### 종합 예제

```python
# EX1. for문을 사용하여 리스트 출력하기
animals = ["dog", "cat", "tiger", "lion"]
for i in range(len(animals)) :
    print(i)          # 0 1 2 3
print()

# EX2. 리스트 오름차순 정렬
numbers3 = [15, 3, 9, 1, 7]
numbers3.sort()
print(numbers3)         # [1, 3, 7, 9, 15]

# EX3. 리스트 내림차순 정렬
score = [88, 92, 75, 63, 99]
score.sort(reverse=True)
print(score)            # [99, 92, 88, 75, 63]

# EX4. 원본 리스트와 새 리스트 모두 출력하기
value = [10, 5, 8, 2, 6]
sorted_value = sorted(value)
print("원본 리스트 :", sorted_value)          # 원본 리스트 : [10, 5, 8, 2, 6]
print("정렬된 리스트 :", sorted)              # 정렬된 리스트 : [2, 5, 6, 8, 10]

# EX5. 리스트 반전시키기
colors = ["red", "green", "blue"]
colors.reverse()
print(colors)           # ['blue', 'green', 'red']
```

<br>

## 딕셔너리 (Dictionary)

- 키(key)와 값(value)의 쌍으로 이루어진 자료형으로 정보를 효율적으로 관리하는데 유용하다.
- key : 데이터를 식별하는 고유한 값. key는 중복될 수 없다. 만약, 같은 key가 여러 번 쓰이면, 마지막에 입력된 값으로 덮어쓰기 된다.
- value : key에 대응되는 데이터 값. value는 중복 가능하다.
- 상품 정보처럼 여러가지 정보를 한꺼번에 저장하고 관리하는데 유용하다.
- 딕셔너리에 포함된 항목들을 하나의 쌍 또는 페어(pair)라고 한다.

```python
# 키(key) - 값(value)
# apple  -   사과

dic = {
    key1: value1
    key2: value2
}

person = {
    "name" : "kim",
    "age" : 30,
    "phone: " "01024562345"
}
```

```python
# EX1
dic = {
    "a" : "abc",
    "b" : 3,
    4 : [1, 2, 3],
}
print(dic)            # {'a': 'abc', 'b': 3, 4: [1, 2, 3]}
print(dic["a"])       # abc
print(dic[4])         # [1, 2, 3]

# EX2
fruits = {
    "apple" : 3,
    "banana" : 5,
    "orange" : 2
}
print(fruits)         # {'apple': 3, 'banana': 5, 'orange': 2}

# EX3
person = {
    "name" : "kim",
    "age" : 30,
    "phone" : "010-1234-5667",
    "subject" : ["python", "java"]
}

print("1. 딕셔너리 전체 출력 :", person)
# 1. 딕셔너리 전체 출력 : {'name': 'kim', 'age': 30, 'phone': '010-1234-5667', 'subject': ['python', 'java']}
print("2. kim 출력 :", person["name"])             # 2. kim 출력 : kim
print("3. subject 출력 :", person["subject"])      # 3. subject 출력 : ['python', 'java']
# print(person["face"])     # KeyError: "face" -> key 값이 없을 때 나타나는 에러
```

### 딕셔너리 (Dictionary) 연산

: 연산을 지원하며, 이를 통해 딕셔너리를 자유롭게 조작하고 데이터를 활용할 수 있다.

1. dic = {}
   - 장 기본적인 딕셔너리 연산은 빈 딕셔너리를 생성하는 것
   - 빈 딕셔너리는 아직 어떤 데이터도 저장하지 않은 상태
2. key-value 쌍 추가

   - 문법 : 딕셔너리 변수명[새로운 key값] = 새로운 value값

   ```python
    # EX1
    dic_color = {
        "red" : "apple",
        "yellow" : "banana",
        "purple" : "grape"
    }
    print(dic_color)          # {'red': 'apple', 'yellow': 'banana', 'purple': 'grape'}

    dic_color["red"] = "orange"
    print(dic_color)          # {'red': 'orange', 'yellow': 'banana', 'purple': 'grape'}

    # EX2
    dic_animal = {
        "dog" : "멍멍",
        "cat" : "야옹",
        "cow" : "음메"
    }
    print(dic_animal)         # {'dog': '멍멍', 'cat': '야옹', 'cow': '음메'}

    dic_animal["bird"] = "짹짹"
    print(dic_animal)         # {'dog': '멍멍', 'cat': '야옹', 'cow': '음메', 'bird': '짹짹'}

    dic_animal["cat"] = "냐옹"
    print(dic_animal)         # {'dog': '멍멍', 'cat': '냐옹', 'cow': '음메', 'bird': '짹짹'}
   ```

3. key-value 쌍 삭제

   - 문법 : del 딕셔너리 변수명[삭제하고 싶은 key값]

   ```python
   # EX1
    sports_star = {
        "축구" : "손흥민",
        "야구" : "이정후",
        "피겨스케이팅" : "김연아",
        "수영" : "박태환",
    }
    print(sports_star)            # {'축구': '손흥민', '야구': '이정후', '피겨스케이팅': '김연아', '수영': '박태환'}

    del sports_star["야구"]
    print(sports_star)            # {'축구': '손흥민', '피겨스케이팅': '김연아', '수영': '박태환'}
   ```

4. pop을 사용하여 삭제하기

   - pop은 삭제하면서 값을 반환해준다. 그래서 나중에 그 값을 활용할 수 있다.
   - 문법 : value = 딕셔너리 변수명.pop(삭제하고 싶은 key값)

   ```python
   # EX1
    dic2 = {
        1 : "java",
        2 : "python",
        3 : "C++"
    }
    print(dic2)           # {1: 'java', 2: 'python', 3: 'C++'}

    value = dic2.pop(1)
    print("삭제된 값 :", value)           # 삭제된 값 : java
    print("삭제 후 딕셔너리 :", dic2)     # 삭제 후 딕셔너리 : {2: 'python', 3: 'C++'}
   ```

5. 딕셔너리 전체 삭제
   - 문법 : 딕셔너리 변수명.clear()
   ```python
   # EX1
   dic2.clear()
   print(dic2)            # {}
   ```

### 딕셔너리의 메서드(기능)

- .get(key) : 해당 key의 값을 가져옴 (key가 없으면 None 반환)

  ```python
  # EX1
  person = {
      "name" : "Tom",
      "age" : 12
  }
  print(person.get("name"))       # Tom
  print(person.get("height"))     # None (오류가 아님)

  # EX2
  fruit_color = {
      "apple" : "red",
      "banana" : "yellow",
      "grape" : "purple"
  }
  print(fruit_color.get("banana"))          # yellow
  print(fruit_color.get("grapefruit"))      # None
  ```

- .keys() : 딕셔너리의 모든 key 값을 반환

  ```python
  # EX1
  fruit_color2 = {
      "red" : "apple",
      "yellow" : "banana",
      "purple" : "blueberry"
  }
  print("1. keys() 출력 : ", fruit_color2.keys())         # 1. keys() 출력 :  dict_keys(['red', 'yellow', 'purple'])
  # fruit_color2.keys().append("test")      # append는 리스트에서만 사용할 수 있다.

  print("2. for문 + keys() 결합")         # 2. for문 + keys() 결합
  for i in fruit_color2.keys() :
      print(i)                           # red yellow purple

  # EX2
  job_dic = {
      "teacher" : "school",
      "doctor" : "hospital",
      "chef" : "restaurant"
  }
  print("직업 목록 :", job_dic)           # 직업 목록 : {'teacher': 'school', 'doctor': 'hospital', 'chef': 'restaurant'}

  for i in job_dic.keys() :
      print(i)          # teacher doctor chef
  ```

  ```python
  # EX1. 딕셔너리 -> 리스트로 변환하기 : keys()
  fruit_colors = {
      "red" : "apple",
      "yellow" : "banana",
      "purple" : "blueberry",
  }
  print("1. keys()")
  print(fruit_colors.keys())          # dict_keys(['red', 'yellow', 'purple'])

  print("2. 리스트로 변환하기 : list() + keys()의 결합")
  color_list = list(fruit_colors.keys())
  print(color_list)                 # ['red', 'yellow', 'purple']

  color_list.append("blue")
  print(list(color_list))           # ['red', 'yellow', 'purple', 'blue']

  # EX2. 딕셔너리 -> 리스트로 변환하기 : keys()
  animal_sounds = {
      "dog" : 1,
      "cat" : 2,
      "cow" : 3
  }
  animal_list = list(animal_sounds.keys())
  print(animal_list)            # ['dog', 'cat', 'cow']

  animal_list.pop(1)
  print(animal_list)            # ['dog', 'cow']

  animal_list.remove("dog")
  print(animal_list)            # ['cow']

  # EX3. 딕셔너리 -> 리스트로 변환하기 : keys()
  t_sound = {
      "car" : 10,
      "train" : 20,
      "bike" : 30
  }

  t_list = list(t_sound.keys())
  print("1. 리스트 변환 :",t_list)      # 1. 리스트 변환 : ['car', 'train', 'bike']

  t_list.append("airplane")
  print("2. 값 추가 후 : ", t_list)     # 2. 값 추가 후 :  ['car', 'train', 'bike', 'airplane']

  t_list.remove("bike")
  print("3. 값 삭제 후 :", t_list)      # 3. 값 삭제 후 : ['car', 'train', 'airplane']
  ```

- .values() : 딕셔너리의 모든 value 값을 반환

  ```python
  # EX1. 딕셔너리 -> 리스트로 변환하기 values 사용
    abc_div = {
        "a" : "alphabet",
        "b" : "best",
        "c" : "cheer"
    }

    print("1. values() 출력")
    print(abc_div.values())         # dict_values(['alphabet', 'best', 'cheer'])
    print()

    print("2. for문과 values()의 결합")
    for i in abc_div.values() :
        print(i)                    # alphabet best cheer
    print()

    print("3. list()와 values()의 결합")
    abc_list = list(abc_div.values())
    abc_list.remove("alphabet")
    print(abc_list)                 # ['best', 'cheer']
  ```

- .pop(key) : key에 해당하는 항목을 삭제하고, 그 value를 반환

  ```python
  # EX1
  person = {
      "name" : "Tom",
      "age" : 12
  }
  age = person.pop("age")
  print(age)          # 12
  print(person)       # {'name': 'Tom'}
  ```

- .update() : 다른 딕셔너리를 추가하거나 기존 값을 수정

  ```python
  # EX1
  person = {
      "name" : "Tom",
      "age" : 12
  }
  person.update({"age" : 12})
  person.update({"height" : 12})
  print(person)         # {'name': 'Tom', 'age': 12, 'height': 12}
  ```

### 딕셔너리의 키 값들을 리스트로 변환하기

- 문법 : list(딕셔너리.keys())

### 딕셔너리의 Value 값들을 리스트로 변환하기

- 문법 : list(딕셔너리.values())

### items() 메서드

- 딕셔너리 안의 (키, 값) 쌍을 튜플 형태로 모두 가져올 수 있다.
- 문법 : 딕셔너리.items()

  ```python
  # EX1
  abc_dic = {
      "a" : "alphabet",
      "b" : "best",
      "c" : "cheer",
  }

  print("1. items()")
  print(abc_dic.items())        # dict_items([('a', 'alphabet'), ('b', 'best'), ('c', 'cheer')])
  print()

  print("2. for문 + items() 결합")
  for a in abc_dic.items() :
      print(a)          # ('a', 'alphabet') ('b', 'best') ('c', 'cheer')
  print()

  print("3. list() + items() 결합")
  abc_list = list(abc_dic.items())
  print(abc_list)         # [('a', 'alphabet'), ('b', 'best'), ('c', 'cheer')]

  abc_list.append(("g", "good"))
  print(abc_list)         # [('a', 'alphabet'), ('b', 'best'), ('c', 'cheer'), ('g', 'good')]

  # EX2.
  score_dic = {
      "Korean" : 95,
      "Math" : 88,
      "English": 92,
  }

  print("1. items() 출력")
  print(score_dic.items())          # dict_items([('Korean', 95), ('Math', 88), ('English', 92)])
  print()

  print("2. for문 + items() 결합")
  for subject, score in score_dic.items() :
      print(f"{subject}, {score}")          # Korean, 95 | Math, 88 | English, 92
  print()

  print("3. list() + items() 결합")
  score_list = list(score_dic.items())
  print(score_list)           # [('Korean', 95), ('Math', 88), ('English', 92)]

  score_list.append(("Science", 55))
  print(score_list)           # [('Korean', 95), ('Math', 88), ('English', 92), ('Science', 55)]
  ```

<br>

## 튜플 (Tuple)

- 여러 개의 값을 하나의 변수에 저장할 수 있는 자료형
- 리스트와 비슷하지만, 튜플은 수정할 수 없다는 큰 차이점이 있다.
- 튜플 문법
  - 변수명 = (요소1, 요소2, 요소3)
- 리스트 문법

  - 변수명 = [요소1, 요소2, 요소3]

  ```python
  # EX1. 음수 인덱스
  names = ("kim", "lee", "park")
  print(names[-3])            # kim
  print(names[-2])            # lee
  print(names[-1])            # park

  for i in names :
      print(i)            # kim lee park

  # EX2. 튜플 슬라이싱
  example = (3, 9, "y", 2, "k", True)
  print(example[1:4])         # (9, 'y', 2)
  print(example[2:6])         # ('y', 2, 'k', True)
  print(example[0:5])         # (3, 9, 'y', 2, 'k')

  # EX3. 범위를 벗어난 슬라이싱
  print(example[4:8])         # ('k', True)
  # print(example[8])         # 오류 발생
  ```

### 리스트와 튜플의 차이

- 리스트(list) : [] 사용 / 수정 가능 / 크기 변경 가능
- 튜플(tuple) : () 사용 / 수정 불가능 / 크기 고정

```python
# EX1. 리스트와 튜플 요소 수정하기
list3 = [3, 0, 9]
tuple3 = (3, 0, 9)

print(list3)          # [3, 0, 9]
print(tuple3)         # (3, 0, 9)

list3[0] = 30
# tuple[0] = 30   # 오류 발생 : 튜플은 수정할 수 없다.

list3.append(7)
print(list3)          # [30, 0, 9, 7]

# tuple.append(7)
# print(tuple)    # 오류 발생 : 튜플은 수정할 수 없다.
```

### 튜플은 언제 사용할까?

1. 값이 변하지 않아야 할 때
2. 리스트보다 속도가 빠르다.
3. 함수에서 여러 개의 값을 한번에 반환할 때

### 튜플의 메서드

1. count() : 리스트, 튜플, 문자열 등에서 특정 값이 몇 번 나오는지 알려주는 메서드

   - 문법 : 변수명.count(찾을 값)

   ```python
   # EX1
   # list
   numbers = [1, 2, 3, 2, 4, 2]
   print("1) list의 count() :", numbers.count(2))            # 1) list의 count() : 3

   # tuple
   colors = ("red", "blue", "red", "green", "red")
   print("2) tuple의 count() :", colors.count("red"))        # 2) tuple의 count() : 3

   # text
   text = "banana"
   print("3) text의 count() :", text.count("b"))             # 3) text의 count() : 1

   # EX2
   tuple_alphabet = ("a", "a", "b", "c", "c", "a")
   print("a의 개수 :", tuple_alphabet.count("a"))            # a의 개수 : 3
   print("b의 개수 :", tuple_alphabet.count("b"))            # b의 개수 : 1
   print("c의 개수 :", tuple_alphabet.count("c"))            # c의 개수 : 2
   ```

2. index() : 리스트, 튜플, 문자열 등에서 특정 값의 위치(어디에 있는지)를 알려주는 메서드 (첫 등장 위치 or 인덱스)

   - 문법 : 변수명.index(찾을 값)

   ```python
   # EX1
   fruits = ["apple", "banana", "cherry", "banana"]
   print(fruits.index("banana"))           # 1

   # EX2
   nums = (3, 5, 7, 9, 2, 7, 1)
   print(nums.index(7))            # 2
   ```

### 튜플의 활용 - 데이터 교환

- 튜플은 각 요소를 직접 수정할 수 없지만, 두 튜플을 활용하여 간접적으로 튜플 요소의 값을 교환할 수 있다.
- '=' 연산자를 사용하여 새로운 튜플의 값을 기존 튜플 변수에 할당한다

  ```python
  x = 10
  y = 20
  print("교환 전 출력 : x = ", x, ", y = ", y)        # 교환 전 출력 : x =  10 , y =  20

  (x, y) = (y, x)
  print("교환 후 출력 : x = ", x, ", y = ", y)        # 교환 후 출력 : x =  20 , y =  10

  # EX2
  name = "Alice"
  nickName = "Ace"
  print("교환 전 출력 : name = ", name, ", nickName = ", nickName)      # 교환 전 출력 : name =  Alice , nickName =  Ace

  (name, nickName) = (nickName, name)
  print("교환 후 출력 : name = ", name, ", nickName = ", nickName)      # 교환 후 출력 : name =  Ace , nickName =  Alice
  ```

<br>

## 세트 (Set)

- 중복을 허용하지 않고, 순서가 없는 자료형이다
- 세트란?
  - 수학에서 말하는 집합과 비슷하다.(합집합, 교집합, 차집합)
  - 중복된 값을 자동으로 제거한다.
  - 값들의 순서가 없어서 인덱스로는 접근이 불가능하다.

### 세트의 기본 형태

- 변수명 = {요소1, 요소2, 요소3 ... }
- 세트의 표현 방법은 {}
- 다른 자료형을 ㅅ ㅔ트로 변환하고자 할 때, 문법 : set(세트로 바꾸고 싶은 다른 자료형)

```python
# EX1. set로 변환한 자료형들
str2 = "apple"
list2 = [1, 2, 3]
tuple2 = (1, 2, 3)

print("str : ", str2)                 # str :  apple
print("list : ", list2)               # list :  [1, 2, 3]
print("tuple : ", tuple2)             # tuple :  (1, 2, 3)

set_str = set(str2)
set_list = set(list2)
set_tuple = set(tuple2)

print("set_str : ", set_str)          # set_str :  {'a', 'p', 'l', 'e'}
print("set_list : ", set_list)        # set_list :  {1, 2, 3}
print("set_tuple : ", set_tuple)      # set_tuple :  {1, 2, 3}

# EX2. 다양한 자료형 (중복 포함)
num_list = [1, 2, 2, 3, 3, 3, 4]
num_tuple = (5, 5, 6, 7, 6, 7, 7)

print("list 원본 :", num_list)              # list 원본 : [1, 2, 2, 3, 3, 3, 4]
print("tuple 원본 :", num_tuple)            # tuple 원본 : (5, 5, 6, 7, 6, 7, 7)

print("list > set :", set(num_list))        # list > set : {1, 2, 3, 4}
print("tuple > set :",set(num_tuple))       # tuple > set : {5, 6, 7}

# EX3. 리스트와 튜플로 변환하여 세트 요소에 접근하기
str_banana = "banana"
set_banana = set(str_banana)
print(set_banana)               # {'a', 'b', 'n'}

list_banana = list(set_banana)
tuple_banana = tuple(set_banana)
print(list_banana[0])           # a
print(tuple_banana[1])          # b

# EX4. 리스트와 튜플로 변환하여 세트 요소에 접근하기
str_apple = "apple"
set_apple = set(str_apple)
print(set_apple)            # {'a', 'p', 'l', 'e'}

list_apple = list(set_apple)
tuple_apple = tuple(set_apple)

print("list_apple :", list_apple[0])            # list_apple : a
print("tuple_apple :", tuple_apple[1])          # tuple_apple : p

# EX5. n번째로 작은 알파벳 출력하기
str_random = "apbdhwoernzhd"

str_random = set(str_random)
print(str_random)         # {'z', 'a', 'h', 'b', 'r', 'd', 'o', 'e', 'w', 'p', 'n'}

list_str = list(str_random)
print(list_str)           # ['z', 'a', 'h', 'b', 'r', 'd', 'o', 'e', 'w', 'p', 'n']

list_str.sort()
print(list_str)           # ['a', 'b', 'd', 'e', 'h', 'n', 'o', 'p', 'r', 'w', 'z']

print("3번째로 작은 알파벳 :", list_str[3])       # 3번째로 작은 알파벳 : e
print("7번째로 작은 알파벳 :", list_str[7])       # 7번째로 작은 알파벳 : p
print("5번째로 작은 알파벳 :", list_str[5])       # 5번째로 작은 알파벳 : n
```

### 세트의 메서드

- .add()

  - '하나'의 요소를 추가할 때 사용하는 메서드
  - 문법 : 세트.add(요소)

  ```python
  # EX1
  set = {1, 2, 3}
  set.add(4)
  print(set)        # {1, 2, 3, 4}

  set.update({5, 6, 7})
  print(set)        # {1, 2, 3, 4, 5, 6, 7}

    # EX2
  alphabet_set = {"a", "b", "c"}
  alphabet_set.add("d")
  print(alphabet_set)           # {'b', 'a', 'd', 'c'}

  alphabet_set.update({"e", "f", "g"})
  print(alphabet_set)           # {'a', 'd', 'e', 'c', 'g', 'b', 'f'}
  ```

- .update()
  - set에 여러 개의 요소를 한꺼번에 추가할 때 사용한다
  - 문법 : 세트.update(반복가능한\_자료형)
  - 예시 : s.update([1, 2, 3])
- remove(값)

  - 지정한 값을 제거, 그 값이 없으면 error가 발생(KeyError)

  ```python
  # EX1
  s = {1, 2, 3}
  s.remove(2)
  print(s)        # {1, 3}
  #s.remove(5)    # 없는 값 삭제 에러 발생
  ```

- discard()

  - 지정한 값을 제거, 그 값이 없어도 조용히 넘어감 (error 발생 X)

  ```python
  # EX1
  dis = {5, 6, 7}
  dis.discard(6)
  print(dis)          # {5, 7}
  dis.discard(10)     # 없는 값 삭제 에러 발생 X
  ```

- pop()

  - 임의의 요소 하나 제거 + 그 값을 반환
  - 순서가 없으므로 어떤 값이 제거 될 지 모름
  - 비어 있으면 error 발생 (KeyError)

  ```python
  # EX1
  set_d = {"b", "l", "u", "e"}

  # pop메서드를 사용하여 요소를 랜덤으로 제거
  print(set_d)              # {'b', 'u', 'e', 'l'}
  # pop은 삭제 요소를 반환한다.
  print(set_d.pop())        # b
  ```

- clear()

  - 모든 요소 삭제 (세트 초기화)

  ```python
  # EX1
  set_last = {1, 2, 3, 4}
  set_last.clear()
  print(set_last)           # set()
  ```

- **중복된 값을 자동으로 걸러진다**

### 세트의 연산 종류

| 연산 종류 | 기호 또는 메서드         | 의미                            |
| --------- | ------------------------ | ------------------------------- |
| 합집합    | \| 또는 union()          | 모든 요소                       |
| 교집합    | `&` 또는 .intersection() | 공통된 값들만 추출              |
| 차집합    | `-` 또는 .difference()   | 앞 세트에는 있고 뒤에는 없는 값 |

```python
# EX1. 교집합
set_a = {2, 4, 6}
set_b = {3, 6, 9}

# intersection() 메서드를 사용
intersection_AandB = set_a.intersection(set_b)
print(intersection_AandB)           # {6}

# & 연산자를 사용
intersection_AandB = set_a & set_b
print(intersection_AandB)           # {6}

# EX2. 교집합
set_c = {"apple", "banana", "cherry"}
set_d = {"apple", "banana", "orange"}

# 메서드를 이용
print(set_c.intersection(set_d))            # {'banana', 'apple'}

# 연산자를 이용
print(set_c & set_d)            # {'banana', 'apple'}
```

```python
# EX1. 합집합
setA = {2, 4, 6}
setB = {3, 6, 9}

# union() 메서드 사용
union_AandB = setA.union(setB)
print(union_AandB)            # {2, 3, 4, 6, 9}

# 연산자 사용
union_AandB = setA | setB
print(union_AandB)            # {2, 3, 4, 6, 9}
```

```python
# EX1. 차집합
setA = {2, 4, 6}
setB = {3, 6, 9}

# 메서드
diff_AandB = setA.difference(setB)
print(diff_AandB)           # {2, 4}

# 연산자
diff_AandB = setA - setB
print(diff_AandB)           # {2, 4}
```

<br>

## 컬렉션 자료형 비교

| 구분      | 리스트             | 딕셔너리                               | 튜플                         | 세트                             |
| --------- | ------------------ | -------------------------------------- | ---------------------------- | -------------------------------- |
| 괄호 모양 | [ ]                | {key: value}                           | ( )                          | { }                              |
| 저장 방식 | 값(value)들의 모음 | 값(value)들의 모음                     | 값(value)들의 모음           | 중복 없는 값들의 모음            |
| 순서      | 가능               | 가능                                   | 가능                         | 불가능(순서 보장)                |
| 수정      | 가능               | 가능                                   | 불가능                       | 가능                             |
| 인덱싱    | 가능               | 불가능                                 | 가능 tuple[0]                | 불가능                           |
| 중복 허용 | 가능               | 가능                                   | 가능                         | 불가능                           |
| 사용 예시 | 여러 값 저장할 때  | 이름과 점수처럼 키-값 구조가 필요할 때 | 변경되지 않아야 하는 값 모음 | 중복 제거, 집합 연산이 필요할 때 |

### 문자열을 set으로 변환했을 때 순서가 매번 달라지는 데, 숫자 리스트나 튜플은 set으로 바꾸면 순서가 거의 고정되어 있는지?

- @ 해시값 : 데이터(문자, 숫자등)를 일정한 규칙에 따라 고정된 크기의 숫자로 바꾼 값이다.
- = 데이터를 빠르게 찾기 위한 고유 식별 숫자(바뀔 수 있다.)

- 숫자는 해시값이 안정적이다
- 문자열: set()으로 변환 시 매번 달라짐
- 숫자: 변환을 해도 대부분 비슷한 순서이다.

<br>
