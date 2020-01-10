import libreria
def agregar_nombre():
    input("Ingrese nombre: ")
    print("Se agrego el nombre")

def agregar_apellido():
    input("Ingrese apellido: ")
    print("Se agrego el apellido")

def agregar_edad():
    input("Ingrese edad: ")
    print("Se agrego la edad")
#fin_def


opc=0
max=4
while(opc!=max):
    print("########## MENU ##########")
    print("#1. Agregar nombre:      #")
    print("#2. Agregar apellido:    #")
    print("#3. Agregar edad:        #")
    print("#4. Salir                #")
    print("##########################")
    opc=libreria.pedir_numero("Ingrese opcion:",1,4)
#fin_while

#Mapeo
    if (opc==1):
        agregar_nombre()
    if (opc==2):
        agregar_apellido()
    if (opc==3):
        agregar_edad()


print("Programa finalizado")

#din_menu
