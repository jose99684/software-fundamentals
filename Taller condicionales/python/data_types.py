numberx = 10
print(type(numberx))
numberx = 10.5
print(type(numberx))
numberx = 8J
print(type(numberx))

n1 = "1"
n2 = "3"
add = n1 + n2
print(add)

suma_datos = True and True 
print("Suma datos: ", suma_datos)
print(type(suma_datos))

################################

x = True - False
print(x) #1

x = True and False
print(x) #False

x = True & False
print(x) #False

x = True | False
print(x) #True

print("######################")
print("p and q")
print("######################")
print(f"V ^ V: {True and True}")
print(f"V ^ F: {True and False}")
print(f"F ^ V: {False and True}")
print(f"F ^ F: {False and False}")

print("######################")
print("p or q")
print("######################")
print(f"V ^ V: {True or True}")
print(f"V ^ F: {True or False}")
print(f"F ^ V: {False or True}")
print(f"F ^ F: {False or False}")

print("Hola \n" * 3)

print('5'+'3') #53

print("\n ###########################")
a = 10
b = 3
div = 10 / 3
print("DIV con /: ", div)
print("Resultado sin decimales: ", int(div))
print(type(div))

div = 10 // 3
print("DIV con //: ", div)
print(type(div)) # El doble // muestra solo la parte Z de la div

print("Tipo de 3.14: ", type(3.14))

x = True # Bool
y = '' \
'True' # String
z = "True" # String
w = '''
    true
''' # String
print(type(x))
print(type(y))
print(type(z))
print(type(w))

div = 10 / 0
print(div)
