import libreria
def agregar_playas():
    input("Agregar playas: ")
    print("Se ingreso playas")
def agregar_rios():
    input("Agregar rios: ")
    print("Se ingreso rios")

opc=0
max=3
while(opc!=max):
    print("######### MENU ##########")
    print("# 1. agregar playas       #")
    print("# 2. aregar rios              #")
    print("# 3. salir              #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_playas()
    if(opc==2):
        agregar_rios()

print("Programa finalizado")
# fin_menu
