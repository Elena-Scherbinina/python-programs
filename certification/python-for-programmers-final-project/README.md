# **Student Grades and Statistics Program**

## **Project Summary**
This Python program determines students' letter grades in a university course and computes statistics for quizzes, midterms, and final exams. It handles file input/output, implements sorting mechanisms, and calculates weighted averages.

## **Features**
- Read student data from an **input CSV file**.
- Compute **final scores** and determine **letter grades**.
- Sort student names **case-sensitive** and **case-insensitive**.
- Compute **class statistics** (average, min, max for quizzes, midterm, and final).
- Output grades and statistics to a **file** and display results in the console.

## **Installation & Usage**
### **1. Prerequisites**
Ensure you have Python installed (Python 3.x recommended).

### **2. Clone the Repository**
```sh
 git clone https://github.com/Elena-Scherbinina/python-programs.git
 cd python-programs/python-for-programmers-final-project
```

### **3. Run the Program**
```sh
python student_management.py input_file.txt output_file.txt
```

## **Task Details**

### **1. File Handling**
- **Input:** Read student data from a CSV file.
- **Output:** Write computed letter grades to an output file.

### **2. Data Processing**
- Compute final scores using the formula:
```python
Final_Score = (quiz1 * 0.15) + (quiz2 * 0.15) + (quiz3 * 0.15) + 
              (quiz4 * 0.15) + (midterm * 0.20) + (final * 0.20)
```
- Assign letter grades based on thresholds:
  - **A**: ≥ 90%
  - **B**: 80-89%
  - **C**: 70-79%
  - **D**: 60-69%
  - **F**: ≤ 59%

### **3. Sorting Requirements**
- **Case-sensitive sorting** of student names.
- **Case-insensitive sorting** of student names.

### **4. Statistics Computation**
- Compute **average, minimum, and maximum** scores for quizzes, midterms, and finals.
- Display class statistics in two formats:
  1. **Scores as columns, averages as rows.**  
  2. **Averages as columns, scores as rows.**  

## **Program Structure**
The project consists of four main classes:

- **FileHandling** – Reads and writes student data.
- **Student** – Represents a student with attributes (name, quiz scores, midterm, final).
- **GradeCalculations** – Computes final scores, assigns letter grades, and sorts students.
- **Statistics** – Calculates quiz, midterm, and final exam statistics and displays them.

## **Error Handling**
- Missing or non-numeric data defaults to 0.
- Floating-point precision is handled with rounding.
- File errors (FileNotFoundError, I/O issues) are managed using try-except blocks.

## **Testing**
The test suite **student_management_test.py** verifies:
- ✅ Grade calculations
- ✅ Sorting mechanisms
- ✅ Statistical computations
