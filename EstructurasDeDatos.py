if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15]
    lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz

    last = numeros[-1]
    print(last)

    lista_cinco = []

    for i in range(5):
        lista_cinco.append(numeros[i])

    print(lista_cinco)

    primeros_cinco = numeros[:5]
    print(primeros_cinco)

    ultimos_cinco = numeros[5:]
    print(ultimos_cinco)

    numeros_en_medio = numeros[3:6]
    print(numeros_en_medio)

    numeros_copia = numeros[:]
    print(numeros_copia)

    tres_en_tres = numeros[3:10:3]
    print(tres_en_tres)

    numeros_al_reves = numeros[::-1]
    print(numeros_al_reves)

    print(4 in tres_en_tres)

    union = numeros_en_medio + tres_en_tres
    print(union)



