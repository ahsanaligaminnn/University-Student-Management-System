print("\n==============================================================")
print("|  University Student Management & Result Evaluation System  |")
print("==============================================================\n")

#Student information
student_name = input("Enter Studnet Name : ")
while True:
    age = input("Enter Age : ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("Enter age in a numberic form.")

roll_number = input("Enter Roll Number : ")
department = input("Enter Department : ")
print()

#Subject Marks and store in list
marks = []
for i in range(1,6):
    while True:
        mark = input(f"Enter Subject {i} Mark : ")
        if mark.isdigit():
            mark = int(mark)
            marks.append(mark)
            break
        else:
            print("Invlaid Command.")


def calculate_result(student_name,age,roll_number,department,marks):
    Total_marks = 500
    obtained_marks = sum(marks)
    highest_marks = max(marks)
    lowest_marks = min(marks)
    percentage = obtained_marks/Total_marks*100
    status = None
    student_result = {}

    #check pass or fail
    for mark in marks:
        if mark < 40:
            status = "FAIL"
            break
        else:
            status = "PASS"  

    #Grade Evaluation
    if percentage >=90 and percentage <=100:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"              
    elif percentage >= 70:
        grade = "B"                    
    elif percentage >= 60:
        grade = "C"      
    elif percentage >= 50:
        grade = "D"                              
    else:
        grade = "F"  

    #Add all information in Dist
    student_result['name'] = student_name
    student_result['age'] = age
    student_result['department'] = department
    student_result['rollnumber'] = roll_number
    student_result['Lowest Mark'] = lowest_marks
    student_result['Highest Mark'] = highest_marks
    student_result['total marks'] = Total_marks
    student_result['obtained marks'] = obtained_marks
    student_result['percentage'] = percentage
    student_result['grade'] = grade
    student_result['status'] = status
    return student_result

result = calculate_result(student_name,age,roll_number,department,marks)

def department_message(department):
    return(f"Department of {department} Result.")


dept_msg = department_message(department)

print("\n====================")
print("|  Student Report  |")
print("====================\n")

print(f"Student Name : {result ['name']}")
print(f"Age : {result['age']}")
print(f"Deparment : {result['department']}")
print(f"Roll Number : {result['rollnumber']}\n")
print(f"Total Marks : {result['total marks']}")
print(f"Obtained Marks : {result['obtained marks']}")
print(f"Percentage : {result['percentage']}")
print(f"Grade : {result['grade']}")
print(f"Subject Highest Marks : {result['Highest Mark']}")
print(f"Subject Lowest Marks : {result['Lowest Mark']}")
print(f"Status : {result['status']}\n")
print(dept_msg)

