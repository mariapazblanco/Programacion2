"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union

"""Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """
def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501

    numeros = []
    no_numeros = []
    for elementos in lista:
        if type(elementos) == int:
            numeros.append(elementos)
        else:
            no_numeros.append(elementos)
    return no_numeros + numeros


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################
"""Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """

def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501


    numeros = [elementos for elementos in lista if type(elementos == int)]
    no_numeros = [elementos for elementos in lista if type(elementos) != int ]

    return no_numeros + numeros


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN