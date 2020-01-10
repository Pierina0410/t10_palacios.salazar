import libreria
def agregar_producto():
    input("Agregar producto1: ")
    print("Se ingreso producto1")
def agregar_producto2():
    input("Agregar producto2: ")
    print("Se ingreso producto2")

opc=0
max=3
while(opc!=max):
    print("######### MENU ##########")
    print("# 1. agregar producto1       #")
    print("# 2. agregar producto2            #")
    print("# 3. salir              #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_producto()
    if(opc==2):
        agregar_producto2()

print("Programa finalizado")
# fin_menu
