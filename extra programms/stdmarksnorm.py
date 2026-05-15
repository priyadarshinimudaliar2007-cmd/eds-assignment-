import numpy as np

student_marks = np.array([
    [85, 78, 92],
    [90, 88, 85],
    [75, 92, 88]
])


bonus_marks = np.array([5, 10, 3])

marks_with_bonus = student_marks + bonus_marks

print("Original Marks:")
print(student_marks)
print("\nBonus Marks per Subject:")
print(bonus_marks)
print("\nMarks after adding Bonus:")
print(marks_with_bonus)