
def fib(N):
    """
    Imprimir lista de los primeros N numeros Fibonacci
    Ejemplo tomado de [1]
    """
    f0, f1 = 0, 1
    f = [1] * N
    for n in range(1, N):
        f[n] = f0 + f1
        f0, f1 = f1, f[n]

    return f

print(fib(10))
