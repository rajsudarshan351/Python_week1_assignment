def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


print("Student Grade Calculator")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

average = calculate_average(marks)
grade = assign_grade(average)

print("\nAverage Marks:", average)
print("Grade:", grade)