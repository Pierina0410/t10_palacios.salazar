import libreria
def agregar_nota():
    input("Agregar nota1: ")
    print("Se ingreso nota2")

def agregar_nota2():
    input("Agregar nota2: ")
    print("Se ingreso nota2")

opc=0
max=3
while(opc!=max):
    print("######### MENU ##########")
    print("# 1. agregar nota       #")
    print("# 2. nota2              #")
    print("# 3. salir              #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_nota()
    if(opc==2):
        agregar_nota2()

print("Programa finalizado")
# fin_menu
