def lista_numeros_pares(n):

    pares = []

    for i in range(1, n+1):
        if i % 2 == 0:
            pares.append(i)

    return pares