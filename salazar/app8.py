import libreria

def agregar_cemento():
    input("Agregar Cemento: ")
    print("Se ingreso Cemento")

def agregar_fierro():
    input("Agregar Fierro: ")
    print("Se ingreso Fierro")

opc=0
max=3
while(opc!=3):
    print("########### MENU #############")
    print("# 1. Cemento                 #")
    print("# 2. Fierro                  #")
    print("# 3. salir                   #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_cemento()
    if(opc==2):
        agregar_fierro()

print("Programa finalizado")
# fin de menu
