def sumar(num1, num2):
    return num1 + num2


def restar(num1, num2):
    return num1 - num2

# Crear funcion: def
# parametros: lista
def calcularPromedio(lista):
    suma = 0
    for numero in lista:
        #suma = suma + numero
        suma += numero # Lo mismo que lo de arriba

    promedio = suma / len(lista)
    return promedio


if __name__ == '__main__':
    print("Hola")
