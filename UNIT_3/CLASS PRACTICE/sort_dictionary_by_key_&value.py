#  Sort Dictionary by Key and Value

student_marks = {'John': 85, 'Emma': 90, 'Michael': 78}
print("Sorted by key (ascending):", dict(sorted(student_marks.items())))
print("Sorted by key (descending):", dict(sorted(student_marks.items(), reverse=True)))
print("Sorted by value (ascending):", dict(sorted(student_marks.items(), key=lambda item: item[1])))
print("Sorted by value (descending):", dict(sorted(student_marks.items(), key=lambda item: item[1], reverse=True)))