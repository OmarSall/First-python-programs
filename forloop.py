# colors = [11, 34, 98, 43, 45, 54, 54]

# for i in colors:
#     print(i)

# student_grades = {"Marry": 9.1, "Sim":8.8, "Johm": 7.5}

# for grades in student_grades.items():
#     print(grades)

# for grades in student_grades.keys():
#     print(grades)

# for grades in student_grades.values():
#     print(grades)

# phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
# for key, value in phone_numbers.items():
#     print(f"{key} has as phone number {value}")

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
   # print(f"{value.replace( '+' , '00')}")
   print(value.replace("+","00"))