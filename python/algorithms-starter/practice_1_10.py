# 1. 출력문 출력하기
print("[1.]")
print("it's fine")
print("it\'s fine")
print("""it's fine""")
print()

# 2. 한줄 주석과 여러줄 주석 사용하기
print("[2.]")
print()

# 3. 큰 따옴표 포함 출력
print("[3.]")
print("\"Life is too short, we need python!\"")
print(""""Life is too short, we need python!" """)
print()

# 4. 
print("[4.]")
print("you\'ll only see a \"C:\\Program Files\" folder.")
print("""you'll only see a "C:\Program Files" folder.""")
print()

# 5. 연산자 사용하기
print("[5.]")
print("-" * 30)
print("절취선")
print("-" * 30)
print()

# 6. type() 함수 사용하기
print("[6.]")
num1 = "72"
num2 = 72
print(f"a는 {type(num1)} 데이터이고 b는 {type(num2)} 데이터이다.")
print()

# 7.
print("[7.]")
num1 = "72"
num2 = 72
print(int(num1) == num2)
print()

# 8. 스페이스 바를 사용하지 않고 출력 
print("[8.]")
print("아버지가", "방에", "들어가신다.")
print()

# 9. 하나의 print() 함수 사용하기 
print("[9.]")
print("서울에서 제주도를 가는 방법 \n 1. 비행기를 탄다. \n 2. 수영을 한다.")
print("""서울에서 제주도를 가는 방법
1. 비행기를 탄다.
2. 수영을 한다.""")
print()

# 10. 하나의 print() 함수 사용하기 
print("[10.]")
a = 2
b = 4
print(f"{a + b} {a - b} {a * b} {a / b}")
print(a + b, a - b, a * b, a / b)
print()
