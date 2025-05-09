# 11. 문자열 포매팅 사용하기 
print("[11.]")
age = 31
height = 169.4
print("준빈이는 올해 {}살, 키는 {}cm이다.".format(age, height))
print("준빈이는 올해 %d살, 키는 %.1fcm이다." % (age, height))
print()

# 12. 서식지정자 사용하기 
print("[12.]")
name, age = "람머스", 70
print("나의 이름은 %s이고, 나이는 %d살이다." % (name, age))
print()

# 13. sep 옵션 
print("[13.]")
print("철수", "영희", "민수", "나")
print("철수", "영희", "민수", "나", sep="랑")
print()

# 14. 제곱 출력 
print("[14.]")
n, m = 2, 3
print(n ** m)
print()

# 15. 연산 우선순위 
print("[15.]")
print(8 / 2 * (3 + 2))
print()

# 16. end 옵션 
print("[16.]")
print("hello", end=" ")
print("python")
print()

# 17.
print("[17.]")
price = 20000
sale = 80 / 100
print(f"정상가격 : {price}원")
print(f"20% 할인 적용 가격 : {price * sale}원")
print()

# 18. 변수의 데이터 타입 
print("[18.]")
print(type(15), type(0.13), type("홍길동"), type([1, 2, 3]), type((1, 3, 5)), type({3, 5, 7}))
print()

# 19. 서식 지정자 % 사용하여 문자열 포매팅  
print("[19.]")
age, name, height = 34, "김진우", 184.5
print("내 이름은 %s, 나이는 %d살이고 키는 %.1f이다." % (name, age, height))
print()

# 20. 문자열 슬라이싱 
print("[20.]")
txt = "show me the money"
print(txt[8])
print()
