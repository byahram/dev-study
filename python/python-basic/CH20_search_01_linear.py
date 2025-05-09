'''
2025.05.08 목
'''

print()
print()
print("------------------------")
print("--- 선형 탐색")
print("------------------------")
print()

'''
[선형 탐색의 정의]

- 찾고자 하는 값을 리스트가 처음부터 끝까지 차례대로 하나씩 비교하여 해당 값을 찾는 가장 기본적인 탐색 알고리즘이다.

[방식] 첫 번째 원소부터 마지막 원소까지 순차적으로 비교
[장점] 구현이 매우 간단하고 정렬이 필요 없다.
[단점] 데이터가 많을수록 속도가 느려진다.
'''

# 선형 탐색 예제
def linear_search(arr, target) :
    for i in range(len(arr)) :
        if arr[i] == target :
            return i    # 찾으면 인덱스 반환
    return -1           # 못 찾으면 -1

# 사용자로부터 리스트 입력 받기
user_input = input("정렬할 숫자들을 공백으로 입력하세요 : ")
numbers = list(map(int, user_input.split()))

# 사용자로부터 찾을 값 입력 받기
target = input("찾을 값을 입력하세요 : ")

# 예제 리스트
# numbers = [12, 23, 77, 4, 6, 8]

# 찾을 값
# target = 21

# 함수 호출
result = linear_search(numbers, target)

# 결과 출력
if result != -1 :
    print(f"{target}는 {result}번 인덱스에 있습니다.")
else :
    print(f"{target}은 리스트에 없습니다.")
    
print()
print()
print("------------------------ 끝")
print()
