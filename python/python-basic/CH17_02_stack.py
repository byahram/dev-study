"""
2025.04.29 화
"""

print()
print()
print("------------------------")
print("--- 스택이란?")
print("------------------------")
print()

'''
[스택(Stack)이란?]

- LIFO 구조

[스택의 정의]

- 데이터를 쌓아 올리는 형태의 선형 자료구조(Linear Data Structure)로, 
마지막에 넣은 데이터가 가장 먼저 나오는 후입선출(LIFO, Last In First Out) 구조이다.

[스택의 동작 예시]

- 예시 : 책을 쌓는 행위
- 삽입 순서 : A -> B -> C
- 꺼내는 순서 : C -> B -> A (가장 마지막에 넣은 것이 가장 먼저 나오는 구조이다.)

[핵심 구성]

- 삽입(push) : 데이터를 스택의 맨 위(top)에 넣는 작업
    - 삽입(append) : 파이썬에서는 push라는 함수가 없기에 append를 사용해야 한다.
- 삭제(pop) : 스택의 맨 위에서 데이터를 꺼내는 작업
- 조회(peek) : 삭제 없이 스택의 가장 위에 있는 데이터를 확인
- 비어있는지 확인(isEmpty) : 스택에 데이터가 있는지 확인

[스택을 사용하는 이유]

1. 실행 취소 기능 구현
2. 웹 브라우저의 뒤로가기
3. 함수 호출 기록(콜 스택)
4. 괄호 검사기, 수식 계산기 등에서의 구조적 데이터 처리
'''

stack = []

# push
stack.append("A")
stack.append("B")
stack.append("C")

# 현재 스택 상태 출력
print("현재 스택 :", stack)
print()

print("~~~~~위~~~~~")
for item in reversed(stack) :       # 거꾸로 출력
    print(item)     
print("~~~~~~~~~~~~")
print()

# pop
print("pop :", stack.pop())
print()

# 조회
print("peek :", stack[-1])      # stack[-1] : 가장 마지막에 추가된 값을 의미한다.
print()

# 스택이 비어있는지 확인하기
print("스택이 비었나요? ", len(stack) == 0)

print()
print("------------------------")
print()

books = []

books.append("동화책")
books.append("수학 문제집")
books.append("영어단어장")

print(">> 현재 책 더미 출력 :")

for book in books :
    print(book)

print()
print(f"1. {books.pop()}을 꺼냈습니다.")
print(f"2. {books.pop()}을 꺼냈습니다.")

print()

if len(books) > 0 :
    print("맨 위 책 확인 :", books[-1])
else :
    print("책 더미가 비어있습니다.")

print()
print("------------------------")
print()

'''
스택을 이용해서 웹 브라우저의 "뒤로가기" 버튼 기능을 스택으로 구현해보는 예제 만들기
"네이버" => "유튜브" => "위키백과"
뒤로가기를 누르면 -> 유튜브 ->네이버
'''

# 방문한 페이지를 저장하는 스택
history = []

# 페이지 방문 (push, append)
def visit(page) :
    print(f"{page} 페이지에 방문했습니다.")
    history.append(page)
    for page in reversed(history) :
        print("-", page)

# 뒤로가기 (pop)
def go_back() :
    if len(history) == 0 :      # 방문한 기록이 아무것도 없으면, 즉  history가 비어있다면
        print("더 이상 뒤로 갈 수 없습니다.")
    
    else :
        # 가장 마지막에 방문한 페이지를 꺼내기
        last_page = history.pop()
        print(f"`{last_page}` 페이지에서 뒤로 갑니다.")

# 현재 페이지 확인 함수 (peek의 역할)
def current_page() :
    # 방문 기록이 없다면
    if len(history) == 0 :
        return "\n현재 페이지 없음\n"
    
    # 가장 마지막 페이지를 보여주기
    return f"\n현재 페이지 : {history[-1]}\n"

# 방문한 전체 페이지를 출력하는 함수
def print_history() :
    if not history:
        print("\n방문한 페이지가 없습니다.\n")
        return
    
    print("\n방문한 페이지 목록(최신순)")
    for page in reversed(history) :
        print("-", page)
    print("----------------")
    print("처음 페이지")

# 테스트 실행 -> 페이지 방문
visit("네이버")
visit("유튜브")
visit("위키백과")

# 현재 보고 있는 페이지 출력
print(current_page())

# 뒤로가기
go_back()
go_back()
go_back()
print_history()

print()
print("------------------------")
print()

'''
[스택을 활용한 계산기 입력 기록 만들기]

- 이 예제는 스택 구조를 활용하여 사용자가 계산기를 사용하면서 입력한 숫자와 연산자를 기록하고,
되돌리기 기능을 통해 마지막 입력을 삭제할 수 있는 프로그램이다.

[프로그램 구성 설명]

* 입력 기록 저장
1. 사용자가 입력한 숫자나, 기호(+, -, /, *)는 input_stack이라는 리스트에 저장된다.
2. 리스트는 스택처럼 동작하며, append로 추가하고, pop으로 삭제한다.

* 명령 종류
"숫자 또는 연산자" 입력 값을 스택에 저장
- undo : 최근 입력한 내용을 삭제
- print : 현재까지 입력한 내용을 모두 출력
- exit : 프로그램 종료
'''

input_stack = []

# 입력(push)
def push(value) :
    print(f"입력 : {value}")
    input_stack.append(value)

# 최근 입력 삭제(pop)
def undo() :
    if len(input_stack) == 0 :
        print("되돌릴 입력값이 없습니다.")
    else :
        removed = input_stack.pop()
        print(f"되돌리기 : {removed} 삭제됨")

# 현재 입력 상태 출력
def print_state() :
    print("현재 입력 상태 :")

    if len(input_stack) == 0 :
        print("입력 없음")
    else :
        # 여러 문자열을 하나로 붙여주는 함수이다.
        # " " 공백을 넣는다는 의미이다.
        print(" ".join(input_stack))

# 사용자 입력 루프
while True :
    command = input("입력할 값(숫자, +, -, *, /) 또는 undo, print, exit 입력 : ")
    
    if command == "exit" :
        break
    elif command == "undo" :
        undo()
    elif command == "print" :
        print_state()
    else :
        push(command)


'''
[나의 풀이]

input_stack = []

while True : 
    user = input("입력할 값 : ")
    
    if user == "print" :
        print("현재 입력 상태 :")
        for item in input_stack :
            print(item, end=" ")
        break

    elif user == "undo" :
        last_item = input_stack.pop()
        print(f"되돌리기 : {last_item} 삭제됨")
        print("input_stack :", input_stack)
        print()

    else :
        print(f"입력 : {user}")
        input_stack.append(user)
        print("input_stack :", input_stack)
        print()
'''

print()
print()
print("------------------------ 끝")
print()