from clases.Ciclista import Ciclista

Ciclista=Ciclista()

Ciclistas = []

cantidad= int (input("Digite la cantidad de ciclistas"))

for i in range(cantidad):
    Ciclista.nombre=(input("Digite nombre: "))
    Ciclista.edad=int(input("Digite la edad: "))
    Ciclista.pais=(input("Digite el pais: "))
    Ciclista.tiempo=int(input("Digite el tiempo: "))


