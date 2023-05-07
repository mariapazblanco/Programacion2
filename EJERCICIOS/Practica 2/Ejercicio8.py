"""Tuple, Enumerate, Zip, Args.





from typing import Any, List, Tuple

Contexto: Se tiene un programa que lee diferentes listas de una tabla en una
base de datos y se quieren combinar estas listas para que luego puedan crearse
los objetos de la capa de negocio.
"""
"""Toma dos listas y devuelve una tupla de duplas con los componentes de
    las listas.

    Restricción:
        - Utilizar un bucle FOR.
        - Utilizar la función range.
        - Utilizar índices.
    """

nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]


def combinar_basico(nombres: List[str], precios: List[float]) -> Tuple[Any]:

    resultado = []
    for i in range(len(nombres)):
        nombre = nombres[1]
        precio = precios[1]

        resultado.append((nombre, precio))

    return tuple(resultado)

    combinacion = combinar_basico(nombre_articulos, precio_articulos, )


# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48),
    ("lámpara", 16.42),
    ("shampoo", 5.2),
)

assert combinar_basico(nombre_articulos, precio_articulos) == respuesta
# NO MODIFICAR - FIN


###############################################################################
"""Re-Escribir utilizando enumerate y agregando un nuevo componente.

    Restricción:
        - Utilizar un bucle FOR.
        - No Utilizar la función range.
        - No Utilizar la función zip.

    Referencia: https://docs.python.org/3/library/functions.html#enumerate
    """

id_articulos = [6852, 1459, 3578]


def combinar_enumerate(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:  # noqa: E501

    resultado[]
    for i, nombre in enumerate(nombres):
        precio = precios[1]
        id_ = ids[1]

        tupla = (id_, nombre, precio, )
        resultado.append(tupla)

    return tuple(resultado)

    combinacion = combinar_enumerate(nombre_articulos, precio_articulos, id_articulos)


# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar_enumerate(nombre_articulos, precio_articulos, id_articulos) == respuesta  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################
"""Re-Escribir utilizando zip.

    Restricción:
        - Utilizar un bucle FOR.
        - No utilizar la función range.
        - No utilizar la función enumerate.
        - No utilizar índices.
    Referencia: https://docs.python.org/3/library/functions.html#zip
    """

id_articulos = [6852, 1459, 3578]


def combinar_zip(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]: # noqa: E501

    resultado=[]
    for nombre, precio, id_ in zip(nombres, precios, ids):
        tupla = (id_, nombre, precio)
        resultado.append(tupla)
    return tuple(resultado)

    combinacion = combinar_zip(nombre_articulos, precio_articulos, id_articulos)


# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar_zip(nombre_articulos, precio_articulos, id_articulos) == respuesta  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################
"""Re-Escribir utilizando zip y una cantidad arbitraria de componentes.

   Restricción:
       - Utilizar un bucle FOR.
       - No utilizar la función range.
       - No utilizar la función enumerate.
       - No utilizar índices.

   Referencia: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists  # noqa: E501
   """

id_articulos = [6852, 1459, 3578]
categoria_articulos = ["hogar", "libreria", "perfumeria"]
importado_articulos = [True, False, True]


def combinar_zip_args(*args) -> Tuple[Any]:

    # Crear una lista vacía para almacenar las tuplas
    resultado = []

    # Iterar sobre las tuplas formadas por los elementos correspondientes de cada lista en paralelo utilizando zip
    for elementos in zip(*args):
        # Crear una tupla con los elementos de cada lista y agregarla a la lista de resultados
        tupla = tuple(elementos)
        resultado.append(tupla)

    # Convertir la lista de tuplas en una tupla y devolverla
    return tuple(resultado)

    combinacion = combinar_zip_args(nombre_articulos, precio_articulos, id_articulos, categoria_articulos,importado_articulos)


# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852, "hogar", True),
    ("lámpara", 16.42, 1459, "libreria", False),
    ("shampoo", 5.2, 3578, "perfumeria", True),
)

componentes = [
    nombre_articulos,
    precio_articulos,
    id_articulos,
    categoria_articulos,
    importado_articulos,
]

assert combinar_zip_args(*componentes) == respuesta
# NO MODIFICAR - FIN