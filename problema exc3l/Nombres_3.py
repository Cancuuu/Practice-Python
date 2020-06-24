
#Nombres Integrantes
personas = [
"Elena Ana Vinagre",
"Karen Inti Morando",
"Boris Demián Pereyra",
"Ariadna Mora Orduña",
"Alamián Marcos Coti",
"Ailin Jazmín Nervo",
"Azucena Dasha Soldi",
"Agustín Ignacio Montero",
"Karen Daiana Otero"]

#output first name
def first():
    def first_name(name):
        #con .split cortamos los nombres
        cut = name.split(" ")
        
        #ahora devolemos el primer nombre
        print(cut[0])
        
    for nombre in personas:
        first_name(nombre)



def second():
    def second_name(name):
        #con .split cortamos los nombres
        cut = name.split(" ")
        
        #ahora devolemos el segundo nombre
        print(cut[1])
        
    for nombre in personas:
        second_name(nombre)


def surname():
    def surname(name):
        #con .split cortamos los nombres
        cut = name.split(" ")
        
        #ahora devolemos el apellido
        print(cut[2])
        
    for nombre in personas:
        surname(nombre)



user_input = input("nombre que queres saber:")

if user_input == "nombre":
    print(first())
elif user_input == "segundo nombre":
    print(second())
elif user_input == "apellido":
    print(surname())
else:
    print("Inserta un valor correcto. Pueden ser: nombre, segundo nombre o apellido")

