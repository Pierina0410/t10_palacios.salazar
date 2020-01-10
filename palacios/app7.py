import libreria
def agregar_planetas():
    input("Agregar planetas: ")
    print("Se ingreso planetas")
def agregar_satelite():
    input("Agregar satelites: ")
    print("Se ingreso satelites")

opc=0
max=3
while(opc!=max):
    print("######### MENU ##########")
    print("# 1. agregar planetas       #")
    print("# 2. agregar satelites           #")
    print("# 3. salir              #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_planetas()
    if(opc==2):
        agregar_satelite()

print("Programa finalizado")
# fin_menu
