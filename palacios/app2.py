import libreria
def agregar_nombre():
    input("Agregar nombre: ")
    print("Se ingreso nombre")
def agregar_edad():
    input("Agregar edad: ")
    print("Se ingreso edad")

opc=0
max=3
while(opc!=max):
    print("######### MENU ##########")
    print("# 1. agregar nombre       #")
    print("# 2. edad              #")
    print("# 3. salir              #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_nombre()
    if(opc==2):
        agregar_edad()

print("Programa finalizado")
# fin_menu
