import libreria

def agregar_silla():
    input("Agregar modelo de Silla: ")
    print("Se agrego modelo de silla")

def agregar_mesa():
    input("Agregar modelo de Mesa: ")
    print("Se agrego mesa")

opc=0
max=3
while(opc!=3):
    print("########### MENU #############")
    print("# 1. Silla                   #")
    print("# 2. Mesa                    #")
    print("# 3. salir                   #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_silla()
    if(opc==2):
        agregar_mesa()

print("Programa finalizado")
# fin_de_menu
