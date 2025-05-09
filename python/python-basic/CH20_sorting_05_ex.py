'''
2025.05.08 목
'''

print()
print()
print("--------------------------")
print("--- 자료구조 - 정렬 예제")
print("--------------------------")
print()

'''
[숫자 리스트를 입력 받아서 정렬하기]

- 목표 : 사용자로부터 숫자를 입력 받아, 3가지 방식으로 정렬
'''

# 내 풀이
# list = []
# while True :
#     user = int(input("숫자를 입력해주세요 >> "))
#     list.append(user)
    
#     if len(list) > 4 :
#         break

# 선생님 풀이
user_input = input("정렬할 숫자들을 공백으로 입력하세요 : ")
user_list = list(map(int, user_input.split()))

# 버블 정렬
def bubble_sort(arr) :
    n = len(arr)

    for i in range(n) :
        for j in range(n - i - 1) :
            if(arr[j] > arr[j+1]) :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 선택 정렬
def selection_sort(arr) :
    n = len(arr)

    for i in range(n) :
        min_idx = i
        for j in range(i+1, n) :
            if arr[j] < arr[min_idx] :
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# 삽입 정렬
def insertion_sort(arr) :
    for i in range(1, len(arr)) :
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key :
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = key
    
    return arr

print()

print("버블 정렬 결과 :", bubble_sort(user_list))
print("선택 정렬 결과 :", selection_sort(user_list))
print("삽입 정렬 결과 :", insertion_sort(user_list))

'''
[복습]

[ list(map(int, user_input.split())) ]

- 문자열로 구성된 리스트 user_input.split()의 각 요소에 내장 함수 int를 순차적으로 적용하여, 문자열 숫자를 정수형 숫자로 변환하는 반복 가능한 객체(map)를 생성한다.

[ map(int, [...]) ]

- 리스트의 각 요소에 int를 적용하여 정수로 변환된 요소들을 순차적으로 생성하는 map 객체를 반환한다.

[ list(map(int, [...])) ]

- 리스트로 감싸면 정수 리스트로 변환된다.

[ map객체란? ]

- map()함수는 반복 가능한 객체를 반환하는데 이 객체를 map 객체라고 부른다.
- 리스트처럼 보이지만, 실제로는 하나씩 꺼내 쓸 수 있는 값들의 묶음이다.

[ map 객체를 왜 쓸까? ]

- 메모리를 덜 쓰고, 속도가 빠름
- 특히, 큰 데이터를처리할 떄 효율적이다.
- 값이 많을수록 map은 리스트보다 훨씬 가볍다.
'''

print()
print()
print("------------------------ 끝")
print()
