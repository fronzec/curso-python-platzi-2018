# Built-in functions
# La funcion print imprime a salida estandar
# La funcion type regresa el typo de un valor
print(type(9))

# La funcion int convierte a entero un valor
print(int('5'))

# La funcion bool convierte un valor a booleano
print(bool('a'))
print(bool(''))

# La funcion float convierte un valor a flotante
print(float('4'))


# Custom functions
def suma_de_dos_numeros(x, y):
    return x + y


print(type(suma_de_dos_numeros))
print(suma_de_dos_numeros(1, 2))

suma_total = suma_de_dos_numeros(1, 2)
print(suma_total)
print(type(suma_total))
