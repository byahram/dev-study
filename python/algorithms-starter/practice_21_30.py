# 21. len()
print("[21.]")
txt = "show me the money"
print(len(txt))
print()

# 22. split()
print("[22.]")
txt = "show me the money"
print(txt.split(" "))
print()

# 23. find()
print("[23.]")
rainbow = "빨주노초파남보"
print(rainbow.find("노"))
print()

# 24. in
print("[24.]")
hello = "hello world"
print("a" in hello)
print()

# 25. strip(), lstrip(), rstrip()
print("[25.]")
name = "   홍길동    "
print(name.strip())
print(name.lstrip())
print(name.rstrip())
print()

# 26. upper(), lower()
print("[26.]")
hello = "hello world"
HELLO = "HELLO WORLD"
print(hello.upper())
print(HELLO.lower())
print()

# 27. 문자열 슬라이싱 1
print("[27.]")
proverb = "By doubting we come at the truth"
print(proverb[15:19])
print()

# 28. 문자열 슬라이싱 2
print("[28.]")
proverb = "By doubting we come at the truth"
print(proverb[-5:])
print()

# 29. replace()
print("[29.]")
txt = "Life is long, you need python"
print(txt.replace("long", "short"))
print()

# 30. 알고리즘 - 통신료 구하기
print("[30.]")
phone = 825900
monthly_fee = 14900
period = 2
bill = monthly_fee * period * 12
total = bill + phone
print("{}년간 총 통신료는 {}원 입니다.".format(period, total))
print()
