student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# 합 구하기 : sum()
total_exam_score = sum(student_scores)
print(total_exam_score)

# 합 구하기 : 수동
sum = 0
for score in student_scores:
    sum += score

print(sum)

# 제일 높은 값 구하기 : max()
highest_core = max(student_scores)
print(highest_core)

# 제일 높은 값 구하기 : 수동
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
