# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     return the_mean

def mean(value):
    #if type(value) == dict:
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

student_grades = {"Marry": 9.1, "Sim": 8.8, "John":7.5}
print(mean([1,4,5]))
print(mean(student_grades))