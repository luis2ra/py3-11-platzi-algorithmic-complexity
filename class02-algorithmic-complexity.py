import time
import sys


sys.setrecursionlimit(250000)

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)


def testear_factorial(n):
    print("n = ", n)
    comienzo = time.time()
    factorial(n)  # el resultado del factorial es de tipo 'int'
    final = time.time()
    print(final - comienzo) 

    comienzo = time.time()
    factorial_r(n)  # el resultado del factorial_r es de tipo 'int'
    final = time.time()
    print(final - comienzo)


if __name__ == '__main__':
    n = 1000
    testear_factorial(n)
    
    n = 2000
    testear_factorial(n)
    
    n = 2500
    testear_factorial(n)

    n = 5000
    testear_factorial(n)

    n = 10000
    testear_factorial(n)

    n = 20000
    testear_factorial(n)

    '''
    Para el valores cercanos a n=20940, en algunos casos, los calculos del 
    factorial recursivo da "Violación de segmento"
    '''
    # n = 20940
    # testear_factorial(n)
    
    # n = 50000
    # testear_factorial(n)
    # n = 200000
    # testear_factorial(n)
