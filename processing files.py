# myfile = open("fruits.txt")
#print(myfile.read())

# content = myfile.read()

# myfile.close()

# print(content)

# with open("fruits.txt") as myfile:
#     content = myfile.read()

# with open("vegetables.txt", "w") as myfile:
#   myfile.write('Tomato\nCucumber\nOnion\n')
#   myfile.write("Garlic")

# def fun(character, filepath = "bear.txt"):
#     file = open(filepath)
#     content = file.read()
#     return content.count(character)

# with open("file.txt","w") as myfile:
#     myfile.write('snail\n')
    
# myfile.close()

# with open("bear.txt", "r") as myfile:
#     content = myfile.read()
#     first_90 = content[:90]

# with open("first.txt",'w') as file:
#     file.write(first_90)

# myfile.close()
# file.close()

# with open ("fruits.txt", "a+") as myfile:
#     myfile.write("Okra")
#     myfile.seek(0)
#     content = myfile.read()

# print(content)

# with open("bear1.txt", "r") as myfile:
#      content = myfile.read()
     
# with open("bear2.txt",'a+') as file:
#      file.write(content)

with open("data.txt",'a+') as myfile:
    myfile.seek(0)
    content = myfile.read()
    myfile.seek(0)
    myfile.write(content)
    myfile.write(content)