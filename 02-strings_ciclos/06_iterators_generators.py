# Iterators
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

## iterate through it using next()

# prints 4
print(next(my_iter))

# prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

# prints 0
print(my_iter.__next__())

# prints 3
print(my_iter.__next__())

## This will raise error, no items left
next(my_iter)


# Generatos

def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


fib1 = fibonacci(20)
fib_nums = [num for num in fib1]

double_fib_nums = [num * 2 for num in fib1]  # no va a funcionar
double_fib_nums = [num * 2 for num in fibonacci(30)]  # sí funciona
