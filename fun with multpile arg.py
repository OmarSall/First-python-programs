# def area(a,b):
#     return a * b

# def fun (a,b):
#     return a + b

# x = fun('Omar','Salloum')
# print(x)

# def mean(*args):
#     return sum(args) / len(args)             #returns a TUPLE

# print(mean(1,2,3,4))


# def fun(*args):
#  args = [x.upper() for x in args]
#  return sorted(args)

# x = fun('omar','natalia','amelia')
# print(x)

# def mean(**kwarg):
#     return kwarg

# print(mean(a=1,b=2,c=3))

def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a = 5, b = 2, c = 2))
