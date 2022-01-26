from calculadora import sumar, restar, calcularPromedio

# Whitespace formatting


if (True):
    print("Hola")
else:
    print("Adios")

# Tipos de datos primitivos
# variables
dinero = 12123123.50
nombre = "Let's go"  # String

# Boolean
auto = True  # Si tengo auto
auto = False  # No tengo auto

# Codición
if (auto):
    print("Hola")
    print("Hola")
    print("Hola")
    print("Hola")
    print("Hola")
else:
    print("Adios")
    print("Adios")
    print("Adios")
    print("Adios")
    print("Adios")
    print("Adios")

# Cree dos variables nombradas ae bimprima la suma de ambas.
# Cree dos variables nombradas ay be imprima el resultado del exponente a^b
# Lea una variable entera nombrada age(use la input(...)función y convierta a int con int(...)) e imprima la edad hasta los 100 años. Por ejemplo, si la edad es 32, imprima Years to 100 are 68
# Lea una variable entera nombrada agepor el usuario y cree una variable nombrada isAdultcon Truesi la edad es mayor de 18 años, de lo contrario ponga False. Imprime la variable isAdult.
# Lea una variable decimal nombrada celsiuse imprima el equivalente en farenheitgrados. uso F = C * 9/5 + 32


# Array
# En python lists
lista = ["Ignacio", "Daniel", "Salvador", "Tomas"]
print(lista[1])
# Indice 0
cosas = [1, "Tzuzul", True, ["Ignacio", "Daniel", "Salvador", "Tomas"]]

print(cosas[0])

lista.append("Maxi")
print(lista)
print(lista[-1])

# Ciclos
# for
for alumno in lista:
    print("Hola", alumno)
    alumno = "Tzuzul"

print(lista)

if __name__ == '__main__':
    # range(len(lista)) -> 0,1,2,3,4
    for posicion in range(len(lista)):
        lista[posicion] = "Tzuzul"

    print(lista)

    suma = sumar(5, 6)

    print(suma)

    listaCalif = [1, 2, 3, 4, 8, 6, 2]
    listaCalif2 = [9, 8, 7, 6]
    listaCalif3 = [1, 2, 3]
    listaCalif4 = [1, 2, 3, 4, 8, 6, 2, 1, 2, 3, 4, 8, 6, 2]

    promedio1 = calcularPromedio(listaCalif)
    promedio2 = calcularPromedio(listaCalif2)
    promedio3 = calcularPromedio(listaCalif3)
    promedio4 = calcularPromedio(listaCalif4)

    promedioDePromedios = calcularPromedio([promedio1, promedio2, promedio3, promedio4])

    print(promedioDePromedios)


