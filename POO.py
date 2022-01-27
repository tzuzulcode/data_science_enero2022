# POO : Programación Orientada a Objetos
# OOP: Object Oriented Programming

class Persona:
    # Atributos
    nombre = ""
    edad = 0
    nacionalidad = ""
    genero = ""
    # atributos privados
    __password = "54321"

    # constructor
    # Inicializar información
    def __init__(self, nombre, edad, nacionalidad, genero):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.genero = genero
        self.__password

    def __get_password(self):
        return self.__password[:4]

    def __set_password(self, password):
        if len(password) > 5:
            self.__password = password
        else:
            self.__password = self.__password
            print("Password too short")

    password = property(__get_password, __set_password)


class Rock(Persona):
    gusto = "Música Rock"

class Pop(Persona):
    gusto = "Música Pop"
    artistas_favoritos = ["Artista pop"]


if __name__ == '__main__':
    jose = Rock("José Francisco", 23, "Mexicana", "Masculino")
    print(jose.gusto)
    print(jose.nombre)
    jose.password = "1234"
    print(jose.password)

    maxi = Pop("Maximiliano Colque", 23, "Argentina", "Masculino")
    print(maxi.gusto)

    lista_personas = [jose, maxi]

    for persona in lista_personas:
        print(persona.nombre)
        print(persona.gusto)
        print(persona.edad)
        if hasattr(persona,'artistas_favoritos'):
            print(persona.artistas_favoritos)

    edades = [persona.edad for persona in lista_personas ]

    print(edades)
