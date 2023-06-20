# Validacion del for
'''
Verificamos el recorrido de un for igual a 2000 (repite el ciclo)
'''

def my_func():
    respuesta = 0
    for i in range(2000):
        respuesta += 1
    return respuesta


if __name__ == '__main__':
    print(my_func())
