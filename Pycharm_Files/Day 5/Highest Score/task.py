student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

min_score = max_score
for other_score in student_scores:
    if other_score < min_score:
        min_score = other_score
print(min_score)
