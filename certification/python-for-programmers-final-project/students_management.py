import csv
import argparse

FILE_INPUT_STUDENTS = "Input_Final_Sample_Data.txt"
FILE_OUTPUT_GRADES1 = "Output_Grades_case_sensitive.txt"
FILE_OUTPUT_GRADES2 = "Output_Grades_case_insensitive.txt"
class FileHandling:
    students:list

    def __init__(self):
        self.students = []


    def read_students_information(self, file_path):
        '''Read student data from csv file and create list of Student objects'''
        try:
            with open(file_path, newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                 if not row:
                     continue

                 try:
                     #It should be 7 fields in the row
                     if len(row) < 7:
                         print(f"Warning! : There are not enough data for student {row[0]}")
                     student = Student(
                      row[0],       #name
                      int(row[1]),  #quize_1
                      int(row[2]),  #quize_2
                      int(row[3]),  #quize_4
                      int(row[4]),  #quize_4
                      int(row[5]),  #midterm
                      int(row[6])   #final
                     )

                     self.students.append(student)
                 except (IndexError, ValueError) as e:
                     print(f"Error parsing row {row}: {e}")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except IOError as e:
            print(f"Error reading file '{file_path}': {e}")
        except Exception as e:
            print(f"An unexpected error: {e}")


        return self.students

    def write_students_to_file(self, file_path, grades):
        '''Write student grades to a file'''
        try:
            with open(file_path, "w") as file:
                for s in grades:
                    file.write(s[0]+ " : " + s[1] + "\n")
        except IOError as e:
            print(f"Error writing to file '{file_path}': {e}")
        except Exception as e:
            print(f"An unexpected error: {e}")

    def print_students(self):
        for student in self.students:
            # Print the string returned by print_student()
            print(student.print_student_grade())



class Student:
    def __init__(self, name, quiz_1=None, quiz_2=None, quiz_3=None, quiz_4=None, midterm=None, final=None):
        self.name = name
        n = name
        self.quiz_1 = quiz_1 if quiz_1 is not None else 0
        self.quiz_2 = quiz_2 if quiz_2 is not None else 0
        self.quiz_3 = quiz_3 if quiz_3 is not None else 0
        self.quiz_4 = quiz_4 if quiz_4 is not None else 0
        self.midterm = midterm if midterm is not None else 0
        self.final = final if final is not None else 0
        if None in [quiz_1, quiz_2, quiz_3, quiz_4, midterm, final]:
            print(f"Data error : Data are missing for student {name}. Missing values are set to 0.")




class GradeCalculations:
    students:list


    def __init__(self, students):
        self.students = students

    def get_score(self, student):
        """
        Calculates the final score for a student.

        :param student: A Student object
        :return: The calculated final score as an integer.
        If an error occurs, it returns 0 and prints the error message.
        """
        try:
            final_score = (
                int(student.quiz_1 * .15) + int(student.quiz_2 *.15) + int(student.quiz_3 *.15) + int(student.quiz_4 * .15) +
                int(student.midterm * 0.20) + int(student.final * 0.20)
        )
        except (ValueError, TypeError) as e:
            print(f"Error in get_score(self, student) method for {student.name}: {e}")
            final_score = 0
        return final_score

    def calculate_final_grade(self, student):
        """
        Determines the final grade for a student based on their final score.
        :param student: A student object
        :return: The final grade ('A', 'B', 'C', 'D', or 'F').
        If an error occurs, it returns 'F' and prints the error message.
        """
        try:
            score = self.get_score(student)
            if score >= 90:
                return 'A'
            elif 80 <= score <= 89:
                return 'B'
            elif 70 <= score <= 79:
                return 'C'
            elif 60 <= score <= 69:
                return 'D'
            else:
                return 'F'
        except Exception as e:
            print(f"Error calculating final grade for {student.name}: {e}")
            return 'F'



    def calculate_final_grades(self):
        """
        Calculates the final grades for all students in the list.
        :return: A list of tuples with the student's name and final grade.
        In case of an error, it prints the error message
        """
        grades = []
        for student in self.students:
            try:
                final_score = self.get_score(student)
                final_grade = self.calculate_final_grade(student)
                grade = (student.name, final_grade)
                grades.append(grade)
            except Exception as e:
                print(f"Processing student {student.name} error in calculate_final_grades(self): {e}")
        return grades

    def get_name_lowcase(self, grade):
        """
        Converts the student's name to lowercase for case-insensitive sorting.

        :param grade: A tuple containing the student's name and final grade.
        :return: The student's name in lowercase.
        """
        return grade[0].lower()

    def get_name(self, grade):
        """
        Returns the student's name for case-sensitive sorting.
        :param grade: A tuple containing the student's name and final grade.
        :return: The student's name.
        """
        return grade[0]

    def sort_by_name_case_insensitive(self, grades):
        """
        Case-insensitive sort by student names.
        :param grades: A list of tuples with student's name and final grade.
        :return: A sorted list of grades by student names.
        """
        try:
            return sorted(grades, key=self.get_name_lowcase)
        except Exception as e:
            print(f"Error in sort_by_name_case_insensitive(self, grades): {e}")
            return grades

    def sort_by_name_case_sensitive(self, grades):
        """
        Case-sensitive sort by student names.
        :param grades: A list of tuples with student's name and final grade.
        :return: A sorted list of grades by student names.
        """
        try:
            return sorted(grades, key=self.get_name)
        except Exception as e:
            print(f"Error in sort_by_name_case_sensitive(self, grades): {e}")
            return grades



class Statistics:
    def __init__(self, students):
        self.students = students
        self.quizzes_average = {}
        self.quizzes_min = {}
        self.quizzes_max = {}


    def compute_quizzes_average_stats(self):
        """
        Computes the average score for each quiz, midterm, and final exam for students list.
        Round average to 2 decimal points to handle floating points arithmetic issues.
        """
        if len(self.students) == 0:
            print("Students list is empty.")
            return
        total_quiz1 = 0
        for student in self.students:
            total_quiz1 += student.quiz_1
        #round
        self.quizzes_average['quiz1'] =  round(total_quiz1/len(self.students), 2)

        total_quiz2 = 0
        for student in self.students:
            total_quiz2 += student.quiz_2
        self.quizzes_average['quiz2'] = round(total_quiz2 / len(self.students), 2)

        total_quiz3 = 0
        for student in self.students:
            total_quiz3 += student.quiz_3
        self.quizzes_average['quiz3'] = round(total_quiz3 / len(self.students), 2)

        total_quiz4 = 0
        for student in self.students:
            total_quiz4 += student.quiz_4
        self.quizzes_average['quiz4'] = round(total_quiz4 / len(self.students), 2)

        total_midterm = 0
        for student in self.students:
            total_midterm += student.midterm
        self.quizzes_average['midterm'] = round(total_midterm/ len(self.students), 2)

        total_final = 0
        for student in self.students:
            total_final += student.final
        self.quizzes_average['final'] = round(total_final / len(self.students), 2)



    def compute_quizzes_min_stats(self):
        """
        Computes the minimum score for each quiz, midterm, and final exam.
        """
        try:
            list_quiz1 = [ student.quiz_1 for student in self.students]
            if list_quiz1:
                self.quizzes_min["quiz1"] = min(list_quiz1)
            else:
                self.quizzes_min["quiz1"] = 0

            list_quiz2 = [ student.quiz_2 for student in self.students]
            if list_quiz2:
                self.quizzes_min["quiz2"] = min(list_quiz2)
            else:
                self.quizzes_min["quiz2"] = 0

            list_quiz3 = [ student.quiz_3 for student in self.students]
            if list_quiz3:
                self.quizzes_min["quiz3"] = min(list_quiz3)
            else:
                self.quizzes_min["quiz3"] = 0

            list_quiz4 = [ student.quiz_4 for student in self.students]
            if list_quiz4:
                self.quizzes_min["quiz4"] = min(list_quiz4)
            else:
                self.quizzes_min["quiz4"] = 0

            list_midterm = [ student.midterm for student in self.students]
            if list_midterm:
                self.quizzes_min["midterm"] = min(list_midterm)
            else:
                self.quizzes_min["midterm"] = 0

            list_final = [student.final for student in self.students]
            self.quizzes_min["final"] = min(list_final)
            if list_final:
                self.quizzes_min["final"] = min(list_final)
            else:
                self.quizzes_min["final"] = 0
        except AttributeError as e:
            print(f"Error: Missing attribute in compute_quizzes_min_stats(self): {e}")
        except ValueError as e:
            print(f"Error: Invalid value for a student in compute_quizzes_min_stats(self): {e}")


    def compute_quizzes_max_stats(self):
        """
        Computes the maximum score for each quiz, midterm, and final exam.
        """
        try:
            list_quiz1 = [ student.quiz_1 for student in self.students]
            self.quizzes_max["quiz1"] = max(list_quiz1)
            if list_quiz1:
                self.quizzes_max["quiz1"] = max(list_quiz1)
            else:
                self.quizzes_max["quiz1"] = 0

            list_quiz2 = [ student.quiz_2 for student in self.students]
            if list_quiz2:
                self.quizzes_max["quiz2"] = max(list_quiz2)
            else:
                self.quizzes_max["quiz2"] = 0

            list_quiz3 = [ student.quiz_3 for student in self.students]
            if list_quiz3:
                self.quizzes_max["quiz3"] = max(list_quiz3)
            else:
                self.quizzes_max["quiz3"] = 0

            list_quiz4 = [ student.quiz_4 for student in self.students]
            if list_quiz4:
                self.quizzes_max["quiz4"] = max(list_quiz4)
            else:
                self.quizzes_max["quiz4"] = 0

            list_midterm = [ student.midterm for student in self.students]
            if list_quiz4:
                self.quizzes_max["midterm"] = max(list_midterm)
            else:
                self.quizzes_max["midterm"] = 0

            list_final = [student.final for student in self.students]
            if list_quiz4:
                self.quizzes_max["final"] = max(list_final)
            else:
                self.quizzes_max["final"] = 0
        except AttributeError as e:
            print(f"Error: Missing attribute in compute_quizzes_max_stats(self): {e}")
        except ValueError as e:
            print(f"Error: Invalid value for a student in compute_quizzes_max_stats(self): {e}")



    def print_statistics(self):
        '''
        Prints the average, minimum, and maximum scores for each quiz, midterm, and final exam
        '''

        for quiz_num in range(1, 5):
            print(f"Quiz {quiz_num} - Average: {self.quizzes_average[f'quiz{quiz_num}']:.2f}, "
                  f"Min: {self.quizzes_min[f'quiz{quiz_num}']}, "
                  f"Max: {self.quizzes_max[f'quiz{quiz_num}']}")

        print(f"Midterm - Average: {self.quizzes_average['midterm']:.2f}, "
              f"Min: {self.quizzes_min['midterm']}, "
              f"Max: {self.quizzes_max['midterm']}")

        print(f"Final - Average: {self.quizzes_average['final']:.2f}, "
              f"Min: {self.quizzes_min['final']}, "
              f"Max: {self.quizzes_max['final']}")


    def print_scores_as_columns(self):
        """
        Prints the average, minimum, and maximum for each quiz, midterm, and final, having
        Average, Minimum, and Final as rows.
        """

        header = f"{'':<8} | {'Quiz 1':>6} | {'Quiz 2':>6} | {'Quiz 3':>6} | {'Quiz 4':>6} | {'Midterm':>7} | {'Final':>6}"
        line = '-' * 65
        print(line)
        print(header)
        print(line)
        print(
             f"{'Average':<8} | {self.quizzes_average['quiz1']:>6.2f} | {self.quizzes_average['quiz2']:>6.2f} | "
             f"{self.quizzes_average['quiz3']:>6.2f} | {self.quizzes_average['quiz4']:>6.2f} | "
             f"{self.quizzes_average['midterm']:>7.2f} | {self.quizzes_average['final']:>6.2f}")
        print(f"{'Minimum':<8} | {self.quizzes_min['quiz1']:>6} | {self.quizzes_min['quiz2']:>6} | "
               f"{self.quizzes_min['quiz3']:>6} | {self.quizzes_min['quiz4']:>6} | "
               f"{self.quizzes_min['midterm']:>7} | {self.quizzes_min['final']:>6}")

        print(f"{'Maximum':<8} | {self.quizzes_max['quiz1']:>6} | {self.quizzes_max['quiz2']:>6} | "
               f"{self.quizzes_max['quiz3']:>6} | {self.quizzes_max['quiz4']:>6} | "
               f"{self.quizzes_max['midterm']:>7} | {self.quizzes_max['final']:>6}")
        print(line)



    def print_averages_as_columns(self):
        """
        Prints the average, minimum, and maximum scores for each quiz, midterm and final, having
        Average, Minimum and Maximum values as columns.
        """
        header = f"{'':<7} | {'Average':>8} | {'Minimum':>8} | {'Maximum':>8}"
        line = '-' * 42

        print(line)
        print(header)
        print(line)

        print(f"{'Quiz 1':<7} | {self.quizzes_average['quiz1']:>8.2f} | {self.quizzes_min['quiz1']:>8} | {self.quizzes_max['quiz1']:>8}")
        print(f"{'Quiz 2':<7} | {self.quizzes_average['quiz2']:>8.2f} | {self.quizzes_min['quiz2']:>8} | {self.quizzes_max['quiz2']:>8}")
        print(f"{'Quiz 3':<7} | {self.quizzes_average['quiz3']:>8.2f} | {self.quizzes_min['quiz3']:>8} | {self.quizzes_max['quiz3']:>8}")
        print(f"{'Quiz 4':<7} | {self.quizzes_average['quiz4']:>8.2f} | {self.quizzes_min['quiz4']:>8} | {self.quizzes_max['quiz4']:>8}")
        print(f"{'Midterm':<7} | {self.quizzes_average['midterm']:>8.2f} | {self.quizzes_min['midterm']:>8} | {self.quizzes_max['midterm']:>8}")
        print(f"{'Final':<7} | {self.quizzes_average['final']:>8.2f} | {self.quizzes_min['final']:>8} | {self.quizzes_max['final']:>8}")
        print(line)





def main():
    parser = argparse.ArgumentParser(description='Calculating student grades.')
    parser.add_argument('input_file', help='The name of the input file with student data.')
    parser.add_argument('output_file', help='The name of the output file.')
    args = parser.parse_args()

    file = FileHandling()
    # Read students information from the input file
    students = file.read_students_information(args.input_file)

    # Calculate the final grades
    grades_calculations = GradeCalculations(students)
    grades = grades_calculations.calculate_final_grades()

    # Sort grades case insensitive
    grades_sorted_case_insensitive = grades_calculations.sort_by_name_case_insensitive(grades)
    # Sort grades case sensitive
    grades_sorted_case_sensitive = grades_calculations.sort_by_name_case_sensitive(grades)

    # Write the sorted grades to the output file, defined in command line arguments
    file.write_students_to_file(args.output_file, grades_sorted_case_insensitive)
    # Write the sorted case-sensitively grades to the output file FILE_OUTPUT_GRADES1
    file.write_students_to_file(FILE_OUTPUT_GRADES1, grades_sorted_case_sensitive)

    #Compute statistics
    stats = Statistics(students)
    stats.compute_quizzes_average_stats()
    stats.compute_quizzes_min_stats()
    stats.compute_quizzes_max_stats()

    stats.print_scores_as_columns()
    stats.print_averages_as_columns()


if __name__ == '__main__':
    main()



