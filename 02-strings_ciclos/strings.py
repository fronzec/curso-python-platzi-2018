"""
En python las cadenas(strings), son secuencias a las quese pueden
acceder a través de un índice
cadena = "manzana"
cadena[0] = "m"
El índice dela primera letra es 0, enla programaciónse empieza a contar desde 0

"""
country = "México"
print(country[0])
print(country[1])
print(country[2])
print(country[3])
print(country[4])
print(country[5])

# Se puede acceder desde el final usando indices negativos
print(country[-1])
print(country[-2])
print(country[-3])
print(country[-4])
print(country[-5])
print(country[-6])

second_letter = country[1]

# Para obtener la direccion de memoria de un objeto podemos usar la funcion id()
print(id(second_letter))
other_var = 'é'
print(id(other_var))

# La misma letra en mayuscula y minuscula se representa de manera diferente
print(id('a'))
print(id('A'))
