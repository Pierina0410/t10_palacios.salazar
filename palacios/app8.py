import libreria
def agregar_universidades():
    input("Agregar universidades: ")
    print("Se ingreso universidades")
def agregar_institutos():
    input("Agregar institutos: ")
    print("Se ingreso institutos")

opc=0
max=3
while(opc!=max):
    print("######### MENU ##########")
    print("# 1. agregar universidades     #")
    print("# 2. agregar institutos              #")
    print("# 3. salir              #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_universidades()
    if(opc==2):
        agregar_institutos()

print("Programa finalizado")
# fin_menu
