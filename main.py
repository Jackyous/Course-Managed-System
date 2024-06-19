#Jacky Zhou
# Mr. David Park - ICS 4U
# 2024/
# AOL 4 - School Management System

import os

class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
class Student(Person):
    def __init__(self,name,grade,age):
        super().__init__(name,age)
        self._grade = grade
    def get_info(self):
        print(f"student's name: {self._name}\nstudent's age: {self._age}\nstudent's grade: {self._grade}")

class Teacher(Person):
    def __init__(self,name,roll,age):
        super().__init__(name,age)
        self._roll = roll

    def get_info(self):
        print(f"teacher's name: {self._name}\nteacher's age: {self._age}\nteacher's roll: {self._roll}")

class Course:
    def __init__(self):
        self.student_list = []
        self.teacher_list = []
        self.teacher_name_list = []

    def append_student(self,course_name):
        self.course_name = course_name
        num = 1
        sum_average_grade = 0
        sum_attendance_percentage = 0
        name = str(input("Type student's name"))
        grade = int(input("Type student's grade"))
        age = int(input("Type student's age"))
        average_grade = int(input("Type the student's average grade in this course"))
        attendance_day = int(input("How many days do student show up in this course (Total school day is 195)"))
        student_number = str(input("Type a student number for this student"))
        attendance_percentage = round(attendance_day / 195 * 100,1)
        student_dict = {"name":name, "grade":grade, "age":age, "average_grade":average_grade,"attendance_percentage":attendance_percentage,
                        "student_number":student_number}
        self.student_list.append(student_dict)
        for i in self.student_list:
            average_grade_1 = i.get("average_grade")
            attendance_1 = i.get("attendance_percentage")
            sum_average_grade += average_grade_1
            sum_attendance_percentage += attendance_1
        class_average = sum_average_grade / len(self.student_list)
        class_attendance_percentage = round(sum_attendance_percentage / len(self.student_list),1)
        print(f"The course average is {class_average}, and the average course attendance percentage is {class_attendance_percentage}%")
        print(f"{self.course_name} has {len(self.student_list)} student/students, including:")
        for dict in self.student_list:
            student_name = dict.get("name")
            student_number = dict.get("student_number")
            print(f"{num}.    name:  {student_name}, student_number:  {student_number}")
            num += 1
    def assign_teacher(self,course_name):
        self.course_name = course_name
        num = 1
        name = str(input("Type teacher's name"))
        role = str(input("Type teacher's role"))
        age = int(input("Type teacher's age"))
        teacher_dict = ({"name": name, "role": role, "age": age})
        self.teacher_list.append(teacher_dict)
        for dict in self.teacher_list:
            teacher_name = dict.get("name")
            teacher_role = dict.get("role")
            print(f"{num}.    name:  {teacher_name}, role:  {teacher_role}")
            num += 1
        print(f"is responsible for {self.course_name} now")

course_list = [] # stores courses
temp_list = []    # Temporary lists always store "num1" and the students/teachers/courses names
temp_list_1 = []
temp_list_3 = []
num1 = 1 # create a variable to make a sequence for students, teachers, and courses
is_create = 0 # create a variable to check if course is create

