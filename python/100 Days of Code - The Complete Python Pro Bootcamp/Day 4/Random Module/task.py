import random

random_integer = random.randint(1, 10)      # 1, 10 포함
print(random_integer)

random_number_0_to_1 = random.random() * 10         # 1 포함, 10 미포함
print(random_number_0_to_1)

random_float = random.uniform(1, 10)      # 1, 10 포함
print(random_float)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
