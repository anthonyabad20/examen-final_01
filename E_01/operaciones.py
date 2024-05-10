
import random
def lista_aleatoria():
    lista = []
    for _ in range(10):
        lista.append(random.randint(1, 30))

    print("Lista de nuemros aleatorios es :", lista)
    return lista


def eliminar_repetidos(lista):

    lista_sin_repetidos = list(set(lista))
    print("Lista de numeros sin repetir es :", lista_sin_repetidos)
    return lista_sin_repetidos


def ordenar_lista(lista):

    lista_mayor_menor = sorted(lista, reverse=True)
    lista_menor_mayor = sorted(lista)
    print("Lista ordenada de mayor a menor:", lista_mayor_menor)
    print("Lista ordenada de menor a mayor:", lista_menor_mayor)
    return lista_mayor_menor, lista_menor_mayor


def mayor_numero_par(lista):

    pares = [num for num in lista if num % 2 == 0]
    if pares:
        mayor_par = max(pares)
        print("El numero mayor par es :", mayor_par)
        return mayor_par
    else:
        print("No hay números pares en la lista.")
        return None