print("                                             ---Welcome to course managed system---")
while True:
    command = str(input("  Type command(number)\n1.    Create a course\n2.    Manage courses\n3.    Save Edit\n4.    Exit program\n"))   # Main menu
    if command == "1": # create a course
        course_class = input("Type the course's name")
        if course_class == "":
            print("course's name cannot be empty!")
        else:
            course_name = course_class
            course_class = Course()
            course_dict = {"course_name":course_name, "course_class":course_class}
            course_list.append(course_dict)
            print(f"{course_name} is created")
            is_create += 1  # course is create

    elif command == "2": # manage courses
        if is_create > 0:
            while True:
                if len(course_list) == 0:
                    print("There is no course left (Automatically back to last step)")
                    break
                print("Course list:")
                num1 = 1
                for dict in course_list:                             # printing a sequence to let user choose
                    course_name_3 = dict.get("course_name")
                    course_class_3 = dict.get("course_class")
                    print(f"{num1}.    {course_name_3}")
                    dict.update({"course_num":str(num1)})         # update new number for each course
                    num1 += 1
                course_num = input("Which course you want to manage(Type the number, Type esc to back to menu)")          # chose course to operate
                if course_num == "esc":
                    break
                elif  course_num == "" or int(course_num) <= 0 or int(course_num) > num1-1:
                    print("-The number is out of range-")
                else:
                    course_num_1 = course_list[int(course_num) - 1].get("course_num")                    # get course info
                    course_name_1 = course_list[int(course_num) - 1].get("course_name")
                    course_class_1 = course_list[int(course_num) - 1].get("course_class")
                    if str(course_num_1) == course_num:
                        while True:
                            command1 = input("1. add students\n2. add teacher to this course\n3. manage student\n4. manage teacher\n" # Course's operation menu
                                             "5. Delete this course \n6. View crew's info\n(Type esc to go back to main menu)")
                            if command1 == "1":
                                course_class_1.append_student(course_name_1)
                                num1 = 1
                            elif command1 == "2":
                                course_class_1.assign_teacher(course_name_1)
                                num1 = 1
                            elif command1 == "3": # manage with students
                                while True:
                                    if len(course_class_1.student_list) == 0:
                                        print(
                                            "this course does not have any student now")
                                        break
                                    else:
                                        print("Student list:")                 # Showing students list
                                        num1 = 1
                                        for dict in course_class_1.student_list:
                                            student_name = dict.get("name")
                                            student_number = dict.get("student_number")
                                            print(f"{num1}.    name:  {student_name}, student_number:  {student_number}")
                                            num1 += 1
                                        student_num_input = str(input("Which student you want to manage? (Type student number or type esc to go back to course manage menu)"))
                                        for dict_2 in course_class_1.student_list:
                                            if dict_2.get("student_number") == student_num_input:
                                                student_input = str(input("You want to 1. change info or 2. delete (Type esc to go back to selection)"))
                                                if student_input == "1":   # Refresh student's info
                                                    course_class_1.student_list.remove(dict_2)
                                                    course_class_1.append_student(course_name_1)
                                                elif student_input == "2": # Delete student
                                                    course_class_1.student_list.remove(dict_2)
                                                    print("student has been deleted from this course")
                                                    num1 = 0
                                                elif student_input == "esc":
                                                    break
                                        if student_num_input == "esc" or course_num == "":
                                            break
                                        elif num1 != 0:
                                            print("-Invalid command-")

                            elif command1 == "4": # manage teacher
                                while True:
                                    if len(course_class_1.teacher_list) == 0:
                                        print("this course does not have any teacher now")
                                        break
                                    else:
                                        print("Teacher list:")         # Showing teacher list
                                        num1 = 1
                                        for dict in course_class_1.teacher_list:
                                            teacher_name = dict.get("name")
                                            teacher_role = dict.get("role")
                                            temp_dict = {"num":num1,"name":teacher_name,"role":teacher_role}
                                            temp_list_3.append(temp_dict)
                                            print(
                                                f"{num1}.    teacher_name:  {teacher_name}, teacher_role:  {teacher_role}")
                                            num1 += 1
                                        teacher_num_input = str(input(
                                            "Which teacher you want to manage? (Type number or type esc to go back to course manage menu)"))
                                        for temp_dict in temp_list_3:
                                            teacher_name_1 = temp_dict.get("name")
                                            teacher_num_1 = temp_dict.get("num")
                                            if str(teacher_num_1) == teacher_num_input:
                                                for teacher_dict in course_class_1.teacher_list:
                                                    teacher_name_2 = teacher_dict.get("name")
                                                    if teacher_name_2 == teacher_name_1:
                                                        teacher_input = str(input("You want to 1. change info or 2. delete (Type esc to go back to selection)"))
                                                        if teacher_input == "1":  # Refresh teacher's info
                                                            course_class_1.teacher_list.remove(teacher_dict)
                                                            course_class_1.assign_teacher(course_name_1)
                                                        elif teacher_input == "2":  # Delete teacher
                                                            course_class_1.teacher_list.remove(teacher_dict)
                                                            print("teacher has been deleted from this course")
                                                            num1 = 0
                                                        elif teacher_input == "esc":
                                                            break

                                        if teacher_num_input == "esc":
                                            break
                                        elif num1 != 0:
                                            print("-Invalid command-")

                            elif command1 == "5": # Delete course
                                for dict in course_list:
                                    course_name = dict.get("course_name")
                                    if course_name == course_name_1:
                                        course_list.remove(dict)
                                        print("This course has been deleted")
                                        is_create -= 1   # Course minus one, to make sure the checking part at the first of the main menu's command 2(manage courses) works
                                        break
                                break

                            elif command1 == "6": # view students and teachers
                                print("Student list:")
                                if len(course_class_1.student_list) == 0:
                                    print("None, this course does not have any student")
                                num1 = 1
                                for dict in course_class_1.student_list:
                                    student_name = dict.get("name")
                                    student_number = dict.get("student_number")
                                    student_average = dict.get("average_grade")
                                    student_attendance = dict.get("attendance_percentage")
                                    student_grade = dict.get("grade")
                                    student_age = dict.get("age")
                                    print(f"{num1}.    name:  {student_name}, grade: {student_grade}, age:{student_age}, student average: {student_average}%,"
                                          f" attendance percentage: {student_attendance},student_number:  {student_number}")
                                    num1 += 1
                                print("Teacher list:")
                                if len(course_class_1.teacher_list) == 0:
                                    print("None, since this course does not have any teacher")
                                num1 = 1
                                for dict in course_class_1.teacher_list:
                                    teacher_name = dict.get("name")
                                    teacher_role = dict.get("role")
                                    temp_dict = {"num": num1, "name": teacher_name, "role": teacher_role}
                                    temp_list_3.append(temp_dict)
                                    print(
                                        f"{num1}.    teacher_name:  {teacher_name}, teacher_role:  {teacher_role}")
                                    num1 += 1
                            elif command1 == "esc":
                                break
                            else:
                                print("-The command is out of range-")

        else:
            print("User have not create any course yet")
    elif command == "3":
        if len(course_list) == 0:
            print("There is no course created(Automatically back to last step)")
        else:
            file_path = "managed_file"
            for i in course_list:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(f"course name: {i["course_name"]}\n{i["course_name"]}'s student list:{i["course_class"].student_list}"
                              f"\n{i["course_name"]}'s teacher list:{i["course_class"].teacher_list}\n")
            print("save success")
    elif command == "4":
        print("see you next time")
        exit()
    else:
        print("-The command is out of range-")
