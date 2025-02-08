from students_management import *


print("\n*** Test Case 1: All Student Data present***")
students = [
    Student("Robert Doe", 91, 85, 90, 95, 86, 96),
    Student("Christy Roe", 75, 70, 65, 80, 78, 85),
    Student("Maria Jones", 90, 70, 65, 85, 70, 90),
    Student("rani Lee", 88, 70, 65, 85, 70, 90),
    Student("marli Le", 95, 88, 85, 97, 90, 95)
]
# Test Grade Calculations
grade_calc = GradeCalculations(students)

print("*** Calculating Final Grades ***")
for student in students:
    final_grade = grade_calc.calculate_final_grade(student)
    print(f"{student.name}: {final_grade}")

# Sorting
print("\n*** Sorting by Name (Case Insensitive) ***")
grades = grade_calc.calculate_final_grades()
sorted_grades = grade_calc.sort_by_name_case_insensitive(grades)
for grade in sorted_grades:
    print(grade)

print("\n*** Sorting by Name (Case Sensitive) ***")
sorted_grades = grade_calc.sort_by_name_case_sensitive(grades)
for grade in sorted_grades:
    print(grade)

stats = Statistics(students)
stats.compute_quizzes_average_stats()
stats.compute_quizzes_min_stats()
stats.compute_quizzes_max_stats()

print("\n*** Statistics ***")
print("Quiz Averages:", stats.quizzes_average)
print("Quiz Minimums:", stats.quizzes_min)
print("Quiz Maximums:", stats.quizzes_max)

print("\n*** Printing statistics ***")
stats.print_averages_as_columns()
stats.print_statistics()


print("\n*** Test Case 2: Missing Student Data***")
students = [
    Student("Robert Doe"),
    Student("Christy Roe", 88, 70, 85, 80),
    Student("Maria Jones", 90, 75, 69, 85, 87, 91),
    ]
# Test Grade Calculations
grade_calc = GradeCalculations(students)

print("*** Final Grades ***")
for student in students:
    final_grade = grade_calc.calculate_final_grade(student)
    print(f"{student.name}: {final_grade}")

# Sorting
print("\n*** Sorting by Name (Case Insensitive) ***")
grades = grade_calc.calculate_final_grades()
sorted_grades = grade_calc.sort_by_name_case_insensitive(grades)
for grade in sorted_grades:
    print(grade)

print("\n*** Sorting by Name (Case Sensitive) ***")
sorted_grades = grade_calc.sort_by_name_case_sensitive(grades)
for grade in sorted_grades:
    print(grade)

stats = Statistics(students)
stats.compute_quizzes_average_stats()
stats.compute_quizzes_min_stats()
stats.compute_quizzes_max_stats()

print("\n*** Statistics ***")
print("Quiz Averages:", stats.quizzes_average)
print("Quiz Minimums:", stats.quizzes_min)
print("Quiz Maximums:", stats.quizzes_max)

print("\n*** Printing statistics ***")
stats.print_averages_as_columns()
stats.print_statistics()










