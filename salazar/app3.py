import libreria
def agregar_pais():
    input("Agregar Pais: ")
    print("Se ingreso Pais")

def agregar_capital():
    input("Agregar Capital: ")
    print("Se ingreso Capital")
#fin_def

opc=0
max=3
while(opc!=3):
    print("######### MENU ##########")
    print("# 1. Pais:              #")
    print("# 2. Capital            #")
    print("# 3. salir              #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)
#fin_while

    #Mapeo
    if(opc==1):
        agregar_pais()
    if(opc==2):
        agregar_capital()

print("fin del programa")
# fin de menu
