from io import open

#Open .txt file with people name

file_text = open("nombres.txt", "r")
people = file_text.readlines()
file_text.close()

#write new name
def write_txt():
    writetxt = open("nombres.txt", "a")
    writetxt.write(input("\n introduci persona: "))



#output first name
def first():
    def first_name(name):
        #con .split cortamos los nombres
        cut = name.split(" ")
        
        #ahora devolemos el primer nombre
        print(cut[0])
        
    for nombre in people:
        first_name(nombre)



def second():
    def second_name(name):
        #con .split cortamos los nombres
        cut = name.split(" ")
        
        #ahora devolemos el segundo nombre
        print(cut[1])
        
    for nombre in people:
        second_name(nombre)


def surname():
    def surname(name):
        #con .split cortamos los nombres
        cut = name.split(" ")
        
        #ahora devolemos el apellido
        print(cut[2])
        
    for nombre in people:
        surname(nombre)

user_input = input("Ingrese una de las siguientes opciones con el numero correspondiente \n 1) Nombre  \n 2) Segundo  \n 3) Apellido \n 4) Agregar un nombre \n ")

if user_input == "1":
    print(first())
elif user_input == "2":
    print(second())
elif user_input == "3":
    print(surname())
elif user_input == "4":
    print(write_txt())
else:
    print("Inserta un valor correcto. Pueden ser: nombre, segundo nombre o apellido")

print(input("\n press enter to exit"))

