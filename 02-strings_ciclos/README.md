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

