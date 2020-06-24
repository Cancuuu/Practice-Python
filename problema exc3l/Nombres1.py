
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



def CutName(name):
    #con .split cortamos los nombres
    cut = name.split(" ")
    
    #ahora devolemos el segundo nombre
    print(cut[1])
    

CutName(personas[7])
    


