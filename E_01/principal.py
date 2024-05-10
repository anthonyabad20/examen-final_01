import operaciones

list_aleat = operaciones.lista_aleatoria()
list_sin_repetir = operaciones.eliminar_repetidos(list_aleat)
list_descendente,list_ascendente = operaciones.ordenar_lista(list_sin_repetir)
mayor_valor_par = operaciones.mayor_numero_par(list_sin_repetir)
