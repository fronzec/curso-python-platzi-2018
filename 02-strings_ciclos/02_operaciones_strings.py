mexico = "México"

print(mexico.upper())
print(mexico.find('xi'))
print(mexico.startswith('M'))
print(mexico.startswith('X'))
print(mexico.endswith('co'))
print(mexico.endswith('CO'))

# Nos dice todos los métodos que podemos utilizar dentro de un objeto.
print(dir(mexico))

# nos imprime en pantalla el docstrings o comentario de ayuda o instrucciones que posee la función.
print(help(str))

print("*" * 50)

# Operadores de pertenencia, nos permiten sabes si un substring, es decir una subsecuencia se encuentra en la secuencia mayor
# Distingue entre maysuculas y minusculas
print("Operadores de pertenencia")
var_string = "Hola"
print('var_string = "Hola"')
if "Ho" in var_string:
    print('if "Ho" in var_string :')
    print('The substring "Ho" is into the string "Hola" ')

print('*' * 50)

if "mundo!" not in var_string:
    print('if "mundo!" not in var_string :')
    print('var_string += "mundo!"')
    var_string += " mundo!"
    print("var_string = ", var_string)

print("*" * 50)


# Ejemplo de como crear un docstring para una funcion que creemos
def mi_funcion():
    """
    Este es un texto de ayuda de como utilizar nuestra funcion
    :return:
    """
    pass


print(help(mi_funcion))
