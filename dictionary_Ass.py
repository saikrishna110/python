"""
Assignment-1:
WAP to create a one student info in dictionary. Dictionary should contain
'student_name, age, roll_no, class, section, percentage, college_name' student data.
Retrieve the student percentage from the dictionary.
"""
d1={"student_name":'sai','age':21,'roll_no':403,'section':'A','percentage':62.9,'college_name':"SIET"}
print(d1['percentage'])


"""
Assignment-2:
WAP to create a 3 students info in dictionary. Dictionary should contain 3 students data with 'student_names,
ages, roll_nos, classes, sections, percentages, university_names' keys and values can be stored in list/tuple.
Retrieve the student_3 class from the dictionary.
"""
student_names={"students":[{"student1":{"student_name":'sai','age':21,'class':['B Com'],'roll_no':403,'section':'A','percentage':62.9,'college_name':"SIET"}},
                           {"student2":{"student_name":'vasu','age':22,'class':['BCA'],'roll_no':405,'section':'A','percentage':65.6,'college_name':"SIET"}},
                           {"student3":{"student_name":'pavan','age':23,'class':['Btech'],'roll_no':408,'section':'A','percentage':70.5,'college_name':"SIET"}}]}

print(student_names["students"][-1]['student3']['class'])
"""
Assignment-3:
WAP to create a 4 employees data in a nested dictionary.
Dictionary should contain 4 employees data, each employee data should be represented in a dictionary
Each sub dictionary should have 'employee_name,salary,Designation' keys.
Retrieve the 3rd employee designation from the nested dictionary.
"""
employees_data={"employee1":{"employee_name":"Vasu","salary":25000,"Designation":"Developer"},
                "employee2":{"employee_name":"Pavan","salary":20000,"Designation":"Tester"},
                "employee3":{"employee_name":"Tejas","salary":20000,"Designation":"Tester"},
                "employee4":{"employee_name":"Sai","salary":20000,"Designation":"Unknown"}}
print(employees_data["employee3"])