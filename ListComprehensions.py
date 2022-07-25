# temps = [221, 234, 340, 230]

# new_temps = [temp / 10 for temp in temps]

# print(new_temps)

# temps = [221, 234, 340,-9999, 230]

# new_temps = [temp / 10 for temp in temps if temp != -9999]

# print(new_temps)

# def foo(lista):
#     new_lista = [element for element in lista if isinstance(element, int)]
#     return new_lista

# print(foo([99,'nodata',64, 98, 'no data']))

# new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

# def foo(lista):
#     new_lista = [i if isinstance(i,int) else 0 for i in lista]
#     return new_lista

lista = ['1.2', '3.4','2.2']

def sum(lista):
    return sum([float(i) for i in lista])


sum(['1.2', '3.4','2.2'])