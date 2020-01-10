import libreria
def agregar_nombre():
    input("Agregar tuberculos: ")
    print("Se ingreso tuberculos")
def agregar_edad():
    input("Agregar verduras: ")
    print("Se ingreso verduras")

opc=0
max=3
while(opc!=max):
    print("######### MENU ##########")
    print("# 1. agregar tuberculos       #")
    print("# 2. agregar verduras         #")
    print("# 3. salir              #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_tuberculos()
    if(opc==2):
        agregar_verduras()

print("Programa finalizado")
# fin_menu
