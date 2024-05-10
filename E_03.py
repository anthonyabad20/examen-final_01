import time


def medicion_time(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print(f"Tiempo de ejecución de {funcion.__name__}: "
              f"{tiempo_ejecucion:.3f} segundos")
        return resultado
    return wrapper


@medicion_time
def multiplicar_numeros(**numeros):
    producto = 1
    for valor in numeros.values():
        producto = producto * valor
    return producto


producto_01 = multiplicar_numeros(num1=15, num2=25, num3=15, num4=20)
print("El resultado de la multiplicación resultado 1 es "
      ": {}".format(producto_01))

producto_02 = multiplicar_numeros(a=1, b=2, c=9)
print("El resultado de la multiplicación resultado 2 es "
      ": {}".format(producto_02))

producto_03 = multiplicar_numeros(x=4, y=8)
print("El resultado de la multiplicación resultado 3 es "
      ": {}".format(producto_03))
