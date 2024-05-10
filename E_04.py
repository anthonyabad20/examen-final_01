import requests as rq


def obtener_usuario_por_id(id_usuario):
    url = f"https://jsonplaceholder.typicode.com/users/{id_usuario}"
    respuesta = rq.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None


usuario_06 = obtener_usuario_por_id(6)
usuario_08 = obtener_usuario_por_id(8)


if usuario_06 and usuario_08:

    usuario_06["nombre"] = "Usuario 6"
    usuario_06["edad"] = 45
    usuario_08["nombre"] = "Usuario 8"
    usuario_08["edad"] = 38

    if usuario_06["edad"] > usuario_08["edad"]:
        print(f"{usuario_06['nombre']} ({usuario_06['edad']}) "
              f"es mayor que {usuario_08['nombre']} ({usuario_08['edad']})")

    elif usuario_06["edad"] < usuario_08["edad"]:
        print(f"{usuario_08['nombre']} ({usuario_08['edad']}) "
              f"es mayor que {usuario_06['nombre']} ({usuario_06['edad']})")

    else:
        print(f"{usuario_06['nombre']} y {usuario_08['nombre']} "
              f"tienen la misma edad ({usuario_06['edad']})")
else:
    print("No se encontraron resultados de los usuarios con los ID .")
