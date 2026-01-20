# Student Marks Analyzer
# Version 2: Advanced with validation and subject-wise report

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


def get_marks(subjects):
    marks_list = []
    for i in range(1, subjects + 1):
        while True:
            marks = int(input(f"Enter marks for subject {i} (0–100): "))
            if 0 <= marks <= 100:
                marks_list.append(marks)
                break
            else:
                print("Invalid marks. Please enter between 0 and 100.")
    return marks_list


# Student details
name = input("Enter student name: ")
subjects = int(input("Enter number of subjects: "))

# Input marks
marks = get_marks(subjects)

# Calculations
total_marks = sum(marks)
percentage = total_marks / subjects
grade = calculate_grade(percentage)

# Output
print("\n--- Student Result ---")
print("Name:", name)

for i, m in enumerate(marks, start=1):
    print(f"Subject {i}: {m}")

print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2))
print("Grade:", grade)
