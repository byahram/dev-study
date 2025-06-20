def is_prime(num):
    """입력된 정수가 소수인지 판별하여 True 또는 False를 반환"""
    if num < 2:
        return False  # 2보다 작은 수는 소수가 아님

    for i in range(2, int(num ** 0.5) + 1):  # 제곱근까지만 확인
        if num % i == 0:
            return False  # 나누어 떨어지면 소수가 아님

    return True  # 끝까지 나누어 떨어지지 않으면 소수

print(is_prime(73))  # True
print(is_prime(75))  # False
print(is_prime(2))   # True
print(is_prime(1))   # False
