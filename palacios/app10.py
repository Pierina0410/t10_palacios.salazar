import libreria
def agregar_mediterraneos():
    input("Agregar paises mediterraneos: ")
    print("Se ingreso paises mediterraneos")
def agregar_costeros():
    input("Agregar paises costeros: ")
    print("Se ingreso paises costeros")

opc=0
max=3
while(opc!=max):
    print("######### MENU ##########")
    print("# 1. agregar paises mediterraneos       #")
    print("# 2. aregar paises costeros             #")
    print("# 3. salir              #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_mediterraneos()
    if(opc==2):
        agregar_costeros()

print("Programa finalizado")
# fin_menu
0
