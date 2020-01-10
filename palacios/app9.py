import libreria
def agregar_mes():
    input("Agregar mes: ")
    print("Se ingreso mes")

def agregar_dia():
    input("Agregar dia: ")
    print("Se ingreso dia")

opc=0
max=3
while(opc!=max):
    print("######### MENU ##########")
    print("# 1. agregar mes       #")
    print("# 2. agregar dia        #")
    print("# 3. salir              #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_mes()
    if(opc==2):
        agregar_dia()

print("Programa finalizado")
# fin_menu
