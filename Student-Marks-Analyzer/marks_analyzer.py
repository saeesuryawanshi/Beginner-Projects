# Student Marks Analyzer
# This program calculates total marks, percentage, and grade for a student

def calculate_grade(percentage):
    if percentage >= 75:
        return "Distinction"
    elif percentage >= 60:
        return "First Class"
    elif percentage >= 50:
        return "Second Class"
    elif percentage >= 40:
        return "Pass"
    else:
        return "Fail"


# Take student details
name = input("Enter student name: ")

# Take marks input
subjects = int(input("Enter number of subjects: "))
total_marks = 0

for i in range(1, subjects + 1):
    marks = int(input(f"Enter marks for subject {i}: "))
    total_marks += marks

# Calculations
percentage = total_marks / subjects
grade = calculate_grade(percentage)

# Output
print("\n--- Result ---")
print("Student Name:", name)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2))
print("Grade:", grade)
