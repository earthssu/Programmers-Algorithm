N = int(input())
grade = list(map(int, input().split(' ')))
max_grade = max(grade)
new_grade = []

for g in grade:
    new_grade.append(g / max_grade * 100)

print(sum(new_grade) / N)