import funciones


while True:
    try:
        tamaño_lista_02 = int(input("Ingrese el tamaño de la lista: "))
        if tamaño_lista_02 > 0:
            break
        else:
            print("El tamaño debe ser mayor que cero. Intente nuevamente.")
    except ValueError:
        print("Error: Ingrese un número entero. Intente nuevamente .")

funciones.lista_aleatoria(tamaño_lista_02)
funciones.calculo_raiz()
print("Se han escrito los números aleatorios y "
      "sus raíces cuadradas en 'notas.txt' exitosamente.")
