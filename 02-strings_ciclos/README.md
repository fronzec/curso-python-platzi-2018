# Strings y ciclos
## Strings
Los strings o** cadenas de textos** tienen un comportamiento distintos a otros tipos como los booleanos, enteros, floats. Las cadenas son secuencias de caracteres, todas se pueden acceder a través de un índice.
- apple = "apple"
    - apple[0]

Podemos saber la longitud de un string, cuántos caracteres se encuentran en esa secuencia. Lo podemos saber con la *built-in function* global llamada `len`.

Algo importante a tener en cuenta cuando hablamos de strings es que estos son inmutables, esto significa que cada vez que modificamos uno estamos generando un nuevo objeto en memoria.

El índice de la primera letra es 0, en la programación se empieza a contar desde 0

En un string se puede guardar el texto que queramos, la unica limitante es la cantidad de memoria que tengamos.

Algo importante en python es que los string son reutilizados a lo largo del programa para ahorrar memoria.

Para conocer la dirección de un objeto en memoria podemos usar la funcion `id(<objeto>)`

## Operaciones con strings
Los strings tienen varios métodos que nosotros podemos utilizar.

- `upper`: convierte todo el string a mayúsculas
- `lower`: convierte todo el string a minúsculas
- `find`: encuentra el indice en donde existe un patrón que nosotros definimos
- `startswith`: significa que empieza con algún patrón.
- `endswith`: significa que termina con algún patrón
- `capitalize`: coloca la primera letra en mayúscula y el resto en minúscula
- `in` y `not in` (Operadores de pertenencia) nos permite saber con cualquier secuencia sin una subsecuencia o substrings se encuentra adentro de la secuencia mayor.
- `dir`: Nos dice todos los métodos que podemos utilizar dentro de un objeto.
- `help`: nos imprime en pantalla el docstrings o comentario de ayuda o instrucciones que posee la función. Casi todas las funciones en Python las tienen.

Las comparacione de strings en python son lexicograficas, es decir 'A' no es igual que 'a'
## Slices
Slices en españoll significa "rebanada", si tenemos una secuencia de elementos y queremos una rebanada tenemos
una sintaxis para definir que pedazos queremos de una secuencia

- `secuencia[comienzo:final:pasos]`

- El comienzo es inclusivo y el primer indice es 0
- El final no es inclusivo
## For loops
Los for loops nos permiten iterar a través de una secuencia

for loops:
   - Tienen dos keywords `break` y `continue` que nos permiten salir anticipadamente del ciclo o saltar a la siguiente iteracion respectivamente.
   - Se usan cuando se quiere ejecutar varias veces una o varias instrucciones.
   - for [variable] in [secuencia]:


Es una convención usar la letra `i` como variable en nuestro for, pero podemos colocar la que queramos.

`range`: Nos da un objeto rango, es un iterador sobre el cual podemos generar secuencias, esto es algo nuevo en python 3.

## While loops
Al igual que las for loops, las while loops nos sirve para iterar, pero las for loops nos sirve para iterar a lo largo de una secuencia mientras que las while loops nos sirve para iterar mientras una condición sea verdadera.

Si no tenemos un mecanismo para convertir el mecanismo en falsedad, entonces nuestro while loops se ira al infinito(infinite loop)

Si en algún momento caemos en un while loop en sistemas UNIX podemos parar la ejecución de un programa usando `CTRL + C`

## Iterators and generators
Un iterador es un objeto que cumple con los requisitos de Iteration Protocol y por lo tanto
puede ser utilizado en ciclos, por ejemplo:

```python
for i in range(10):
    print(i)
```

En este caso, la función range es un iterable que regresa un nuevo valor en cada ciclo.

Para crear un objeto que sea un iterable, y por lo tanto, implemente el protocolo de iteración, debemos hacer tres cosas:
-  Crear una clase que implemente los métodos iter y next
- iter debe regresar el objeto sobre el cual se iterará
- next debe regresar el siguiente valor y aventar la excepciób StopIteration cuando ya no hayan elementos sobre los cual  iterar

En otro lado los generadores son simplemente una funcion rápida de crear iterables sin la
necesidad de declarar una clase que implemente el protocolo de iteración.

Para crear un generator simplemente declaramos una función y utilizamos el keyword yield en vez de return
para regresar el siguiente valor en una iteración. Por ejemplo:

```python
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
```

Es importante recalcar que una vez que se ha agotado un generator ya no podemos utilizarlo y debemos crear una instancia nueva. Por ejemplo:
```
fib1 = fibonacci(20)
fib_nums = [num for num in fib1]

double_fib_nums = [num * 2 for num in fib1]  # no va a funcionar
double_fib_nums = [num * 2 for num in fibonacci(30)]  # sí funciona
```