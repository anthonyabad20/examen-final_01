import random
import math


def lista_aleatoria(tamaño, name_archivo = "notas.txt"):
    lista_02 = []
    for _ in range(tamaño):
        lista_02.append(random.randint(4, 60))
    with open(name_archivo, "w") as file:
        for numero in lista_02:
            file.write(str(numero) + "\n")


def calculo_raiz(name_archivo = "notas.txt"):
    with open(name_archivo, "r+") as file:
        lineas = file.readlines()
        file.seek(0)
        for linea in lineas:
            valor = float(linea.strip())
            raiz_cuadrada = math.sqrt(valor)
            file.write(f"{raiz_cuadrada:.3f}\n")
        file.truncate()
