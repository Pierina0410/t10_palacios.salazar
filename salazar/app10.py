import libreria

def ingresar_universidad():
    input("Agregue nombre de la Universidad: ")
    print("Se ingreso nombre de la universidad")

def ingresar_facultad():
    input("Agregar Facultad: ")
    print("Se ingreso nombre de la Facultad")

opc=0
max=3
while(opc!=3):
    print("########### MENU #############")
    print("# 1. Universidad             #")
    print("# 2. Facultad                #")
    print("# 3. salir                   #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        ingresar_universidad()
    if(opc==2):
        ingresar_facultad()

print("Programa finalizado")
# fin de menu
