5lado=0
apotema=0
print("Esta aplicacion calcula el perimetro y el area de un terreno hexagonal")
print("introduce un lado del terreno hexagonal: ")
lado=int(input())
print("introduce el apotema del terreno hexagonal: ")
apotema=int(input())
perimetro=lado*6
area=(perimetro*apotema)/2
print("El perimetro del terreno hexagonal es:",perimetro, "y su area es:",area,)

