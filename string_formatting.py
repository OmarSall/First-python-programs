# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# # message = "Hello %s %s!" % (name,surname)      #string formatting expression (percentage operator)
# message = f"Hello {name} {surname}"     #for newer version
# print(message)



def fun(name):
    message = f"Hi {name.title()}"
    return message

print(fun('omar'))
