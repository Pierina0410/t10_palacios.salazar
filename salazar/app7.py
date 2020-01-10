import libreria

def agregar_fruta():
    input("Agregar Fruta: ")
    print("Se ingreso nombre dela fruta")

def agregar_verdura():
    input("Agregar Verdura: ")
    print("Se ingreso nombre de verdura")

opc=0
max=3
while(opc!=3):
    print("########### MENU #############")
    print("# 1. Fruta                   #")
    print("# 2. Verdura                 #")
    print("# 3. salir                   #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_fruta()
    if(opc==2):
        agregar_verdura()

print("Programa finalizado")
# fin de menu
