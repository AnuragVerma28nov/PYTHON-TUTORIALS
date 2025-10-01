# Sum of Dictionary Values 

student_marks = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    student_marks[name] = marks
print("Sum of marks:", sum(student_marks.values()))