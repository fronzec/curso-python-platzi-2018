x = 2
y = 3
a = 5
b = 6

print('De acuerdo a los siguientes valores de variables')
print('x=', x)
print('y=', y)
print('a=', a)
print('b=', b)
print('Sabemos que...')

if x == y:
    print('"x" es igual que"y"')
else:
    print('"x"no es igual que"y"')

if x < y:
    print('"x" es menor que"y"')

if x > y:
    print('"x" es mayor que"y"')

if y < x:
    print('"y" es menor que"x"')

if y > x:
    print('"y" es mayor que"x"')

if x < y and a < b:
    print('"x" es menor que"y" y "a" es menor que"b"')

if x < y or a > b:
    print('"x" es menor que"y" o "a" es mayor que"b"')

if x > y or a < b:
    print('"x" es mayor que"y" o "a" es mayor que"b"')
