n=int(input())

students = []
for i in range(n):
    name, score = input().split()
    students.append((name, int(score)))

students.sort(key=lambda student: student[1])
sort_students = sorted(students, key=lambda student: student[1])
# 람다식 기억하기

# print(students)