# This python file  is for test all fuctions in the student class 
# this is for testing real life scenarios and many functions used in the file 

from modules.student.Student import studentClass

# step 1:student registration test

email = input("Enter your email : ")  
password=input("Enter your password : ") 

s1=studentClass()
s1.setuserNameandPassword(email, password)
# step 2: basic student details

full_name = input("Enter your full name : ")
date_of_birth = input("Enter your date of birth : ")    
gender = input("Enter your gender : ")
mobile_number = input("Enter your mobile number : ") 
preferred_language = input("Enter your preferred language : ")
school_college_name = input("Enter your school/college name : ")    
class_grade = input("Enter your class/grade : ")    
board_curriculum = input("Enter your board/curriculum : ")
academic_year = input("Enter your academic year : ")

s1.basicDetails(full_name, date_of_birth, gender, mobile_number, preferred_language, school_college_name, class_grade, board_curriculum, academic_year)


s1.save_to_database()
s1.setfullname_dob_gender_mobile(self, full_name, date_of_birth, gender, mobile_number):
        